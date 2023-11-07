# tx_modelings.py

## Explanation
This Python script contains classes that model transactions in a Bitcoin network. The classes generate transactions, publish them, receive them, fill blocks with transactions, update the mempool, and provide information about the mempool size and waiting transaction count. There are four classes: `TxModel`, `NoneTxModel`, `SimpleTxModel`, and `FullTxModel`. Each class represents a different model of transaction handling.

## Dependencies
- `sys`
- `heapq`
- `random`
- `bitcoin.models` (Miner, Block, Transaction)
- `bitcoin.messages` (InvMessage)
- `loguru` (logger)

## Classes

### TxModel
This is the base class for transaction models. It contains methods for generating, publishing, and receiving transactions, filling blocks with transactions, updating the mempool, and getting the mempool size and waiting transaction count. However, these methods are not implemented in this base class.

#### `generate(self, node: Miner) -> Transaction`
This method generates a transaction. It takes a `Miner` object as input and returns a `Transaction` object. The transaction size, fee, and value are generated using Gaussian distributions with parameters based on historical Bitcoin data.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | `Transaction` |

#### `publish(self, node: Miner, tx: Transaction, direct: bool = False)`
This method is a placeholder for publishing a transaction. It does not have any functionality in this base class.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`tx: Transaction`<br>`direct: bool` | None |

#### `receive(self, node: Miner, tx: Transaction = None)`
This method is a placeholder for receiving a transaction. It does not have any functionality in this base class.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`tx: Transaction` | None |

#### `fill_block(self, node: Miner, block: Block) -> Block`
This method is a placeholder for filling a block with transactions. It does not have any functionality in this base class.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`block: Block` | `Block` |

#### `update_mempool(self, node: Miner, block: Block)`
This method is a placeholder for updating the mempool after a block has been mined. It does not have any functionality in this base class.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`block: Block` | None |

#### `get_mempool_size(self, node: Miner)`
This method is a placeholder for getting the size of the mempool. It returns 0 in this base class.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | int |

#### `get_waiting_tx_count(self, node: Miner)`
This method is a placeholder for getting the count of transactions waiting in the mempool. It returns 0 in this base class.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | int |

### NoneTxModel
This class inherits from `TxModel` and overrides some of its methods. It represents a model where no transactions are generated.

#### `generate(self, node: Miner) -> Transaction`
This method is a placeholder for generating a transaction. It does not have any functionality in this class.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | None |

#### `fill_block(self, node: Miner, block: Block) -> Block`
This method assigns a transaction count and total size to a block. The values are generated using Gaussian distributions with parameters based on historical Bitcoin data.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`block: Block` | `Block` |

### SimpleTxModel
This class inherits from `TxModel` and overrides some of its methods. It represents a simple model where transactions are generated and added to a shared mempool.

#### `generate(self, node: Miner) -> Transaction`
This method generates a transaction and adds it to the shared mempool. It returns the generated `Transaction` object.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | `Transaction` |

#### `fill_block(self, node: Miner, block: Block) -> Block`
This method adds transactions to a block from the shared mempool until it reaches its maximum size.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`block: Block` | `Block` |

#### `get_mempool_size(self, node: Miner)`
This method returns the total size of the transactions in the shared mempool.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | int |

#### `get_waiting_tx_count(self, node: Miner)`
This method returns the count of transactions waiting in the shared mempool.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | int |

### FullTxModel
This class inherits from `TxModel` and overrides some of its methods. It represents a full model where transactions are generated, published, received, added to a local mempool, and relayed to peers.

#### `generate(self, node: Miner) -> Transaction`
This method generates a transaction and directly sends it to all peers. It returns the generated `Transaction` object.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | `Transaction` |

#### `publish(self, node: Miner, tx: Transaction, direct: bool = False)`
This method sends a transaction either directly or with inv/getdata to all peers.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`tx: Transaction`<br>`direct: bool` | None |

#### `receive(self, node: Miner, tx: Transaction = None)`
This method receives a transaction, adds it to the local mempool, saves its receipt time, and relays it to peers.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`tx: Transaction` | None |

#### `fill_block(self, miner: Miner, block: Block) -> Block`
This method fills a block with transactions from the local mempool until it reaches its maximum size.

| Parameters | Returns |
| --- | --- |
| `miner: Miner`<br>`block: Block` | `Block` |

#### `update_mempool(self, node: Miner, block: Block)`
This method removes the transactions in a block from the local mempool.

| Parameters | Returns |
| --- | --- |
| `node: Miner`<br>`block: Block` | None |

#### `get_mempool_size(self, node: Miner)`
This method returns the total size of the transactions in the local mempool.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | int |

#### `get_waiting_tx_count(self, node: Miner)`
This method returns the count of transactions waiting in the local mempool.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | int |

## Example usage
```python
# Create a miner
miner = Miner()

# Create a transaction model
tx_model = FullTxModel()

# Generate a transaction
tx = tx_model.generate(miner)

# Publish the transaction
tx_model.publish(miner, tx, direct=True)

# Receive the transaction
tx_model.receive(miner, tx)

# Create a block
block = Block()

# Fill the block with transactions
block = tx_model.fill_block(miner, block)

# Update the mempool
tx_model.update_mempool(miner, block)

# Get the mempool size
mempool_size = tx_model.get_mempool_size(miner)

# Get the waiting transaction count
waiting_tx_count = tx_model.get_waiting_tx_count(miner)
```