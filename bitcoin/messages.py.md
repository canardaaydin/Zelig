# messages.py

## Explanation
This module contains the various message types that can be sent over the Bitcoin network. It includes two classes, `InvMessage` and `GetDataMessage`, which represent INV messages used to announce new blocks and GET_DATA messages used to request blocks after receiving INV messages, respectively.

## Dependencies
- `sys`: This module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.
- `sim.base_models`: This module contains base models for the simulation.

## Classes

### InvMessage
This class represents INV messages used to announce new blocks.

#### `__init__`
This method is used to create an `InvMessage` object.
| Parameters | Returns |
| --- | --- |
| `item_id` (str): Id of the block/transaction being announced. | None |
| `sender_id` (str): Id of the sender node. Can be used as a return address. |  |
| `type` (str): Type of the item. |  |

### GetDataMessage
This class represents GET_DATA messages used to request blocks after receiving INV messages.

#### `__init__`
This method is used to create a `GetDataMessage` object.
| Parameters | Returns |
| --- | --- |
| `item_id` (str): Id of the block/transaction being requested. | None |
| `sender_id` (str): Id of the sender node. Can be used as a return address. |  |
| `type` (str): Type of the item. |  |

## Example usage
```python
# Create an InvMessage object
inv_message = InvMessage("block1", "block", "node1")

# Create a GetDataMessage object
get_data_message = GetDataMessage("block1", "block", "node1")
```