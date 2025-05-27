# AttributeDisplay

How attributes are displayed for specific assets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**attribute** | **str** | Name of the attribute of the asset type | 
**unit** | **str** | Physical unit of numeric data | [optional] 
**precision** | **int** | Number of decimal places | [optional] 
**min** | **float** | Lower limit | [optional] 
**max** | **float** | Upper limit | [optional] 
**viewer** | **bool** | Should the attribute be displayed in viewer | [optional] [default to False]
**ar** | **bool** | Should the attribute be displayed in AR | [optional] [default to False]
**sequence** | **int** | Sequence in AR display | [optional] 
**map** | **List[object]** | list of mapping between value and custom text | [optional] 

## Example

```python
from eliona.api_client2.models.attribute_display import AttributeDisplay

# TODO update the JSON string below
json = "{}"
# create an instance of AttributeDisplay from a JSON string
attribute_display_instance = AttributeDisplay.from_json(json)
# print the JSON string representation of the object
print(AttributeDisplay.to_json())

# convert the object into a dict
attribute_display_dict = attribute_display_instance.to_dict()
# create an instance of AttributeDisplay from a dict
attribute_display_from_dict = AttributeDisplay.from_dict(attribute_display_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


