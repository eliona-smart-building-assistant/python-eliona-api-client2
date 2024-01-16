# WidgetTypeElement

An element for widget types

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal Id of widget element | [optional] [readonly] 
**category** | **str** | The category for this element | 
**sequence** | **int** | sequence of element in widget; if not defined the index in array is taken | [optional] 
**config** | **object** | individual config parameters depending on category | [optional] 

## Example

```python
from eliona.api_client2.models.widget_type_element import WidgetTypeElement

# TODO update the JSON string below
json = "{}"
# create an instance of WidgetTypeElement from a JSON string
widget_type_element_instance = WidgetTypeElement.from_json(json)
# print the JSON string representation of the object
print WidgetTypeElement.to_json()

# convert the object into a dict
widget_type_element_dict = widget_type_element_instance.to_dict()
# create an instance of WidgetTypeElement from a dict
widget_type_element_form_dict = widget_type_element.from_dict(widget_type_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


