# DataListen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**timestamp** | **datetime** | Timestamp of the latest data change | [optional] 
**data** | **object** | Asset payload | 
**asset_type_name** | **str** | The name of the corresponding asset type | [optional] [readonly] 
**client_reference** | **str** | freely assignable by the client to identify self-created data | [optional] 
**status_code** | **int** | The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable  | [optional] 

## Example

```python
from eliona.api_client2.models.data_listen import DataListen

# TODO update the JSON string below
json = "{}"
# create an instance of DataListen from a JSON string
data_listen_instance = DataListen.from_json(json)
# print the JSON string representation of the object
print(DataListen.to_json())

# convert the object into a dict
data_listen_dict = data_listen_instance.to_dict()
# create an instance of DataListen from a dict
data_listen_from_dict = DataListen.from_dict(data_listen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


