# Asset

An asset

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resource_id** | **str** | A custom identifier for the resource, which can be utilized to identify it for various operations such as updates, deletions, and other related tasks. If this identifier is not provided, the application will generate a new value for it automatically | [optional] 
**id** | **int** | The internal Id of asset | [optional] [readonly] 
**device_ids** | **List[str]** | A list of unique device ids | [optional] 
**project_id** | **str** | ID of the project to which the asset belongs | 
**global_asset_identifier** | **str** | Unique identifier for the asset | 
**name** | **str** | Alternate text for the asset to display in frontend | [optional] 
**asset_type** | **str** | Reference to asset type by name | 
**latitude** | **float** | Latitude coordinate (GPS) of the asset | [optional] 
**longitude** | **float** | Longitude coordinate (GPS) of the asset | [optional] 
**is_tracker** | **bool** | Does the asset function as a tracker and capture its position by itself | [optional] [default to False]
**tracker_id** | **int** | Tracker Asset Id | [optional] 
**description** | **str** | Textual description for this asset | [optional] 
**parent_functional_asset_id** | **int** | The id of an asset which groups this asset as a functional child | [optional] 
**functional_asset_id_path** | **List[int]** | The hierarchical path of functional ids of the asset | [optional] [readonly] 
**parent_locational_asset_id** | **int** | The id of an asset which groups this asset as a locational child | [optional] 
**locational_asset_id_path** | **List[int]** | The hierarchical path of locational ids of the asset | [optional] [readonly] 
**parent_functional_identifier** | **str** | The identifier specified by the identifiedBy parameter classifies this asset as a functional child. | [optional] 
**parent_locational_identifier** | **str** | The identifier specified by the identifiedBy parameter classifies this asset as a locational child | [optional] 
**tags** | **List[str]** | List of associated tags | [optional] 
**allowed_inactivity** | **str** |  | [optional] 
**children_info** | [**List[Asset]**](Asset.md) | List of children for this asset. | [optional] [readonly] 
**attachments** | [**List[Attachment]**](Attachment.md) | A list of files attached to the asset | [optional] 

## Example

```python
from eliona.api_client2.models.asset import Asset

# TODO update the JSON string below
json = "{}"
# create an instance of Asset from a JSON string
asset_instance = Asset.from_json(json)
# print the JSON string representation of the object
print(Asset.to_json())

# convert the object into a dict
asset_dict = asset_instance.to_dict()
# create an instance of Asset from a dict
asset_from_dict = Asset.from_dict(asset_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


