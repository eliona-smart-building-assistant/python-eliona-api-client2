# Widget

A widget on a frontend dashboard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal Id of widget | [optional] [readonly] 
**widget_type_name** | **str** | The name for the type of this widget | 
**details** | **object** | Detailed configuration depending on the widget type | [optional] 
**asset_id** | **int** | The master asset id of this widget | [optional] 
**sequence** | **int** | Placement order on dashboard; if not set the index in array is taken | [optional] 
**data** | [**List[WidgetData]**](WidgetData.md) | List of data for the elements of widget | [optional] 

## Example

```python
from eliona.api_client2.models.widget import Widget

# TODO update the JSON string below
json = "{}"
# create an instance of Widget from a JSON string
widget_instance = Widget.from_json(json)
# print the JSON string representation of the object
print Widget.to_json()

# convert the object into a dict
widget_dict = widget_instance.to_dict()
# create an instance of Widget from a dict
widget_form_dict = widget.from_dict(widget_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


