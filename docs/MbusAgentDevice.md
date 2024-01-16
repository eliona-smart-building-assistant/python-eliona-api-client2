# MbusAgentDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int** | Unique id for the device | [optional] [readonly] 
**agent_id** | **int** | The id of the agent the device belongs to | [optional] [readonly] 
**enable** | **bool** | Is the device enabled or not | [optional] [default to False]
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
from eliona.api_client2.models.mbus_agent_device import MbusAgentDevice

# TODO update the JSON string below
json = "{}"
# create an instance of MbusAgentDevice from a JSON string
mbus_agent_device_instance = MbusAgentDevice.from_json(json)
# print the JSON string representation of the object
print MbusAgentDevice.to_json()

# convert the object into a dict
mbus_agent_device_dict = mbus_agent_device_instance.to_dict()
# create an instance of MbusAgentDevice from a dict
mbus_agent_device_form_dict = mbus_agent_device.from_dict(mbus_agent_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


