# AgentDeviceGeneral

A general device for an agent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int** | Unique id for the device | [optional] [readonly] 
**agent_id** | **int** | The id of the agent the device belongs to | [optional] [readonly] 
**enable** | **bool** | Is the device enabled or not | [optional] [default to False]

## Example

```python
from eliona.api_client2.models.agent_device_general import AgentDeviceGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDeviceGeneral from a JSON string
agent_device_general_instance = AgentDeviceGeneral.from_json(json)
# print the JSON string representation of the object
print AgentDeviceGeneral.to_json()

# convert the object into a dict
agent_device_general_dict = agent_device_general_instance.to_dict()
# create an instance of AgentDeviceGeneral from a dict
agent_device_general_form_dict = agent_device_general.from_dict(agent_device_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


