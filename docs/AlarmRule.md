# AlarmRule

Rule for an alarm

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the rule | [optional] [readonly] 
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**attribute** | **str** | Name of the attribute of the asset type | 
**enable** | **bool** | Rule enabled or not | [optional] [default to True]
**priority** | [**AlarmPriority**](AlarmPriority.md) |  | 
**requires_acknowledge** | **bool** | Requires the alarm an acknowledgment | [optional] [default to False]
**equal** | **float** | Triggers alarm if attribute value equals this value | [optional] 
**low** | **float** | Triggers alarm if attribute value is less than value | [optional] 
**high** | **float** | Triggers alarm if attribute value is greater than value | [optional] 
**message** | **object** | Texts for alarm | [optional] 
**tags** | **List[str]** | List of associated tags | [optional] 
**subject** | **str** | The subject for the alarm | [optional] 
**urldoc** | **str** | The url describing the alarm | [optional] 
**params** | **object** | Parameter for aggregated alarms | [optional] 
**notify_on** | **str** | Notification | [optional] 
**dont_mask** | **bool** | Do not mask | [optional] [default to False]
**check_type** | **str** | Check type | [optional] 
**asset_info** | [**Asset**](Asset.md) |  | [optional] 

## Example

```python
from eliona.api_client2.models.alarm_rule import AlarmRule

# TODO update the JSON string below
json = "{}"
# create an instance of AlarmRule from a JSON string
alarm_rule_instance = AlarmRule.from_json(json)
# print the JSON string representation of the object
print(AlarmRule.to_json())

# convert the object into a dict
alarm_rule_dict = alarm_rule_instance.to_dict()
# create an instance of AlarmRule from a dict
alarm_rule_from_dict = AlarmRule.from_dict(alarm_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


