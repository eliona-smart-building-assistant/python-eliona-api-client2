# eliona.api_client2.AlarmsApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alarm_by_id**](AlarmsApi.md#delete_alarm_by_id) | **DELETE** /alarms/{alarm-rule-id} | Removes an alarm
[**get_alarm_by_id**](AlarmsApi.md#get_alarm_by_id) | **GET** /alarms/{alarm-rule-id} | Information about alarm
[**get_alarm_history_by_id**](AlarmsApi.md#get_alarm_history_by_id) | **GET** /alarms-history/{alarm-rule-id} | Information about alarm history
[**get_alarms**](AlarmsApi.md#get_alarms) | **GET** /alarms | Information about alarms
[**get_alarms_history**](AlarmsApi.md#get_alarms_history) | **GET** /alarms-history | Information about alarms history
[**get_highest_alarms**](AlarmsApi.md#get_highest_alarms) | **GET** /alarms-highest | Information about most prioritized alarms
[**listen_alarm**](AlarmsApi.md#listen_alarm) | **GET** /alarm-listener | WebSocket connection for alarm changes
[**patch_alarm_by_id**](AlarmsApi.md#patch_alarm_by_id) | **PATCH** /alarms/{alarm-rule-id} | Update alarm
[**put_alarm**](AlarmsApi.md#put_alarm) | **PUT** /alarms | Create or update an alarm


# **delete_alarm_by_id**
> delete_alarm_by_id(alarm_rule_id)

Removes an alarm

Marks an alarm as gone

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule

    try:
        # Removes an alarm
        api_instance.delete_alarm_by_id(alarm_rule_id)
    except Exception as e:
        print("Exception when calling AlarmsApi->delete_alarm_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule | 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully removes an alarm |  -  |
**404** | Alarm with alarm rule id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_by_id**
> Alarm get_alarm_by_id(alarm_rule_id, expansions=expansions)

Information about alarm

Gets information about alarm.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm import Alarm
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about alarm
        api_response = api_instance.get_alarm_by_id(alarm_rule_id, expansions=expansions)
        print("The response of AlarmsApi->get_alarm_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->get_alarm_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an alarm |  -  |
**404** | Alarm with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_history_by_id**
> List[Alarm] get_alarm_history_by_id(alarm_rule_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)

Information about alarm history

Gets information about alarm over the entire time. This includes current alarm and history.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm import Alarm
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    from_date = '2020-01-01T09:00:00.000Z' # str | Filter by lower date time (RFC3339) limit inclusive (optional)
    to_date = '2021-12-31T23:00:00.000Z' # str | Filter by upper date time (RFC3339) limit exclusive (optional)
    tags = ['tags_example'] # List[str] | A list of defined tags. Result must include all of these tags, not just some. (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about alarm history
        api_response = api_instance.get_alarm_history_by_id(alarm_rule_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)
        print("The response of AlarmsApi->get_alarm_history_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->get_alarm_history_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule | 
 **from_date** | **str**| Filter by lower date time (RFC3339) limit inclusive | [optional] 
 **to_date** | **str**| Filter by upper date time (RFC3339) limit exclusive | [optional] 
 **tags** | [**List[str]**](str.md)| A list of defined tags. Result must include all of these tags, not just some. | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms**
> List[Alarm] get_alarms(project_id=project_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)

Information about alarms

Gets information about alarms

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm import Alarm
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    project_id = 'project_id_example' # str | Filter for a specific project (optional)
    from_date = '2020-01-01T09:00:00.000Z' # str | Filter by lower date time (RFC3339) limit inclusive (optional)
    to_date = '2021-12-31T23:00:00.000Z' # str | Filter by upper date time (RFC3339) limit exclusive (optional)
    tags = ['tags_example'] # List[str] | A list of defined tags. Result must include all of these tags, not just some. (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about alarms
        api_response = api_instance.get_alarms(project_id=project_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)
        print("The response of AlarmsApi->get_alarms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->get_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Filter for a specific project | [optional] 
 **from_date** | **str**| Filter by lower date time (RFC3339) limit inclusive | [optional] 
 **to_date** | **str**| Filter by upper date time (RFC3339) limit exclusive | [optional] 
 **tags** | [**List[str]**](str.md)| A list of defined tags. Result must include all of these tags, not just some. | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarms_history**
> List[Alarm] get_alarms_history(project_id=project_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)

Information about alarms history

Gets information about alarms over the entire time. This includes current alarms and alarms, which are already processed.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm import Alarm
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    project_id = 'project_id_example' # str | Filter for a specific project (optional)
    from_date = '2020-01-01T09:00:00.000Z' # str | Filter by lower date time (RFC3339) limit inclusive (optional)
    to_date = '2021-12-31T23:00:00.000Z' # str | Filter by upper date time (RFC3339) limit exclusive (optional)
    tags = ['tags_example'] # List[str] | A list of defined tags. Result must include all of these tags, not just some. (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about alarms history
        api_response = api_instance.get_alarms_history(project_id=project_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)
        print("The response of AlarmsApi->get_alarms_history:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->get_alarms_history: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Filter for a specific project | [optional] 
 **from_date** | **str**| Filter by lower date time (RFC3339) limit inclusive | [optional] 
 **to_date** | **str**| Filter by upper date time (RFC3339) limit exclusive | [optional] 
 **tags** | [**List[str]**](str.md)| A list of defined tags. Result must include all of these tags, not just some. | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_highest_alarms**
> List[Alarm] get_highest_alarms(project_id=project_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)

Information about most prioritized alarms

Gets information about an alarms with the highest priority for each asset.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm import Alarm
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    project_id = 'project_id_example' # str | Filter for a specific project (optional)
    from_date = '2020-01-01T09:00:00.000Z' # str | Filter by lower date time (RFC3339) limit inclusive (optional)
    to_date = '2021-12-31T23:00:00.000Z' # str | Filter by upper date time (RFC3339) limit exclusive (optional)
    tags = ['tags_example'] # List[str] | A list of defined tags. Result must include all of these tags, not just some. (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about most prioritized alarms
        api_response = api_instance.get_highest_alarms(project_id=project_id, from_date=from_date, to_date=to_date, tags=tags, expansions=expansions)
        print("The response of AlarmsApi->get_highest_alarms:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->get_highest_alarms: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| Filter for a specific project | [optional] 
 **from_date** | **str**| Filter by lower date time (RFC3339) limit inclusive | [optional] 
 **to_date** | **str**| Filter by upper date time (RFC3339) limit exclusive | [optional] 
 **tags** | [**List[str]**](str.md)| A list of defined tags. Result must include all of these tags, not just some. | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Alarm]**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of most prioritized alarms |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_alarm**
> AlarmListen listen_alarm(expansions=expansions)

WebSocket connection for alarm changes

Open a WebSocket connection to get informed when new alarm data is written or anything changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm_listen import AlarmListen
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # WebSocket connection for alarm changes
        api_response = api_instance.listen_alarm(expansions=expansions)
        print("The response of AlarmsApi->listen_alarm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->listen_alarm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AlarmListen**](AlarmListen.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully opened a connection to alarm WebSocket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **patch_alarm_by_id**
> patch_alarm_by_id(alarm_rule_id, acknowledged, acknowledge_text=acknowledge_text)

Update alarm

Update properties of alarm for given id.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    acknowledged = True # bool | Marks the alarm as acknowledged or not acknowledged by setting the acknowledge timestamp to now or to null.
    acknowledge_text = 'acknowledge_text_example' # str | Sets the text for acknowledgement if acknowledged is set to true (optional)

    try:
        # Update alarm
        api_instance.patch_alarm_by_id(alarm_rule_id, acknowledged, acknowledge_text=acknowledge_text)
    except Exception as e:
        print("Exception when calling AlarmsApi->patch_alarm_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule | 
 **acknowledged** | **bool**| Marks the alarm as acknowledged or not acknowledged by setting the acknowledge timestamp to now or to null. | 
 **acknowledge_text** | **str**| Sets the text for acknowledgement if acknowledged is set to true | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated the alarm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alarm**
> Alarm put_alarm(alarm)

Create or update an alarm

Creates or updates an alarm

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm import Alarm
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
    api_instance = eliona.api_client2.AlarmsApi(api_client)
    alarm = eliona.api_client2.Alarm() # Alarm | 

    try:
        # Create or update an alarm
        api_response = api_instance.put_alarm(alarm)
        print("The response of AlarmsApi->put_alarm:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmsApi->put_alarm: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm** | [**Alarm**](Alarm.md)|  | 

### Return type

[**Alarm**](Alarm.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing alarm |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

