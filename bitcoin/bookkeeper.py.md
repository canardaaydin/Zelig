# bookkeeper.py

## Explanation
The `bookkeeper.py` script is a part of a simulation system. It is responsible for keeping track of various metrics related to nodes in a network. These metrics include transaction receipt times, block receipt times, computational power usage, and storage space usage.

## Dependencies
- `sys` - Standard Python library for system-specific parameters and functions.
- `typing` - Standard Python library for support of type hints.
- `sim.base_models` - Custom module containing base models for the simulation.

## Classes

### Bookkeeper
The `Bookkeeper` class is responsible for tracking and managing various metrics related to nodes in a network.

#### `__init__`
This method initializes a new instance of the `Bookkeeper` class. It sets up several dictionaries and lists to store metrics related to nodes.

| Parameters | Returns |
| --- | --- |
| None | None |

#### `register_node`
This method performs initial setup for a node. It associates the node with the bookkeeper and initializes metrics for the node.

| Parameters | Returns |
| --- | --- |
| `node: Node` | None |

#### `save_block`
This method saves the receipt time of a given block for a given node.

| Parameters | Returns |
| --- | --- |
| `node: Node`, `block: Item`, `timestamp: int` | None |

#### `save_tx`
This method saves the receipt time of a given transaction for a given node.

| Parameters | Returns |
| --- | --- |
| `node: Node`, `tx: Item`, `timestamp: int` | None |

#### `get_node_block_rcv`
This method gets the receipt time of a given block for a given node.

| Parameters | Returns |
| --- | --- |
| `node: Node`, `block: Item` | `int` |

#### `use_compute`
This method records the computational power usage (simulated) by a node.

| Parameters | Returns |
| --- | --- |
| `node: Node`, `amount: int` | None |

#### `use_space`
This method records the storage space (simulated) usage by a node.

| Parameters | Returns |
| --- | --- |
| `node: Node`, `amount: int` | None |

## Example usage
```python
from sim.base_models import Node, Item
from bookkeeper import Bookkeeper

# Initialize a bookkeeper
bk = Bookkeeper()

# Initialize a node and register it with the bookkeeper
node = Node()
bk.register_node(node)

# Simulate a block receipt
block = Item()
bk.save_block(node, block, 123456)

# Simulate a transaction receipt
tx = Item()
bk.save_tx(node, tx, 123456)

# Get block receipt time
print(bk.get_node_block_rcv(node, block))  # Output: 123456

# Record computational power usage
bk.use_compute(node, 100)

# Record storage space usage
bk.use_space(node, 200)
```