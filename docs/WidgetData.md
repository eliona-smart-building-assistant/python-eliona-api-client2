# WidgetData

Data for a widget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal Id of widget data | [optional] [readonly] 
**element_sequence** | **int** | Position of the element in widget type | [optional] 
**asset_id** | **int** | The master asset id of this widget | [optional] 
**data** | **object** | individual config parameters depending on category | [optional] 

## Example

```python
from eliona.api_client2.models.widget_data import WidgetData

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetData from a JSON string
widget_data_instance = WidgetData.from_json(json)
# print the JSON string representation of the object
print WidgetData.to_json()

# convert the object into a dict
widget_data_dict = widget_data_instance.to_dict()
# create an instance of WidgetData from a dict
widget_data_form_dict = widget_data.from_dict(widget_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


