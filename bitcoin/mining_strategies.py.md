# mining_strategies.py

## Explanation
This Python script contains classes that define different mining strategies for a Bitcoin miner. The strategies include a default no-mining strategy, an honest mining strategy that follows the Bitcoin protocol, and a selfish mining strategy that attempts to gain more rewards by keeping mined blocks private.

## Dependencies
- `loguru`: Used for logging.
- `bitcoin.models`: Provides the `Miner` and `BTCBlock` classes.
- `bitcoin.consensus`: Provides the `Reward` class.

## Classes

### NullMining
This class represents the default no-mining strategy. It corresponds to the full nodes in Bitcoin.

#### \_\_init\_\_
Initializes the NullMining instance.

#### setup
This method sets up the mining strategy for a node.
- Parameters: `node` (Miner)
- Returns: None

#### choose_head
Returns the head of the longest chain.
- Parameters: `node` (Miner)
- Returns: `max_block` (BTCBlock)

#### generate_block
Specifies the strategy for mining a new block. This method is not implemented in this class.
- Parameters: `node` (Miner), `prev` (BTCBlock)
- Returns: None

#### receive_block
Specifies the strategy for receiving a block. The given block is published to the node's peers if `relay` is True.
- Parameters: `node` (Miner), `block` (BTCBlock), `relay` (bool), `shallow` (bool)
- Returns: None

### HonestMining
This class extends NullMining and implements an honest miner following the Bitcoin protocol.

#### \_\_init\_\_
Initializes the HonestMining instance.

#### generate_block
Generates and returns a Block. If `prev` is not provided, the block is chosen according to the protocol.
- Parameters: `node` (Miner), `prev` (BTCBlock)
- Returns: `block` (BTCBlock)

#### receive_block
Receives a block and relays it to other nodes.
- Parameters: `node` (Miner), `block` (BTCBlock), `relay` (bool), `shallow` (bool)
- Returns: None

### SelfishMining
This class extends NullMining and implements a miner launching the selfish mining attack.

#### \_\_init\_\_
Initializes the SelfishMining instance.

#### setup
Sets up the mining strategy for a node. It also initializes a private chain for the node.
- Parameters: `node` (Miner)
- Returns: None

#### choose_head
Returns the head of the longest chain, either from the private chain or the public chain.
- Parameters: `node` (Miner), `private` (bool)
- Returns: `max_block` (BTCBlock)

#### generate_block
Generates a new block and adds it to the private chain.
- Parameters: `node` (Miner), `prev` (BTCBlock)
- Returns: `block` (BTCBlock)

#### receive_block
Receives a block and decides whether to publish the private chain based on the length difference between the private and public chains.
- Parameters: `node` (Miner), `block` (BTCBlock), `relay` (bool), `shallow` (bool)
- Returns: None

#### publish_private_chain
Publishes all blocks in the private chain to the public chain.
- Parameters: `node` (Miner)
- Returns: None

#### get_delta_prev
Returns the length difference between the private and public chains.
- Parameters: `node` (Miner)
- Returns: `priv_length - pub_length` (int)

## Example usage
```python
# Create a miner
miner = Miner()

# Create a mining strategy
strategy = HonestMining()

# Set up the strategy for the miner
strategy.setup(miner)

# Generate a block
block = strategy.generate_block(miner)

# Receive a block
strategy.receive_block(miner, block, relay=True)
```