# Message

A message

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sender** | **str** | Address of the sender, e.g. an e-mail address | [optional] 
**recipients** | **List[str]** | A list of recipient addresses to receive this message | 
**copy_recipients** | **List[str]** | A list of recipient addresses to receive this message as copy | [optional] 
**blind_copy_recipients** | **List[str]** | A list of recipient addresses to receive this message as blind copy without any other recipient information | [optional] 
**subject** | **str** | The subject for this message | [optional] 
**content** | **str** | The content of the message. If template is used, the content is embedded in the template. | 
**attachments** | [**List[Attachment]**](Attachment.md) | A list of files attached to the message | [optional] 

## Example

```python
from eliona.api_client2.models.message import Message

# TODO update the JSON string below
json = "{}"
# create an instance of Message from a JSON string
message_instance = Message.from_json(json)
# print the JSON string representation of the object
print(Message.to_json())

# convert the object into a dict
message_dict = message_instance.to_dict()
# create an instance of Message from a dict
message_from_dict = Message.from_dict(message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


