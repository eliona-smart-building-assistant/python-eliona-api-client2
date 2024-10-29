# eliona.api_client2.AlarmRulesApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_alarm_rule_by_id**](AlarmRulesApi.md#delete_alarm_rule_by_id) | **DELETE** /alarm-rules/{alarm-rule-id} | Delete an alarm rule
[**get_alarm_rule_by_id**](AlarmRulesApi.md#get_alarm_rule_by_id) | **GET** /alarm-rules/{alarm-rule-id} | Information about an alarm rule
[**get_alarm_rules**](AlarmRulesApi.md#get_alarm_rules) | **GET** /alarm-rules | Information about alarm rules
[**post_alarm_rule**](AlarmRulesApi.md#post_alarm_rule) | **POST** /alarm-rules | Create an alarm rule
[**put_alarm_rule**](AlarmRulesApi.md#put_alarm_rule) | **PUT** /alarm-rules | Create or update an alarm rule
[**put_alarm_rule_by_id**](AlarmRulesApi.md#put_alarm_rule_by_id) | **PUT** /alarm-rules/{alarm-rule-id} | Update an alarm rule


# **delete_alarm_rule_by_id**
> delete_alarm_rule_by_id(alarm_rule_id)

Delete an alarm rule

Deletes an alarm rule.

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
    api_instance = eliona.api_client2.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule

    try:
        # Delete an alarm rule
        api_instance.delete_alarm_rule_by_id(alarm_rule_id)
    except Exception as e:
        print("Exception when calling AlarmRulesApi->delete_alarm_rule_by_id: %s\n" % e)
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
**204** | Successfully deleted the alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_rule_by_id**
> AlarmRule get_alarm_rule_by_id(alarm_rule_id, expansions=expansions)

Information about an alarm rule

Gets information about an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm_rule import AlarmRule
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
    api_instance = eliona.api_client2.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about an alarm rule
        api_response = api_instance.get_alarm_rule_by_id(alarm_rule_id, expansions=expansions)
        print("The response of AlarmRulesApi->get_alarm_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alarm_rules**
> List[AlarmRule] get_alarm_rules(alarm_rule_ids=alarm_rule_ids, asset_id=asset_id, expansions=expansions)

Information about alarm rules

Gets information about alarm rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm_rule import AlarmRule
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
    api_instance = eliona.api_client2.AlarmRulesApi(api_client)
    alarm_rule_ids = [56] # List[int] | List of alarm rule ids for filtering (optional)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about alarm rules
        api_response = api_instance.get_alarm_rules(alarm_rule_ids=alarm_rule_ids, asset_id=asset_id, expansions=expansions)
        print("The response of AlarmRulesApi->get_alarm_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmRulesApi->get_alarm_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_ids** | [**List[int]**](int.md)| List of alarm rule ids for filtering | [optional] 
 **asset_id** | **int**| Filter for a specific asset id | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[AlarmRule]**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of alarm rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_alarm_rule**
> AlarmRule post_alarm_rule(alarm_rule)

Create an alarm rule

Create a new alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm_rule import AlarmRule
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
    api_instance = eliona.api_client2.AlarmRulesApi(api_client)
    alarm_rule = eliona.api_client2.AlarmRule() # AlarmRule | 

    try:
        # Create an alarm rule
        api_response = api_instance.post_alarm_rule(alarm_rule)
        print("The response of AlarmRulesApi->post_alarm_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmRulesApi->post_alarm_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  | 

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new alarm rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alarm_rule**
> AlarmRule put_alarm_rule(alarm_rule)

Create or update an alarm rule

Deprecated - Use POST /alarm-rules to create and PUT /alarm-rules/{alarm-rule-id} to update

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm_rule import AlarmRule
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
    api_instance = eliona.api_client2.AlarmRulesApi(api_client)
    alarm_rule = eliona.api_client2.AlarmRule() # AlarmRule | 

    try:
        # Create or update an alarm rule
        api_response = api_instance.put_alarm_rule(alarm_rule)
        print("The response of AlarmRulesApi->put_alarm_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  | 

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing alarm rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_alarm_rule_by_id**
> AlarmRule put_alarm_rule_by_id(alarm_rule_id, alarm_rule)

Update an alarm rule

Update an alarm rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.alarm_rule import AlarmRule
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
    api_instance = eliona.api_client2.AlarmRulesApi(api_client)
    alarm_rule_id = 4711 # int | The id of the alarm rule
    alarm_rule = eliona.api_client2.AlarmRule() # AlarmRule | 

    try:
        # Update an alarm rule
        api_response = api_instance.put_alarm_rule_by_id(alarm_rule_id, alarm_rule)
        print("The response of AlarmRulesApi->put_alarm_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AlarmRulesApi->put_alarm_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **alarm_rule_id** | **int**| The id of the alarm rule | 
 **alarm_rule** | [**AlarmRule**](AlarmRule.md)|  | 

### Return type

[**AlarmRule**](AlarmRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing alarm rule |  -  |
**404** | Alarm rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

