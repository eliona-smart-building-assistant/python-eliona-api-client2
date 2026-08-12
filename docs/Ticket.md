# Ticket

A ticket and task record

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ticket_id** | **int** | The id of the ticket | [optional] [readonly] 
**parent_id** | **int** | The id of the parent ticket | [optional] 
**title** | **str** | Title of the ticket | [optional] 
**description** | **str** | Description of the ticket | [optional] 
**priority** | **int** | Priority of the ticket | [optional] 
**reason** | **str** | Reason or type of the ticket | [optional] 
**state** | **str** | Current state of the ticket | [optional] 
**contact** | **object** | Contact information as JSON object | [optional] 
**tags** | **List[str]** | List of associated tags | [optional] 
**created_by** | **str** | User who created the ticket | [optional] 
**created_at** | **datetime** | Timestamp when the ticket was created | [optional] 
**assigned_to** | **str** | User the ticket is assigned to | [optional] 
**assigned_at** | **datetime** | Timestamp when the ticket was assigned | [optional] 
**closed_at** | **datetime** | Timestamp when the ticket was closed | [optional] 
**project_id** | **str** | ID of the project to which the ticket belongs | [optional] 
**asset_id** | **int** | ID of the associated asset | [optional] 
**alarm_id** | **int** | ID of the associated alarm | [optional] 
**alarm** | **object** | Alarm data snapshot as JSON object | [optional] 
**start_at** | **datetime** | Scheduled start time | [optional] 
**end_at** | **datetime** | Scheduled end time | [optional] 
**time_spent** | **str** | Time spent on the ticket | [optional] 
**reference** | **str** | External reference | [optional] 
**modified_by** | **str** | User who last modified the ticket | [optional] 
**modified_at** | **datetime** | Timestamp of last modification | [optional] 

## Example

```python
from eliona.api_client2.models.ticket import Ticket

# TODO update the JSON string below
json = "{}"
# create an instance of Ticket from a JSON string
ticket_instance = Ticket.from_json(json)
# print the JSON string representation of the object
print(Ticket.to_json())

# convert the object into a dict
ticket_dict = ticket_instance.to_dict()
# create an instance of Ticket from a dict
ticket_from_dict = Ticket.from_dict(ticket_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


