# AgentDeviceMappingGeneral

A general mapping of attributes for an agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int** | Unique id for the mapping | [optional] [readonly] 
**device_id** | **int** | The id of the device the mapping belongs to | [optional] [readonly] 
**enable** | **bool** | Is the mapping enabled or not | [optional] [default to True]
**asset_id** | **int** | ID of the corresponding asset | [optional] 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**attribute** | **str** | Name of the attribute to map | 

## Example

```python
from eliona.api_client2.models.agent_device_mapping_general import AgentDeviceMappingGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDeviceMappingGeneral from a JSON string
agent_device_mapping_general_instance = AgentDeviceMappingGeneral.from_json(json)
# print the JSON string representation of the object
print(AgentDeviceMappingGeneral.to_json())

# convert the object into a dict
agent_device_mapping_general_dict = agent_device_mapping_general_instance.to_dict()
# create an instance of AgentDeviceMappingGeneral from a dict
agent_device_mapping_general_from_dict = AgentDeviceMappingGeneral.from_dict(agent_device_mapping_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


