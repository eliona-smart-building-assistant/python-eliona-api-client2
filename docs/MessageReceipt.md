# MessageReceipt

A receipt for a message or notification

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifies the message or notification | [readonly] 
**scheduled_at** | **datetime** | When the message or notification is scheduled | [optional] 
**status** | **str** | Status of communication processing | [optional] 

## Example

```python
from eliona.api_client2.models.message_receipt import MessageReceipt

# TODO update the JSON string below
json = "{}"
# create an instance of MessageReceipt from a JSON string
message_receipt_instance = MessageReceipt.from_json(json)
# print the JSON string representation of the object
print(MessageReceipt.to_json())

# convert the object into a dict
message_receipt_dict = message_receipt_instance.to_dict()
# create an instance of MessageReceipt from a dict
message_receipt_from_dict = MessageReceipt.from_dict(message_receipt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


