# models.py

## Explanation
This Python script is the main implementation of a Bitcoin simulator. It contains classes for transactions, blocks, and miners, and methods for their interactions. The script simulates the creation and propagation of transactions and blocks in the Bitcoin network, and the consensus mechanism among miners.

## Dependencies
- `sys`
- `typing.Dict`
- `loguru.logger`
- `sim.base_models`
- `bitcoin.messages.InvMessage, GetDataMessage`
- `bitcoin.consensus`
- `bitcoin.bookkeeper`

## Classes

### Transaction
This class represents a Bitcoin transaction. It inherits from the `Item` class.

#### `__init__(self, sender_id:str, created_at:int, size:float, value:float, fee:float)`
This method initializes a `Transaction` object. It takes the sender's ID, the creation time, the size of the transaction, the value of the transaction, and the transaction fee as parameters.

| Parameters | Returns |
| --- | --- |
| `sender_id: str` | None |
| `created_at: int` | None |
| `size: float` | None |
| `value: float` | None |
| `fee: float` | None |

### BTCBlock
This class represents a Bitcoin block. It inherits from the `Block` class.

#### `__init__(self, creator, prev_id:str, height:int)`
This method initializes a `BTCBlock` object. It takes the creator of the block, the ID of the previous block, and the height of the block as parameters.

| Parameters | Returns |
| --- | --- |
| `creator` | None |
| `prev_id: str` | None |
| `height: int` | None |

### Miner
This class represents a Bitcoin miner. It inherits from the `Node` class.

#### `__init__(self, name:str, mine_power:float, region:Region, iter_seconds, timestamp=0)`
This method initializes a `Miner` object. It takes the miner's name, mining power, region, iteration seconds, and timestamp as parameters.

| Parameters | Returns |
| --- | --- |
| `name: str` | None |
| `mine_power: float` | None |
| `region: Region` | None |
| `iter_seconds` | None |
| `timestamp: int` | None |

## Functions

### `step(self, seconds:float)`
This method simulates a step in the Bitcoin network. It takes the number of seconds to simulate as a parameter.

| Parameters | Returns |
| --- | --- |
| `seconds: float` | `items` |

### `consume(self, item:Item)`
This method consumes an item in the Bitcoin network. It takes the item to consume as a parameter.

| Parameters | Returns |
| --- | --- |
| `item: Item` | None |

### `publish_item(self, item:Item, item_type:str)`
This method publishes an item over all of the node's outgoing connections. It takes the item to publish and the item's type as parameters.

| Parameters | Returns |
| --- | --- |
| `item: Item` | None |
| `item_type: str` | None |

## Example usage
```python
# Create a miner
miner = Miner("Miner1", 0.1, Region.US, 1)

# Create a transaction
transaction = Transaction("Sender1", 0, 400, 100, 0.01)

# Miner consumes the transaction
miner.consume(transaction)

# Miner takes a step in the network
miner.step(1)

# Miner publishes the transaction
miner.publish_item(transaction, "transaction")
```