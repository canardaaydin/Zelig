# util.py

## Explanation
The `util.py` module contains various utility classes and methods that are used throughout the application. It includes a class for defining regions and a function for generating unique identifiers.

## Dependencies
- `uuid`: This module is used to generate unique identifiers.
- `math`: This module provides mathematical functions.
- `enum`: This module is used for creating enumeration classes.

## Classes

### Region
This class is an enumeration of the supported regions. The regions include 'US', 'RU', 'KZ', 'ML', 'CN', 'GE', 'NR', 'VN', and 'CH'.

## Functions

### generate_uuid
This function generates a unique identifier that can be used as an id for `sim.base_models.Node` and `sim.base_models.Item`.

| Parameters | Returns |
| --- | --- |
| None | `str`: A unique identifier |

## Example usage

```python
from util import Region, generate_uuid

# Create a new unique identifier
new_id = generate_uuid()
print(new_id)  # Prints a unique identifier

# Check if a region is supported
if 'US' in Region:
    print('Region is supported')
else:
    print('Region is not supported')
```