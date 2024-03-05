# AssetType

A type of assets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The unique name for this asset type | 
**custom** | **bool** | Is this a customer created type or not | [optional] [default to True]
**vendor** | **str** | The vendor providing assets of this type | [optional] 
**model** | **str** | The specific model of assets of this type | [optional] 
**translation** | [**Translation**](Translation.md) |  | [optional] 
**urldoc** | **str** | The url describing assets of this type | [optional] 
**icon** | **str** | Icon name corresponding to assets of this type: blind, building, button, closable, elevator, environment, fallback, filling, gateway, light, mailbox, parking, people, power, rack, storey, trash, ventilation, vibration, water, weather | [optional] 
**payload_function** | **str** | Asset types payload function | [optional] 
**allowed_inactivity** | **str** |  | [optional] 
**attributes** | [**List[AssetTypeAttribute]**](AssetTypeAttribute.md) | List of named attributes | [optional] 

## Example

```python
from eliona.api_client2.models.asset_type import AssetType

# TODO update the JSON string below
json = "{}"
# create an instance of AssetType from a JSON string
asset_type_instance = AssetType.from_json(json)
# print the JSON string representation of the object
print AssetType.to_json()

# convert the object into a dict
asset_type_dict = asset_type_instance.to_dict()
# create an instance of AssetType from a dict
asset_type_form_dict = asset_type.from_dict(asset_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


