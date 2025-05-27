# Project

A project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The internal ID of the project | [optional] [readonly] 
**title** | **str** | The title of the project | [optional] 
**users** | [**List[ProjectUser]**](ProjectUser.md) | List of users with a project role | [optional] 

## Example

```python
from eliona.api_client2.models.project import Project

# TODO update the JSON string below
json = "{}"
# create an instance of Project from a JSON string
project_instance = Project.from_json(json)
# print the JSON string representation of the object
print(Project.to_json())

# convert the object into a dict
project_dict = project_instance.to_dict()
# create an instance of Project from a dict
project_from_dict = Project.from_dict(project_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


