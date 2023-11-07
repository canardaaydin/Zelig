# analysis.py

## Explanation
This module contains various helper methods to extract statistics from the nodes dumped after a simulation run. It provides functionalities such as getting all blocks, computing the longest chain, calculating block propagation delays, calculating stale block rate, reward distribution, transactions per second, and average block interval.

## Dependencies
- `typing` for type hinting
- `math` for mathematical operations
- `sys` for appending paths
- `bitcoin.models` for Miner, Block models
- `bitcoin.bookkeeper` for Bookkeeper model

## Classes
### Analysis
This class contains various methods to analyze the data from a simulation run.

#### `__init__(self, bookkeeper: Bookkeeper, nodes: List[Node]) -> None`
This method initializes the Analysis class with a bookkeeper and a list of nodes.

| Parameters | Returns |
| --- | --- |
| `bookkeeper: Bookkeeper` | `None` |
| `nodes: List[Node]` | |

#### `get_all_blocks(self) -> Dict[str, Block]`
This method returns a list of all blocks seen by all the nodes.

| Parameters | Returns |
| --- | --- |
| | `blocks: Dict[str, Block]` |

#### `get_longest_chain(self, blocks: Dict[str, Block]) -> List[Block]`
This method computes and returns the list of blocks in the longest chain.

| Parameters | Returns |
| --- | --- |
| `blocks: Dict[str, Block]` | `chain: List[Block]` |

#### `block_prop_delays(self, block: Block) -> List[int]`
This method computes how much time it took for a block to reach each node.

| Parameters | Returns |
| --- | --- |
| `block: Block` | `List[int]` |

#### `block_percentile_delay(self, block: Block, percent: float) -> int`
This method calculates the time it takes for a block to reach a given percent of the nodes.

| Parameters | Returns |
| --- | --- |
| `block: Block` | `int` |
| `percent: float` | |

#### `stale_block_rate(self, node: Miner) -> float`
This method returns the share of orphan blocks from a node's point of view.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | `float` |

#### `reward_distribution(self) -> Dict[Miner, int]`
This method returns the total mining rewards collected for each miner as a dictionary with miner names as keys.

| Parameters | Returns |
| --- | --- |
| | `Dict[Miner, int]` |

#### `transactions_per_second(self, blocks: List[Block], sim_seconds: int) -> float`
This method calculates the rate of transactions per second given the list of all blocks and simulation time in seconds.

| Parameters | Returns |
| --- | --- |
| `blocks: List[Block]` | `float` |
| `sim_seconds: int` | |

#### `avg_block_interval(self, node: Miner) -> float`
This method computes the average block interval for blocks in the main chain from a given node's point of view.

| Parameters | Returns |
| --- | --- |
| `node: Miner` | `float` |

## Example usage
```python
from bitcoin.models import Miner, Block
from bitcoin.bookkeeper import Bookkeeper
from analysis import Analysis

# Initialize a bookkeeper and a list of nodes
bookkeeper = Bookkeeper()
nodes = [Miner("Miner1"), Miner("Miner2")]

# Initialize the Analysis class
analysis = Analysis(bookkeeper, nodes)

# Get all blocks
all_blocks = analysis.get_all_blocks()

# Get the longest chain
longest_chain = analysis.get_longest_chain(all_blocks)

# Compute block propagation delays
block = Block("Block1")
prop_delays = analysis.block_prop_delays(block)

# Compute block percentile delay
percentile_delay = analysis.block_percentile_delay(block, 0.5)

# Compute stale block rate
stale_rate = analysis.stale_block_rate(nodes[0])

# Get reward distribution
reward_dist = analysis.reward_distribution()

# Compute transactions per second
tps = analysis.transactions_per_second(all_blocks, 1000)

# Compute average block interval
avg_interval = analysis.avg_block_interval(nodes[0])
```