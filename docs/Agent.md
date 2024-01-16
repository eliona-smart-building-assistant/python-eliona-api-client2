# Agent

An agent installed on an edge node

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Unique id for the agent | [optional] [readonly] 
**node_id** | **str** | Id of the node where the agent is installed | [optional] 
**asset_id** | **int** | ID of the corresponding asset | [optional] 
**var_class** | [**AgentClass**](AgentClass.md) |  | [optional] 
**description** | **str** | Descriptive text for the agent | [optional] 
**enable** | **bool** | Is the agent enabled or not | [optional] [default to False]
**config** | **object** | Individual configuration depending on agent class | [optional] 

## Example

```python
from eliona.api_client2.models.agent import Agent

# TODO update the JSON string below
json = "{}"
# create an instance of Agent from a JSON string
agent_instance = Agent.from_json(json)
# print the JSON string representation of the object
print Agent.to_json()

# convert the object into a dict
agent_dict = agent_instance.to_dict()
# create an instance of Agent from a dict
agent_form_dict = agent.from_dict(agent_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


