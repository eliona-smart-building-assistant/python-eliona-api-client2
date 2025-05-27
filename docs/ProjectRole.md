# ProjectRole

A role that can assigned to users within a project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal Id of role | [optional] [readonly] 
**name** | **str** | Display name of the role | 

## Example

```python
from eliona.api_client2.models.project_role import ProjectRole

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectRole from a JSON string
project_role_instance = ProjectRole.from_json(json)
# print the JSON string representation of the object
print(ProjectRole.to_json())

# convert the object into a dict
project_role_dict = project_role_instance.to_dict()
# create an instance of ProjectRole from a dict
project_role_from_dict = ProjectRole.from_dict(project_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


