# Dashboard

A frontend dashboard

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The internal Id of dashboard | [optional] [readonly] 
**name** | **str** | The name for this dashboard | 
**project_id** | **str** | ID of the project to which the dashboard belongs | 
**user_id** | **str** | ID of the user who owns the dashboard | 
**sequence** | **int** | The sequence of the dashboard | [optional] [default to 0]
**widgets** | [**List[Widget]**](Widget.md) | List of widgets on this dashboard (order matches the order of widgets on the dashboard) | [optional] 

## Example

```python
from eliona.api_client2.models.dashboard import Dashboard

# TODO update the JSON string below
json = "{}"
# create an instance of Dashboard from a JSON string
dashboard_instance = Dashboard.from_json(json)
# print the JSON string representation of the object
print Dashboard.to_json()

# convert the object into a dict
dashboard_dict = dashboard_instance.to_dict()
# create an instance of Dashboard from a dict
dashboard_form_dict = dashboard.from_dict(dashboard_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


