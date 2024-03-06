# eliona.api_client2.WidgetsTypesApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_widget_type_by_name**](WidgetsTypesApi.md#delete_widget_type_by_name) | **DELETE** /widget-types/{widget-type-name} | Delete a widget type
[**get_widget_type_by_name**](WidgetsTypesApi.md#get_widget_type_by_name) | **GET** /widget-types/{widget-type-name} | Information about a widget type
[**get_widget_types**](WidgetsTypesApi.md#get_widget_types) | **GET** /widget-types | List of widget types
[**post_widget_type**](WidgetsTypesApi.md#post_widget_type) | **POST** /widget-types | Create a widget type
[**put_widget_type**](WidgetsTypesApi.md#put_widget_type) | **PUT** /widget-types | Create or update a widget type
[**put_widget_type_by_name**](WidgetsTypesApi.md#put_widget_type_by_name) | **PUT** /widget-types/{widget-type-name} | Update a widget type


# **delete_widget_type_by_name**
> delete_widget_type_by_name(widget_type_name)

Delete a widget type

Deletes a widget type and the elements for this widget type.

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
    api_instance = eliona.api_client2.WidgetsTypesApi(api_client)
    widget_type_name = 'weather' # str | The name of the widget type

    try:
        # Delete a widget type
        api_instance.delete_widget_type_by_name(widget_type_name)
    except Exception as e:
        print("Exception when calling WidgetsTypesApi->delete_widget_type_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type_name** | **str**| The name of the widget type | 

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
**204** | Successfully deleted the widget type |  -  |
**404** | Widget type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_type_by_name**
> WidgetType get_widget_type_by_name(widget_type_name, expansions=expansions)

Information about a widget type

Gets information about a widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.widget_type import WidgetType
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
    api_instance = eliona.api_client2.WidgetsTypesApi(api_client)
    widget_type_name = 'weather' # str | The name of the widget type
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about a widget type
        api_response = api_instance.get_widget_type_by_name(widget_type_name, expansions=expansions)
        print("The response of WidgetsTypesApi->get_widget_type_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsTypesApi->get_widget_type_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type_name** | **str**| The name of the widget type | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a widget type by name. |  -  |
**404** | Widget type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_widget_types**
> List[WidgetType] get_widget_types(expansions=expansions)

List of widget types

Returns a list of widget types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.widget_type import WidgetType
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
    api_instance = eliona.api_client2.WidgetsTypesApi(api_client)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # List of widget types
        api_response = api_instance.get_widget_types(expansions=expansions)
        print("The response of WidgetsTypesApi->get_widget_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsTypesApi->get_widget_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[WidgetType]**](WidgetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of widget types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_widget_type**
> WidgetType post_widget_type(widget_type, expansions=expansions)

Create a widget type

Create a new widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.widget_type import WidgetType
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
    api_instance = eliona.api_client2.WidgetsTypesApi(api_client)
    widget_type = eliona.api_client2.WidgetType() # WidgetType | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create a widget type
        api_response = api_instance.post_widget_type(widget_type, expansions=expansions)
        print("The response of WidgetsTypesApi->post_widget_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsTypesApi->post_widget_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type** | [**WidgetType**](WidgetType.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created widget type |  -  |
**409** | Widget type name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_widget_type**
> WidgetType put_widget_type(widget_type, expansions=expansions)

Create or update a widget type

Create a new widget type or update it if already exists. Uses the unique widget type name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.widget_type import WidgetType
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
    api_instance = eliona.api_client2.WidgetsTypesApi(api_client)
    widget_type = eliona.api_client2.WidgetType() # WidgetType | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create or update a widget type
        api_response = api_instance.put_widget_type(widget_type, expansions=expansions)
        print("The response of WidgetsTypesApi->put_widget_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsTypesApi->put_widget_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type** | [**WidgetType**](WidgetType.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully added or updated widget type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_widget_type_by_name**
> WidgetType put_widget_type_by_name(widget_type_name, widget_type, expansions=expansions)

Update a widget type

Update a widget type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import eliona.api_client2
from eliona.api_client2.models.widget_type import WidgetType
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
    api_instance = eliona.api_client2.WidgetsTypesApi(api_client)
    widget_type_name = 'weather' # str | The name of the widget type
    widget_type = eliona.api_client2.WidgetType() # WidgetType | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Update a widget type
        api_response = api_instance.put_widget_type_by_name(widget_type_name, widget_type, expansions=expansions)
        print("The response of WidgetsTypesApi->put_widget_type_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WidgetsTypesApi->put_widget_type_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **widget_type_name** | **str**| The name of the widget type | 
 **widget_type** | [**WidgetType**](WidgetType.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**WidgetType**](WidgetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated widget type |  -  |
**404** | Widget type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

