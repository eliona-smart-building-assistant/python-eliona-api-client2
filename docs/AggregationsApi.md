# eliona.api_client2.AggregationsApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_aggregation_by_id**](AggregationsApi.md#delete_aggregation_by_id) | **DELETE** /aggregations/{aggregation-id} | Delete an aggregation
[**get_aggregation_by_id**](AggregationsApi.md#get_aggregation_by_id) | **GET** /aggregations/{aggregation-id} | Information about an aggregation
[**get_aggregations**](AggregationsApi.md#get_aggregations) | **GET** /aggregations | Information about aggregations
[**post_aggregation**](AggregationsApi.md#post_aggregation) | **POST** /aggregations | Creates an aggregation
[**put_aggregation**](AggregationsApi.md#put_aggregation) | **PUT** /aggregations | Creates or updates an aggregation
[**put_aggregation_by_id**](AggregationsApi.md#put_aggregation_by_id) | **PUT** /aggregations/{aggregation-id} | Updates an aggregation


# **delete_aggregation_by_id**
> delete_aggregation_by_id(aggregation_id)

Delete an aggregation

Deprecated: Use the 'GET /data-trend-aggregated' endpoint to retrieve aggregated data for periodic rasters without defining aggregations.
Deletes an aggregation by the given id.


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
    api_instance = eliona.api_client2.AggregationsApi(api_client)
    aggregation_id = 4711 # int | The id of the aggregation

    try:
        # Delete an aggregation
        api_instance.delete_aggregation_by_id(aggregation_id)
    except Exception as e:
        print("Exception when calling AggregationsApi->delete_aggregation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_id** | **int**| The id of the aggregation | 

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
**204** | Successfully deleted the aggregation by id. |  -  |
**404** | Aggregation with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregation_by_id**
> Aggregation get_aggregation_by_id(aggregation_id)

Information about an aggregation

Deprecated: Use the 'GET /data-trend-aggregated' endpoint to retrieve aggregated data for periodic rasters without defining aggregations.
Gets information about an aggregation by the given id.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.aggregation import Aggregation
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
    api_instance = eliona.api_client2.AggregationsApi(api_client)
    aggregation_id = 4711 # int | The id of the aggregation

    try:
        # Information about an aggregation
        api_response = api_instance.get_aggregation_by_id(aggregation_id)
        print("The response of AggregationsApi->get_aggregation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregationsApi->get_aggregation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_id** | **int**| The id of the aggregation | 

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an aggregation by id. |  -  |
**404** | Aggregation with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_aggregations**
> List[Aggregation] get_aggregations()

Information about aggregations

Deprecated: Use the 'GET /data-trend-aggregated' endpoint to retrieve aggregated data for periodic rasters without defining aggregations.
Gets a list of aggregations.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.aggregation import Aggregation
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
    api_instance = eliona.api_client2.AggregationsApi(api_client)

    try:
        # Information about aggregations
        api_response = api_instance.get_aggregations()
        print("The response of AggregationsApi->get_aggregations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregationsApi->get_aggregations: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[Aggregation]**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of aggregations |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_aggregation**
> Aggregation post_aggregation(aggregation)

Creates an aggregation

Deprecated: Use the 'GET /data-trend-aggregated' endpoint to retrieve aggregated data for periodic rasters without defining aggregations.
Creates a new aggregation.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.aggregation import Aggregation
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
    api_instance = eliona.api_client2.AggregationsApi(api_client)
    aggregation = eliona.api_client2.Aggregation() # Aggregation | 

    try:
        # Creates an aggregation
        api_response = api_instance.post_aggregation(aggregation)
        print("The response of AggregationsApi->post_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregationsApi->post_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation** | [**Aggregation**](Aggregation.md)|  | 

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created an aggregation |  -  |
**409** | Combination of asset id, subtype, attribute and raster already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aggregation**
> Aggregation put_aggregation(aggregation)

Creates or updates an aggregation

Deprecated: Use the 'GET /data-trend-aggregated' endpoint to retrieve aggregated data for periodic rasters without defining aggregations.
Creates an aggregation or updates if already exists. Uses the unique combination of asset id, subtype, attribute and raster for updating.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.aggregation import Aggregation
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
    api_instance = eliona.api_client2.AggregationsApi(api_client)
    aggregation = eliona.api_client2.Aggregation() # Aggregation | 

    try:
        # Creates or updates an aggregation
        api_response = api_instance.put_aggregation(aggregation)
        print("The response of AggregationsApi->put_aggregation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregationsApi->put_aggregation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation** | [**Aggregation**](Aggregation.md)|  | 

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created or updated an aggregation |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_aggregation_by_id**
> Aggregation put_aggregation_by_id(aggregation_id, aggregation)

Updates an aggregation

Deprecated: Use the 'GET /data-trend-aggregated' endpoint to retrieve aggregated data for periodic rasters without defining aggregations.
Updates an aggregation.


### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.aggregation import Aggregation
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
    api_instance = eliona.api_client2.AggregationsApi(api_client)
    aggregation_id = 4711 # int | The id of the aggregation
    aggregation = eliona.api_client2.Aggregation() # Aggregation | 

    try:
        # Updates an aggregation
        api_response = api_instance.put_aggregation_by_id(aggregation_id, aggregation)
        print("The response of AggregationsApi->put_aggregation_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AggregationsApi->put_aggregation_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **aggregation_id** | **int**| The id of the aggregation | 
 **aggregation** | [**Aggregation**](Aggregation.md)|  | 

### Return type

[**Aggregation**](Aggregation.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an aggregation |  -  |
**404** | Aggregation with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

