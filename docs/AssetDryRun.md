# AssetDryRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier (textual or numeric) of resources | [optional] 
**status_code** | **int** | The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable  | [optional] 
**error_message** | **str** | The error message expecting when actually perform the operation.  | [optional] 
**identified_by** | [**AssetIdentifyBy**](AssetIdentifyBy.md) |  | [optional] 
**before** | [**Asset**](Asset.md) |  | [optional] 
**after** | [**Asset**](Asset.md) |  | [optional] 

## Example

```python
from eliona.api_client2.models.asset_dry_run import AssetDryRun

# TODO update the JSON string below
json = "{}"
# create an instance of AssetDryRun from a JSON string
asset_dry_run_instance = AssetDryRun.from_json(json)
# print the JSON string representation of the object
print AssetDryRun.to_json()

# convert the object into a dict
asset_dry_run_dict = asset_dry_run_instance.to_dict()
# create an instance of AssetDryRun from a dict
asset_dry_run_form_dict = asset_dry_run.from_dict(asset_dry_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


