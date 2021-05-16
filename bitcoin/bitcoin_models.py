import random
import sys

from typing import Dict

sys.path.append("..")

from loguru import logger

from sim.base_models import *
from messages import InvMessage, GetDataMessage

logger.remove()
logger.add(sys.stdout, level='INFO')
logger.add('logs/bitcoin_logs.txt', level='DEBUG')


class Block(Item):
    def __init__(self, miner: Node, sender_id: str, timestamp: int, created_at: int, prev_id: str):
        super().__init__(timestamp, sender_id, 0, created_at)
        self.prev_id = prev_id
        self.size = 1300000  # TODO
        self.miner = miner

    def __str__(self) -> str:
        return f'BLOCK (id:{self.id}, prev: {self.prev_id})'


class Transaction(Item):
    pass  # TODO


class Miner(Node):
    def __init__(self, name: str, pos_x: float, pos_y: float, mine_power: int, mine_cost=0, timestamp=0):
        super().__init__(pos_x, pos_y, timestamp)
        self.name = name
        self.mine_power = mine_power
        self.mine_cost = mine_cost
        self.blockchain: Dict[str, Block] = dict()
        self.heads: List[Block] = []
        self.difficulty = 0.01
        logger.info(f'CREATED MINER {self.name}')

    def step(self):
        super().step()
        items = self.get_items()
        for item in items:
            self.__consume(item)

        if random.random() <= self.mine_power * self.difficulty:
            self.generate_block()

    def connect(self, node: Node):
        # link = Link(self, node, os.getenv('BANDWIDTH')) #TODO: bandwidth
        link = Link(self, node, 5000000)  # 5 MB/s
        self.outs.append(link)
        node.ins.append(link)

    def __consume(self, item: Item):
        if type(item) == Block:
            logger.info(f'[{self.timestamp}] {self.name} RECEIVED BLOCK {item.id}')
            self.add_block(item)
            self.__publish_block(item)
        elif type(item) == InvMessage:
            logger.debug(f'[{self.timestamp}] {self.name} RECEIVED INV MESSAGE FOR BLOCK {item.block_id}')
            if item.block_id not in self.blockchain.keys():
                logger.debug(f'[{self.timestamp}] {self.name} RESPONDED WITH GETDATA')
                msg = GetDataMessage(item.block_id, self.id, self.timestamp, 10, self.timestamp)
                self.__send_to(item.sender_id, msg)
        elif type(item) == GetDataMessage:
            logger.debug(f'[{self.timestamp}] {self.name} RECEIVED GETDATA MESSAGE FOR BLOCK {item.block_id}')
            self.__send_to(item.sender_id, self.blockchain[item.block_id])
        # removed getblockchain message until implementation of dynamic leave/join of miners

    # FIXME: public for testing
    def generate_block(self, prev=None) -> Block:
        if prev is None:
            prev = self.__choose_prev_block()
        block = Block(self, self.id, self.timestamp, self.timestamp, prev.id)
        logger.success(f'[{self.timestamp}] {self.name} GENERATED BLOCK {block.id} ==> {prev.id}')
        self.add_block(block)
        self.__publish_block(block)
        return block

    # FIXME: public for testing
    # remove block.prev from heads if exists and add block to blockchain
    def add_block(self, block):
        self.blockchain[block.id] = block
        prev = list(filter(lambda head: head.id == block.prev_id, self.heads))
        if len(prev) > 0:
            self.heads.remove(prev[0])
        self.heads.append(block)

    def __publish_block(self, block: Block):
        for link in self.outs:
            msg = InvMessage(block.id, self.id, self.timestamp, 10, self.timestamp)
            link.send(msg)

    # returns the head of the longest chain
    def __choose_prev_block(self) -> Block:
        lengths = [self.__get_length(block) for block in self.heads]
        return self.heads[lengths.index(max(lengths))]

    def __send_to(self, node_id: str, item: Item):
        for link in self.outs:
            if link.end.id == node_id:
                link.send(item)

    # get length of chain starting ending at `block`
    def __get_length(self, block, count=0):
        prev = self.blockchain.get(block.prev_id, None)
        if prev is not None:
            return self.__get_length(prev, count + 1)
        else:
            return count

    # -- LOGGING / INFO METHODS --
    def log_blockchain(self):
        head = self.__choose_prev_block()
        logger.warning(f'{self.name}')
        logger.warning(f'\tBLOCKCHAIN:')
        for block in self.blockchain.values():
            logger.warning(f'\t\t{block}')
        logger.warning(f'\tHEADS:')
        for block in self.heads:
            if block == head:
                logger.warning(f'\t\t*** {block}')
            else:
                logger.warning(f'\t\t{block}')

    def log_stats(self):
        logger.warning(f'{self.name}')
        logger.warning(f'\tSTATS:')
        logger.warning(f'\t\tAverage block interval: {self.avg_block_interval()}')

    def avg_block_interval(self):
        total, count = 0, 0
        head = self.__choose_prev_block()
        while True:
            block = self.blockchain.get(head.prev_id, None)
            if block is None:
                break
            count += 1
            total += head.created_at - block.created_at
            head = block
        return total / count
