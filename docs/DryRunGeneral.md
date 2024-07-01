# DryRunGeneral

Information about dry run the operation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identifier** | **str** | Unique identifier (textual or numeric) of resources | [optional] 
**status_code** | **int** | The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable  | [optional] 
**error_message** | **str** | The error message expecting when actually perform the operation.  | [optional] 

## Example

```python
from eliona.api_client2.models.dry_run_general import DryRunGeneral

# TODO update the JSON string below
json = "{}"
# create an instance of DryRunGeneral from a JSON string
dry_run_general_instance = DryRunGeneral.from_json(json)
# print the JSON string representation of the object
print(DryRunGeneral.to_json())

# convert the object into a dict
dry_run_general_dict = dry_run_general_instance.to_dict()
# create an instance of DryRunGeneral from a dict
dry_run_general_from_dict = DryRunGeneral.from_dict(dry_run_general_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


