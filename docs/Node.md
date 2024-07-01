# Node

An edge node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id for the edge node | [optional] [readonly] 
**ident** | **str** | UUID to identify the edge node | [optional] [readonly] 
**password** | **str** | Password with which the node identifies itself | [optional] 
**asset_id** | **int** | ID of the corresponding asset | [optional] 
**vendor** | **str** | Vendor name | [optional] 
**model** | **str** | Model name | [optional] 
**description** | **str** | Descriptive text for the edge node | [optional] 
**enable** | **bool** | Is the node enabled or not | [optional] [default to False]

## Example

```python
from eliona.api_client2.models.node import Node

# TODO update the JSON string below
json = "{}"
# create an instance of Node from a JSON string
node_instance = Node.from_json(json)
# print the JSON string representation of the object
print(Node.to_json())

# convert the object into a dict
node_dict = node_instance.to_dict()
# create an instance of Node from a dict
node_from_dict = Node.from_dict(node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


