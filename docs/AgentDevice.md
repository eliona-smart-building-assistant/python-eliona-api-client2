# AgentDevice


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
**manufacturer** | **str** |  | [optional] 
**model** | **str** |  | [optional] 
**address** | **int** |  | [optional] 
**sec_address** | **str** |  | [optional] 
**raster** | **str** |  | [optional] 
**max_fail** | **int** |  | [optional] [default to 4]
**max_retry** | **int** |  | [optional] [default to 3]
**send_nke** | **bool** |  | [optional] [default to False]
**app_reset_subcode** | **int** |  | [optional] 
**multi_frames** | **int** |  | [optional] [default to 0]

## Example

```python
from eliona.api_client2.models.agent_device import AgentDevice

# TODO update the JSON string below
json = "{}"
# create an instance of AgentDevice from a JSON string
agent_device_instance = AgentDevice.from_json(json)
# print the JSON string representation of the object
print AgentDevice.to_json()

# convert the object into a dict
agent_device_dict = agent_device_instance.to_dict()
# create an instance of AgentDevice from a dict
agent_device_form_dict = agent_device.from_dict(agent_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


