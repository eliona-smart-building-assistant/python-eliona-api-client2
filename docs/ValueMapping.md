# ValueMapping

Mapping between value and custom text

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** | Value that should be mapped | [optional] 
**text** | **str** | Custom text to display instead of value | [optional] 

## Example

```python
from eliona.api_client2.models.value_mapping import ValueMapping

# TODO update the JSON string below
json = "{}"
# create an instance of ValueMapping from a JSON string
value_mapping_instance = ValueMapping.from_json(json)
# print the JSON string representation of the object
print ValueMapping.to_json()

# convert the object into a dict
value_mapping_dict = value_mapping_instance.to_dict()
# create an instance of ValueMapping from a dict
value_mapping_form_dict = value_mapping.from_dict(value_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


