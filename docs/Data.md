# Data

Data for assets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**timestamp** | **datetime** | Timestamp of the latest data change | [optional] 
**data** | **object** | Asset payload | 
**asset_type_name** | **str** | The name of the corresponding asset type | [optional] [readonly] 
**client_reference** | **str** | freely assignable by the client to identify self-created data | [optional] 

## Example

```python
from eliona.api_client2.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print(Data.to_json())

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_from_dict = Data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


