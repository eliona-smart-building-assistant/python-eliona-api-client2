# eliona.api_client2.AgentsApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_agent_by_class_and_id**](AgentsApi.md#get_agent_by_class_and_id) | **GET** /agents/{agent-class}/{agent-id} | Information about an agent
[**get_agent_device_by_id**](AgentsApi.md#get_agent_device_by_id) | **GET** /agent-devices/{agent-class}/{agent-device-id} | Information about agent device
[**get_agent_device_mapping_by_id**](AgentsApi.md#get_agent_device_mapping_by_id) | **GET** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Information about agent device mapping
[**get_agent_device_mappings_by_device_id**](AgentsApi.md#get_agent_device_mappings_by_device_id) | **GET** /agent-devices/{agent-class}/{agent-device-id}/mappings | Information about agent device mappings
[**get_agent_devices_by_agent_id**](AgentsApi.md#get_agent_devices_by_agent_id) | **GET** /agents/{agent-class}/{agent-id}/devices | Information about agent devices
[**get_agents**](AgentsApi.md#get_agents) | **GET** /agents | Information about agents
[**get_agents_by_class**](AgentsApi.md#get_agents_by_class) | **GET** /agents/{agent-class} | Information about agents for a specific class
[**post_agent_by_class**](AgentsApi.md#post_agent_by_class) | **POST** /agents/{agent-class} | Create an agent
[**post_agent_device_by_agent_id**](AgentsApi.md#post_agent_device_by_agent_id) | **POST** /agents/{agent-class}/{agent-id}/devices | Create an agent device
[**post_agent_device_mapping_by_device_id**](AgentsApi.md#post_agent_device_mapping_by_device_id) | **POST** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create an agent device mapping
[**put_agent_by_class**](AgentsApi.md#put_agent_by_class) | **PUT** /agents/{agent-class} | Create or update an agent
[**put_agent_by_class_and_id**](AgentsApi.md#put_agent_by_class_and_id) | **PUT** /agents/{agent-class}/{agent-id} | Update an agent
[**put_agent_device_by_agent_id**](AgentsApi.md#put_agent_device_by_agent_id) | **PUT** /agents/{agent-class}/{agent-id}/devices | Create or update an agent device
[**put_agent_device_by_id**](AgentsApi.md#put_agent_device_by_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id} | Update an agent device
[**put_agent_device_mapping_by_device_id**](AgentsApi.md#put_agent_device_mapping_by_device_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create or update an agent device mapping
[**put_agent_device_mapping_by_id**](AgentsApi.md#put_agent_device_mapping_by_id) | **PUT** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Update an agent device mapping


# **get_agent_by_class_and_id**
> Agent get_agent_by_class_and_id(agent_id, agent_class)

Information about an agent

Gets information about an agent.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.agent import Agent
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_id = 4711 # int | The id of the agent
    agent_class = 'iosys' # str | The class of an agent

    try:
        # Information about an agent
        api_response = api_instance.get_agent_by_class_and_id(agent_id, agent_class)
        print("The response of AgentsApi->get_agent_by_class_and_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_by_class_and_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| The id of the agent | 
 **agent_class** | **str**| The class of an agent | 

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an agent |  -  |
**404** | Agent with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_device_by_id**
> List[IosysAgentDevice] get_agent_device_by_id(agent_class, agent_device_id)

Information about agent device

Gets information about agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device import IosysAgentDevice
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device

    try:
        # Information about agent device
        api_response = api_instance.get_agent_device_by_id(agent_class, agent_device_id)
        print("The response of AgentsApi->get_agent_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_device_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_id** | **int**| The id of the device | 

### Return type

[**List[IosysAgentDevice]**](IosysAgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_device_mapping_by_id**
> List[IosysAgentDeviceMapping] get_agent_device_mapping_by_id(agent_class, agent_device_mapping_id)

Information about agent device mapping

Gets information about agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_mapping_id = 4711 # int | The id of the device mapping

    try:
        # Information about agent device mapping
        api_response = api_instance.get_agent_device_mapping_by_id(agent_class, agent_device_mapping_id)
        print("The response of AgentsApi->get_agent_device_mapping_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_device_mapping_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_mapping_id** | **int**| The id of the device mapping | 

### Return type

[**List[IosysAgentDeviceMapping]**](IosysAgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_device_mappings_by_device_id**
> List[IosysAgentDeviceMapping] get_agent_device_mappings_by_device_id(agent_class, agent_device_id)

Information about agent device mappings

Gets information about mappings between agent and eliona.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device

    try:
        # Information about agent device mappings
        api_response = api_instance.get_agent_device_mappings_by_device_id(agent_class, agent_device_id)
        print("The response of AgentsApi->get_agent_device_mappings_by_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_device_mappings_by_device_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_id** | **int**| The id of the device | 

### Return type

[**List[IosysAgentDeviceMapping]**](IosysAgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agent_devices_by_agent_id**
> List[IosysAgentDevice] get_agent_devices_by_agent_id(agent_class, agent_id)

Information about agent devices

Gets information about agent devices.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device import IosysAgentDevice
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_id = 4711 # int | The id of the agent

    try:
        # Information about agent devices
        api_response = api_instance.get_agent_devices_by_agent_id(agent_class, agent_id)
        print("The response of AgentsApi->get_agent_devices_by_agent_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agent_devices_by_agent_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_id** | **int**| The id of the agent | 

### Return type

[**List[IosysAgentDevice]**](IosysAgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of devices |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents**
> List[Agent] get_agents()

Information about agents

Gets information about agents.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.agent import Agent
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)

    try:
        # Information about agents
        api_response = api_instance.get_agents()
        print("The response of AgentsApi->get_agents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Agent]**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_agents_by_class**
> List[Agent] get_agents_by_class(agent_class)

Information about agents for a specific class

Gets information about agents.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.agent import Agent
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent

    try:
        # Information about agents for a specific class
        api_response = api_instance.get_agents_by_class(agent_class)
        print("The response of AgentsApi->get_agents_by_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->get_agents_by_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 

### Return type

[**List[Agent]**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of agents |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_by_class**
> Agent post_agent_by_class(agent_class, agent)

Create an agent

Create a new agent for a specific class

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.agent import Agent
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent = eliona.api_client2.Agent() # Agent | 

    try:
        # Create an agent
        api_response = api_instance.post_agent_by_class(agent_class, agent)
        print("The response of AgentsApi->post_agent_by_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->post_agent_by_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent** | [**Agent**](Agent.md)|  | 

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_device_by_agent_id**
> IosysAgentDevice post_agent_device_by_agent_id(agent_class, agent_id, body)

Create an agent device

Create a new agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device import IosysAgentDevice
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_id = 4711 # int | The id of the agent
    body = eliona.api_client2.IosysAgentDevice() # IosysAgentDevice | 

    try:
        # Create an agent device
        api_response = api_instance.post_agent_device_by_agent_id(agent_class, agent_id, body)
        print("The response of AgentsApi->post_agent_device_by_agent_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->post_agent_device_by_agent_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_id** | **int**| The id of the agent | 
 **body** | **IosysAgentDevice**|  | 

### Return type

[**IosysAgentDevice**](IosysAgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_agent_device_mapping_by_device_id**
> IosysAgentDeviceMapping post_agent_device_mapping_by_device_id(agent_class, agent_device_id, body)

Create an agent device mapping

Create a new agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device
    body = eliona.api_client2.IosysAgentDeviceMapping() # IosysAgentDeviceMapping | 

    try:
        # Create an agent device mapping
        api_response = api_instance.post_agent_device_mapping_by_device_id(agent_class, agent_device_id, body)
        print("The response of AgentsApi->post_agent_device_mapping_by_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->post_agent_device_mapping_by_device_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_id** | **int**| The id of the device | 
 **body** | **IosysAgentDeviceMapping**|  | 

### Return type

[**IosysAgentDeviceMapping**](IosysAgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_by_class**
> Agent put_agent_by_class(agent_class, agent)

Create or update an agent

Deprecated - use POST /agents/{agent-class} for creating and PUT /agents/{agent-class}/{agent-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.agent import Agent
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent = eliona.api_client2.Agent() # Agent | 

    try:
        # Create or update an agent
        api_response = api_instance.put_agent_by_class(agent_class, agent)
        print("The response of AgentsApi->put_agent_by_class:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->put_agent_by_class: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent** | [**Agent**](Agent.md)|  | 

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_by_class_and_id**
> Agent put_agent_by_class_and_id(agent_id, agent_class, agent)

Update an agent

Update an agent.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.agent import Agent
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_id = 4711 # int | The id of the agent
    agent_class = 'iosys' # str | The class of an agent
    agent = eliona.api_client2.Agent() # Agent | 

    try:
        # Update an agent
        api_response = api_instance.put_agent_by_class_and_id(agent_id, agent_class, agent)
        print("The response of AgentsApi->put_agent_by_class_and_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->put_agent_by_class_and_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **int**| The id of the agent | 
 **agent_class** | **str**| The class of an agent | 
 **agent** | [**Agent**](Agent.md)|  | 

### Return type

[**Agent**](Agent.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing agent |  -  |
**404** | Agent with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_by_agent_id**
> IosysAgentDevice put_agent_device_by_agent_id(agent_class, agent_id, body)

Create or update an agent device

Deprecated - use POST /agents/{agent-class}/{agent-id}/devices for creating and PUT /agent-devices/{agent-class}/{agent-device-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device import IosysAgentDevice
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_id = 4711 # int | The id of the agent
    body = eliona.api_client2.IosysAgentDevice() # IosysAgentDevice | 

    try:
        # Create or update an agent device
        api_response = api_instance.put_agent_device_by_agent_id(agent_class, agent_id, body)
        print("The response of AgentsApi->put_agent_device_by_agent_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->put_agent_device_by_agent_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_id** | **int**| The id of the agent | 
 **body** | **IosysAgentDevice**|  | 

### Return type

[**IosysAgentDevice**](IosysAgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_by_id**
> IosysAgentDevice put_agent_device_by_id(agent_class, agent_device_id, body)

Update an agent device

Update a new agent device.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device import IosysAgentDevice
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device
    body = eliona.api_client2.IosysAgentDevice() # IosysAgentDevice | 

    try:
        # Update an agent device
        api_response = api_instance.put_agent_device_by_id(agent_class, agent_device_id, body)
        print("The response of AgentsApi->put_agent_device_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->put_agent_device_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_id** | **int**| The id of the device | 
 **body** | **IosysAgentDevice**|  | 

### Return type

[**IosysAgentDevice**](IosysAgentDevice.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully update a new agent device |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_mapping_by_device_id**
> IosysAgentDeviceMapping put_agent_device_mapping_by_device_id(agent_class, agent_device_id, body)

Create or update an agent device mapping

Deprecated - Use POST /agent-devices/{agent-class}/{agent-device-id}/mappings for creating and /agent-device-mappings/{agent-class}/{agent-device-mapping-id} for updating

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_id = 4711 # int | The id of the device
    body = eliona.api_client2.IosysAgentDeviceMapping() # IosysAgentDeviceMapping | 

    try:
        # Create or update an agent device mapping
        api_response = api_instance.put_agent_device_mapping_by_device_id(agent_class, agent_device_id, body)
        print("The response of AgentsApi->put_agent_device_mapping_by_device_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_device_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_id** | **int**| The id of the device | 
 **body** | **IosysAgentDeviceMapping**|  | 

### Return type

[**IosysAgentDeviceMapping**](IosysAgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_agent_device_mapping_by_id**
> IosysAgentDeviceMapping put_agent_device_mapping_by_id(agent_class, agent_device_mapping_id, body)

Update an agent device mapping

Update a new agent device mapping.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.iosys_agent_device_mapping import IosysAgentDeviceMapping
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Configure Bearer authorization (JWT): BearerAuth
configuration = eliona.api_client2.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_class = 'iosys' # str | The class of an agent
    agent_device_mapping_id = 4711 # int | The id of the device mapping
    body = eliona.api_client2.IosysAgentDeviceMapping() # IosysAgentDeviceMapping | 

    try:
        # Update an agent device mapping
        api_response = api_instance.put_agent_device_mapping_by_id(agent_class, agent_device_mapping_id, body)
        print("The response of AgentsApi->put_agent_device_mapping_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentsApi->put_agent_device_mapping_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_class** | **str**| The class of an agent | 
 **agent_device_mapping_id** | **int**| The id of the device mapping | 
 **body** | **IosysAgentDeviceMapping**|  | 

### Return type

[**IosysAgentDeviceMapping**](IosysAgentDeviceMapping.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully update a new agent device mapping |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

