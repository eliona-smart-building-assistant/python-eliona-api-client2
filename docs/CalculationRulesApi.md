# eliona.api_client2.CalculationRulesApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_calculation_rule_by_id**](CalculationRulesApi.md#delete_calculation_rule_by_id) | **DELETE** /calculation-rules/{calculation-rule-id} | Delete a calculation rule
[**get_calculation_rule_by_id**](CalculationRulesApi.md#get_calculation_rule_by_id) | **GET** /calculation-rules/{calculation-rule-id} | Information about a calculation rules rule
[**get_calculation_rules**](CalculationRulesApi.md#get_calculation_rules) | **GET** /calculation-rules | Information about calculation rules
[**put_calculation_rule**](CalculationRulesApi.md#put_calculation_rule) | **PUT** /calculation-rules | Creates or updates a calculation rule
[**put_calculation_rule_by_id**](CalculationRulesApi.md#put_calculation_rule_by_id) | **PUT** /calculation-rules/{calculation-rule-id} | Update a calculation rule


# **delete_calculation_rule_by_id**
> delete_calculation_rule_by_id(calculation_rule_id)

Delete a calculation rule

Deletes a calculation rule.

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
    api_instance = eliona.api_client2.CalculationRulesApi(api_client)
    calculation_rule_id = 4711 # int | The id of the calculation rule

    try:
        # Delete a calculation rule
        api_instance.delete_calculation_rule_by_id(calculation_rule_id)
    except Exception as e:
        print("Exception when calling CalculationRulesApi->delete_calculation_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_id** | **int**| The id of the calculation rule | 

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
**204** | Successfully deleted the calculation rule |  -  |
**404** | Calculation rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_rule_by_id**
> CalculationRule get_calculation_rule_by_id(calculation_rule_id)

Information about a calculation rules rule

Gets information about a calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.calculation_rule import CalculationRule
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
    api_instance = eliona.api_client2.CalculationRulesApi(api_client)
    calculation_rule_id = 4711 # int | The id of the calculation rule

    try:
        # Information about a calculation rules rule
        api_response = api_instance.get_calculation_rule_by_id(calculation_rule_id)
        print("The response of CalculationRulesApi->get_calculation_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationRulesApi->get_calculation_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_id** | **int**| The id of the calculation rule | 

### Return type

[**CalculationRule**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned ancalculation rule |  -  |
**404** | Calculation rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_calculation_rules**
> List[CalculationRule] get_calculation_rules(calculation_rule_ids=calculation_rule_ids)

Information about calculation rules

Gets information about calculation rules.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.calculation_rule import CalculationRule
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
    api_instance = eliona.api_client2.CalculationRulesApi(api_client)
    calculation_rule_ids = [56] # List[int] | List of calculation rule ids for filtering (optional)

    try:
        # Information about calculation rules
        api_response = api_instance.get_calculation_rules(calculation_rule_ids=calculation_rule_ids)
        print("The response of CalculationRulesApi->get_calculation_rules:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationRulesApi->get_calculation_rules: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_ids** | [**List[int]**](int.md)| List of calculation rule ids for filtering | [optional] 

### Return type

[**List[CalculationRule]**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of calculation rules |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_calculation_rule**
> CalculationRule put_calculation_rule(calculation_rule)

Creates or updates a calculation rule

Creates a new or updates an existing calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.calculation_rule import CalculationRule
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
    api_instance = eliona.api_client2.CalculationRulesApi(api_client)
    calculation_rule = eliona.api_client2.CalculationRule() # CalculationRule | 

    try:
        # Creates or updates a calculation rule
        api_response = api_instance.put_calculation_rule(calculation_rule)
        print("The response of CalculationRulesApi->put_calculation_rule:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationRulesApi->put_calculation_rule: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule** | [**CalculationRule**](CalculationRule.md)|  | 

### Return type

[**CalculationRule**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created or updated a calculation rule |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_calculation_rule_by_id**
> CalculationRule put_calculation_rule_by_id(calculation_rule_id, calculation_rule)

Update a calculation rule

Update a calculation rule.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.calculation_rule import CalculationRule
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
    api_instance = eliona.api_client2.CalculationRulesApi(api_client)
    calculation_rule_id = 4711 # int | The id of the calculation rule
    calculation_rule = eliona.api_client2.CalculationRule() # CalculationRule | 

    try:
        # Update a calculation rule
        api_response = api_instance.put_calculation_rule_by_id(calculation_rule_id, calculation_rule)
        print("The response of CalculationRulesApi->put_calculation_rule_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationRulesApi->put_calculation_rule_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **calculation_rule_id** | **int**| The id of the calculation rule | 
 **calculation_rule** | [**CalculationRule**](CalculationRule.md)|  | 

### Return type

[**CalculationRule**](CalculationRule.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing calculation rule |  -  |
**404** | Calculation rule with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

