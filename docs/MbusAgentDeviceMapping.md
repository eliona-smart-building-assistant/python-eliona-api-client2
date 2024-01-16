# MbusAgentDeviceMapping


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**id** | **int** | Unique id for the mapping | [optional] [readonly] 
**device_id** | **int** | The id of the device the mapping belongs to | [optional] [readonly] 
**enable** | **bool** | Is the mapping enabled or not | [optional] [default to True]
**asset_id** | **int** | ID of the corresponding asset | [optional] 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**attribute** | **str** | Name of the attribute to map | 
**field** | **int** |  | [optional] 
**scale** | **float** |  | [optional] 
**zero** | **float** |  | [optional] 

## Example

```python
from eliona.api_client2.models.mbus_agent_device_mapping import MbusAgentDeviceMapping

# TODO update the JSON string below
json = "{}"
# create an instance of MbusAgentDeviceMapping from a JSON string
mbus_agent_device_mapping_instance = MbusAgentDeviceMapping.from_json(json)
# print the JSON string representation of the object
print MbusAgentDeviceMapping.to_json()

# convert the object into a dict
mbus_agent_device_mapping_dict = mbus_agent_device_mapping_instance.to_dict()
# create an instance of MbusAgentDeviceMapping from a dict
mbus_agent_device_mapping_form_dict = mbus_agent_device_mapping.from_dict(mbus_agent_device_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


