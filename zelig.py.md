# zelig.py

## Explanation
This script is a simulation of a blockchain network. It creates a network of nodes, each representing a miner in the blockchain network. The simulation runs for a specified number of iterations, with each node performing actions such as mining and transaction processing. The simulation can be configured through a YAML configuration file.

## Dependencies
- `importlib`
- `pickle`
- `argparse`
- `pathlib.Path`
- `typing.Callable`
- `psutil`
- `yaml`
- `time`
- `loguru.logger`
- `sim.base_models.Node`
- `sim.util.Region`
- `bitcoin.tx_modelings`
- `bitcoin.models.Miner`
- `bitcoin.mining_strategies`
- `bitcoin.consensus`
- `bitcoin.bookkeeper.Bookkeeper`

## Classes

### Simulation
This class represents the simulation of the blockchain network.

#### `__init__(self, config_file=None)`
This method initializes the simulation. It sets up the simulation parameters and loads the configuration file if provided.

Parameters:

| Parameters | Type |
| --- | --- |
| `config_file` | `str` |

#### `run(self, report_time=False, track_perf=False)`
This method runs the simulation. It sets up the network, runs the simulation for the specified number of iterations, and saves the state of each node after the simulation.

Parameters:

| Parameters | Type |
| --- | --- |
| `report_time` | `bool` |
| `track_perf` | `bool` |

#### `add_node(self, node:Node)`
This method adds a node to the simulation.

Parameters:

| Parameters | Type |
| --- | --- |
| `node` | `Node` |

#### `__setup_mining(self)`
This method sets up the mining process for the simulation. It adds a genesis block and sets up the consensus oracles for each node.

#### `__load_config_file(self, detailed=False)`
This method loads the configuration file for the simulation.

Parameters:

| Parameters | Type |
| --- | --- |
| `detailed` | `bool` |

#### `set_log_level(level:str)`
This method sets the log level for the simulation.

Parameters:

| Parameters | Type |
| --- | --- |
| `level` | `str` |

## Example usage
```python
# Create a simulation with a configuration file
sim = Simulation('config.yaml')

# Run the simulation
sim.run(report_time=True, track_perf=True)
```
This example creates a simulation using a configuration file named 'config.yaml'. It then runs the simulation, reporting the time taken and tracking performance.