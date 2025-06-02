# AssetTypeCategory

A category for asset types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this asset type category | 
**translation** | [**Translation**](Translation.md) |  | [optional] 
**properties** | [**List[AssetTypeCategoryProperty]**](AssetTypeCategoryProperty.md) | List of asset type category properties | [optional] 

## Example

```python
from eliona.api_client2.models.asset_type_category import AssetTypeCategory

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeCategory from a JSON string
asset_type_category_instance = AssetTypeCategory.from_json(json)
# print the JSON string representation of the object
print(AssetTypeCategory.to_json())

# convert the object into a dict
asset_type_category_dict = asset_type_category_instance.to_dict()
# create an instance of AssetTypeCategory from a dict
asset_type_category_from_dict = AssetTypeCategory.from_dict(asset_type_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


