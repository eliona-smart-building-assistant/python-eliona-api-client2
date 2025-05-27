# ProjectUser

A project user

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_name** | **str** | The unique identifier for the user, represented as an email address. | 
**role_name** | **str** | The role assigned to the user within the project (e.g., readonly, admin, contributor). | 
**enabled** | **bool** | Whether the user for this project is currently active (true) or disabled (false). | [optional] 

## Example

```python
from eliona.api_client2.models.project_user import ProjectUser

# TODO update the JSON string below
json = "{}"
# create an instance of ProjectUser from a JSON string
project_user_instance = ProjectUser.from_json(json)
# print the JSON string representation of the object
print(ProjectUser.to_json())

# convert the object into a dict
project_user_dict = project_user_instance.to_dict()
# create an instance of ProjectUser from a dict
project_user_from_dict = ProjectUser.from_dict(project_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


