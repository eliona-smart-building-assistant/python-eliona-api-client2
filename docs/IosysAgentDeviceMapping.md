# IosysAgentDeviceMapping


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
**ios_var** | **str** |  | [optional] 
**ios_type** | **str** |  | [optional] 
**down** | **bool** |  | [optional] [default to False]
**scale** | **float** |  | [optional] 
**zero** | **float** |  | [optional] 
**mask** | **List[int]** |  | [optional] 
**mask_attributes** | **List[str]** |  | [optional] 
**dead_time** | **int** |  | [optional] 
**dead_band** | **float** |  | [optional] 
**filter** | **str** |  | [optional] 
**tau** | **float** |  | [optional] 

## Example

```python
from eliona.api_client2.models.iosys_agent_device_mapping import IosysAgentDeviceMapping

# TODO update the JSON string below
json = "{}"
# create an instance of IosysAgentDeviceMapping from a JSON string
iosys_agent_device_mapping_instance = IosysAgentDeviceMapping.from_json(json)
# print the JSON string representation of the object
print(IosysAgentDeviceMapping.to_json())

# convert the object into a dict
iosys_agent_device_mapping_dict = iosys_agent_device_mapping_instance.to_dict()
# create an instance of IosysAgentDeviceMapping from a dict
iosys_agent_device_mapping_from_dict = IosysAgentDeviceMapping.from_dict(iosys_agent_device_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


