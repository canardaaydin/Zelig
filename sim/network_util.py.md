# network_util.py

## Explanation
This Python script contains helper functions to perform network-layer calculations. It calculates the delay of a message between two regions, the fixed latency value between two regions, and the bottleneck bandwidth between two regions. It uses data from `sim.util.Region` and predefined speed and latency data.

## Dependencies
- `sim.util.Region`: This is a dependency used to define the regions for the network calculations.

## Functions

### get_delay
This function calculates and returns the delay (in seconds) of a message between two regions. It uses the latency and speed between the two regions and the size of the message to calculate the delay.

| Parameters | Returns |
| --- | --- |
| `a` (`sim.util.Region`): Source region | `float`: Delay in seconds |
| `b` (`sim.util.Region`): Destination region | |
| `size` (`float`): Message size in bytes | |

### latency
This function returns the fixed latency value between two regions. It uses a predefined latency dictionary to get the latency value.

| Parameters | Returns |
| --- | --- |
| `a` (`sim.util.Region`): Source region | `float`: Latency value |
| `b` (`sim.util.Region`): Destination region | |

### speed
This function returns the bottleneck bandwidth between two regions. In other words, it returns the minimum of the source region's upload speed and the destination region's download speed. It uses a predefined speed dictionary to get the speed values.

| Parameters | Returns |
| --- | --- |
| `src` (`sim.util.Region`): Source region | `float`: Bottleneck bandwidth |
| `dest` (`sim.util.Region`): Destination region | |

## Example usage
```python
from sim.util import Region
from network_util import get_delay, latency, speed

# Define regions
region_a = Region.US
region_b = Region.CH

# Define message size
message_size = 1000.0  # in bytes

# Calculate delay
delay = get_delay(region_a, region_b, message_size)
print(f"Delay: {delay} seconds")

# Get latency
lat = latency(region_a, region_b)
print(f"Latency: {lat} seconds")

# Get speed
bw = speed(region_a, region_b)
print(f"Bottleneck bandwidth: {bw} MB/s")
```
This example calculates the delay of a 1000-byte message from the US to Switzerland, the latency between the two regions, and the bottleneck bandwidth between the two regions.