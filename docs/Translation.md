# Translation

Readable text to display in frontend

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**de** | **str** | German text | [optional] 
**en** | **str** | English text | [optional] 
**fr** | **str** | French text | [optional] 
**it** | **str** | Italian text | [optional] 

## Example

```python
from eliona.api_client2.models.translation import Translation

# TODO update the JSON string below
json = "{}"
# create an instance of Translation from a JSON string
translation_instance = Translation.from_json(json)
# print the JSON string representation of the object
print(Translation.to_json())

# convert the object into a dict
translation_dict = translation_instance.to_dict()
# create an instance of Translation from a dict
translation_from_dict = Translation.from_dict(translation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


