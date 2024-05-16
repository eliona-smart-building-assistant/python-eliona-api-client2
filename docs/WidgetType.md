# WidgetType

A frontend widget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal Id of widget type | [optional] [readonly] 
**name** | **str** | The unique name for this widget type | 
**custom** | **bool** | Is this a customer created type or not | [optional] [default to True]
**translation** | [**Translation**](Translation.md) |  | 
**icon** | **str** | Icon name corresponding to assets used in this widget | [optional] 
**with_alarm** | **bool** | Show alarms in widget | [optional] [default to False]
**with_timespan** | **bool** | Show selection for timespan in widget | [optional] [default to False]
**elements** | [**List[WidgetTypeElement]**](WidgetTypeElement.md) | A list of elements for this widget (order matches the order of elements for this type) | 

## Example

```python
from eliona.api_client2.models.widget_type import WidgetType

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetType from a JSON string
widget_type_instance = WidgetType.from_json(json)
# print the JSON string representation of the object
print(WidgetType.to_json())

# convert the object into a dict
widget_type_dict = widget_type_instance.to_dict()
# create an instance of WidgetType from a dict
widget_type_from_dict = WidgetType.from_dict(widget_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


