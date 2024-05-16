# IosysAgentDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int** | Unique id for the device | [optional] [readonly] 
**agent_id** | **int** | The id of the agent the device belongs to | [optional] [readonly] 
**enable** | **bool** | Is the device enabled or not | [optional] [default to False]
**port** | **int** | Port of device | [optional] 
**certificate** | **str** | Certificate of device | [optional] 
**key** | **str** | Key for device | [optional] 
**timeout** | **int** | Time in seconds | [optional] 
**reconnect** | **int** | Reconnect | [optional] 

## Example

```python
from eliona.api_client2.models.iosys_agent_device import IosysAgentDevice

# TODO update the JSON string below
json = "{}"
# create an instance of IosysAgentDevice from a JSON string
iosys_agent_device_instance = IosysAgentDevice.from_json(json)
# print the JSON string representation of the object
print(IosysAgentDevice.to_json())

# convert the object into a dict
iosys_agent_device_dict = iosys_agent_device_instance.to_dict()
# create an instance of IosysAgentDevice from a dict
iosys_agent_device_from_dict = IosysAgentDevice.from_dict(iosys_agent_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


