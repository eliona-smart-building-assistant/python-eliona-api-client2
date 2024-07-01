# App

An app

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the app | 
**active** | **bool** | Is the app active or inactive | [optional] 
**registered** | **bool** | Is the app already registered or not | [optional] 
**metadata** | **object** | Delivers the apps metadata to handle it in the app store | [optional] 
**version** | **str** | the apps version | [optional] 

## Example

```python
from eliona.api_client2.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


