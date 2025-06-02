# AssetTypeCategoryProperty

A property for asset type categories

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this asset type category property | 
**translation** | [**Translation**](Translation.md) |  | [optional] 
**unit** | **str** | Unit of data | [optional] 

## Example

```python
from eliona.api_client2.models.asset_type_category_property import AssetTypeCategoryProperty

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeCategoryProperty from a JSON string
asset_type_category_property_instance = AssetTypeCategoryProperty.from_json(json)
# print the JSON string representation of the object
print(AssetTypeCategoryProperty.to_json())

# convert the object into a dict
asset_type_category_property_dict = asset_type_category_property_instance.to_dict()
# create an instance of AssetTypeCategoryProperty from a dict
asset_type_category_property_from_dict = AssetTypeCategoryProperty.from_dict(asset_type_category_property_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


