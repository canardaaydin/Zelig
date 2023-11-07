# base_models.py

## Explanation
This Python script contains the core classes and functions that make up a blockchain simulator. It includes classes for items that can be transmitted over a network (e.g., blocks, messages), blocks to be stored on the blockchain, packets for transmitting items over the network, and nodes representing participants in the blockchain system. 

## Dependencies
- `math`
- `enum`
- `loguru`
- `typing` (List, Dict)
- `sim` (util)
- `sim.network_util` (get_delay, Region)

## Classes

### Item
Represents objects that can be transmitted over a network (e.g., blocks, messages).

#### `__init__(self, sender_id:str, size:float)`
Creates an Item object.
- Parameters: `sender_id` (str), `size` (float)
- Returns: None

### Block
Represents a block to be stored on the blockchain. Inherits from `Item`.

#### `__init__(self, creator, prev_id:str, height:int)`
Creates a Block object.
- Parameters: `creator` (Node), `prev_id` (str), `height` (int)
- Returns: None

#### `add_tx(self, tx)`
Adds a transaction to the block.
- Parameters: `tx` (Transaction)
- Returns: None

#### `has_tx(self, tx)`
Checks if a transaction is in the block.
- Parameters: `tx` (Transaction)
- Returns: Boolean

### Packet
Wrapper class for transmitting `Item` objects over the network.

#### `__init__(self, payload:Item)`
Creates a Packet object.
- Parameters: `payload` (Item)
- Returns: None

### Node
Represents the participants in the blockchain system.

#### `__init__(self, iter_seconds, name, region, timestamp=0)`
Creates a Node object.
- Parameters: `iter_seconds` (int), `name` (str), `region` (Region), `timestamp` (int, optional)
- Returns: None

#### `step(self, seconds:float)`
Performs one simulation step.
- Parameters: `seconds` (float)
- Returns: List of `Item` objects

#### `reset(self)`
Resets node state back to simulation start.
- Parameters: None
- Returns: None

#### `send_to(self, node, item:Item)`
Sends an item to a specific node.
- Parameters: `node` (Node), `item` (Item)
- Returns: None

#### `connect(self, *argv)`
Establishes an outgoing connection to one or more nodes.
- Parameters: `*argv` (Node)
- Returns: None

#### `print_blockchain(self, head:Block=None)`
Prints the blockchain.
- Parameters: `head` (Block, optional)
- Returns: None

### Reward
Represents the reward for mining a block.

#### `__init__(self, node:Node, value:int)`
Creates a Reward object.
- Parameters: `node` (Node), `value` (int)
- Returns: None

## Example usage
```python
# Create a node
node1 = Node(iter_seconds=1, name="Node1", region=Region.US_EAST)

# Create another node
node2 = Node(iter_seconds=1, name="Node2", region=Region.US_WEST)

# Connect the nodes
node1.connect(node2)

# Create an item
item = Item(sender_id="Node1", size=10)

# Node1 sends the item to Node2
node1.send_to(node2, item)

# Node2 performs a simulation step
node2.step(seconds=1)
```