# AlarmListen


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rule_id** | **int** | The id of the corresponding rule | [optional] 
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | 
**attribute** | **str** | Name of the attribute of the asset type | [optional] 
**priority** | [**AlarmPriority**](AlarmPriority.md) |  | 
**requires_acknowledge** | **bool** | Requires the alarm an acknowledgment | [optional] [default to False]
**value** | **float** | The value which triggers the alarm | [optional] 
**timestamp** | **datetime** | Timestamp of the latest data change | 
**gone_timestamp** | **datetime** | Timestamp of the latest data change | [optional] 
**acknowledge_timestamp** | **datetime** | Timestamp of the latest data change | [optional] 
**occurrences** | **int** | How often this alarm is triggered | 
**acknowledge_text** | **str** | Text of acknowledgement | [optional] 
**acknowledge_user_id** | **str** | User who acknowledged the alarm | [optional] 
**message** | **object** | Message.yaml texts for alarm | [optional] 
**asset_info** | [**Asset**](Asset.md) |  | [optional] 
**rule_info** | [**AlarmRule**](AlarmRule.md) |  | [optional] 
**status_code** | **int** | The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable  | [optional] 

## Example

```python
from eliona.api_client2.models.alarm_listen import AlarmListen

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmListen from a JSON string
alarm_listen_instance = AlarmListen.from_json(json)
# print the JSON string representation of the object
print AlarmListen.to_json()

# convert the object into a dict
alarm_listen_dict = alarm_listen_instance.to_dict()
# create an instance of AlarmListen from a dict
alarm_listen_form_dict = alarm_listen.from_dict(alarm_listen_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


