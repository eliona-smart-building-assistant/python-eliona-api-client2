# eliona.api_client2.AssetTypesApi

All URIs are relative to *https://name.eliona.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_type_by_name**](AssetTypesApi.md#delete_asset_type_by_name) | **DELETE** /asset-types/{asset-type-name} | Delete an asset type
[**get_asset_type_by_name**](AssetTypesApi.md#get_asset_type_by_name) | **GET** /asset-types/{asset-type-name} | Information about an asset type
[**get_asset_types**](AssetTypesApi.md#get_asset_types) | **GET** /asset-types | List of asset types
[**post_asset_type**](AssetTypesApi.md#post_asset_type) | **POST** /asset-types | Create an asset type
[**post_asset_type_attribute**](AssetTypesApi.md#post_asset_type_attribute) | **POST** /asset-types/{asset-type-name}/attributes | Create asset type attribute
[**put_asset_type**](AssetTypesApi.md#put_asset_type) | **PUT** /asset-types | Create or update an asset type
[**put_asset_type_attribute**](AssetTypesApi.md#put_asset_type_attribute) | **PUT** /asset-types/{asset-type-name}/attributes | Create or update an asset type attribute
[**put_asset_type_by_name**](AssetTypesApi.md#put_asset_type_by_name) | **PUT** /asset-types/{asset-type-name} | Update an asset type


# **delete_asset_type_by_name**
> delete_asset_type_by_name(asset_type_name)

Delete an asset type

Deletes an asset type and the attributes for this asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type_name = 'weather_location' # str | The name of the asset type

    try:
        # Delete an asset type
        api_instance.delete_asset_type_by_name(asset_type_name)
    except Exception as e:
        print("Exception when calling AssetTypesApi->delete_asset_type_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type | 

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
**204** | Successfully deleted the asset type |  -  |
**404** | Asset type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_type_by_name**
> AssetType get_asset_type_by_name(asset_type_name, expansions=expansions)

Information about an asset type

Gets information about an asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type import AssetType
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type_name = 'weather_location' # str | The name of the asset type
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about an asset type
        api_response = api_instance.get_asset_type_by_name(asset_type_name, expansions=expansions)
        print("The response of AssetTypesApi->get_asset_type_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->get_asset_type_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned an asset type by name. |  -  |
**404** | Asset type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_types**
> List[AssetType] get_asset_types(expansions=expansions)

List of asset types

Returns a list of asset types

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type import AssetType
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # List of asset types
        api_response = api_instance.get_asset_types(expansions=expansions)
        print("The response of AssetTypesApi->get_asset_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->get_asset_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[AssetType]**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned a list of asset types |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_type**
> AssetType post_asset_type(asset_type, expansions=expansions)

Create an asset type

Create a new asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type import AssetType
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type = eliona.api_client2.AssetType() # AssetType | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create an asset type
        api_response = api_instance.post_asset_type(asset_type, expansions=expansions)
        print("The response of AssetTypesApi->post_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->post_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type** | [**AssetType**](AssetType.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new asset type |  -  |
**409** | Asset type name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_type_attribute**
> AssetTypeAttribute post_asset_type_attribute(asset_type_name, asset_type_attribute)

Create asset type attribute

Create a new asset type attribute.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type_attribute import AssetTypeAttribute
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type_name = 'weather_location' # str | The name of the asset type
    asset_type_attribute = eliona.api_client2.AssetTypeAttribute() # AssetTypeAttribute | 

    try:
        # Create asset type attribute
        api_response = api_instance.post_asset_type_attribute(asset_type_name, asset_type_attribute)
        print("The response of AssetTypesApi->post_asset_type_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->post_asset_type_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type | 
 **asset_type_attribute** | [**AssetTypeAttribute**](AssetTypeAttribute.md)|  | 

### Return type

[**AssetTypeAttribute**](AssetTypeAttribute.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new asset type attribute |  -  |
**409** | Combination of asset type name, subtype and attribute name already exists |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_type**
> AssetType put_asset_type(asset_type, expansions=expansions)

Create or update an asset type

Create a new asset type or update an asset type if already exists. Uses the unique asset type name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type import AssetType
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type = eliona.api_client2.AssetType() # AssetType | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create or update an asset type
        api_response = api_instance.put_asset_type(asset_type, expansions=expansions)
        print("The response of AssetTypesApi->put_asset_type:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->put_asset_type: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type** | [**AssetType**](AssetType.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing asset type |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_type_attribute**
> AssetTypeAttribute put_asset_type_attribute(asset_type_name, asset_type_attribute)

Create or update an asset type attribute

Create a new asset type attribute or update an asset type attribute if already exists. Uses the unique combination of asset type name, subtype and attribute name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type_attribute import AssetTypeAttribute
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type_name = 'weather_location' # str | The name of the asset type
    asset_type_attribute = eliona.api_client2.AssetTypeAttribute() # AssetTypeAttribute | 

    try:
        # Create or update an asset type attribute
        api_response = api_instance.put_asset_type_attribute(asset_type_name, asset_type_attribute)
        print("The response of AssetTypesApi->put_asset_type_attribute:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->put_asset_type_attribute: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type | 
 **asset_type_attribute** | [**AssetTypeAttribute**](AssetTypeAttribute.md)|  | 

### Return type

[**AssetTypeAttribute**](AssetTypeAttribute.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing asset type attribute |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_type_by_name**
> AssetType put_asset_type_by_name(asset_type_name, asset_type, expansions=expansions)

Update an asset type

Update an asset type.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_type import AssetType
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
    api_instance = eliona.api_client2.AssetTypesApi(api_client)
    asset_type_name = 'weather_location' # str | The name of the asset type
    asset_type = eliona.api_client2.AssetType() # AssetType | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Update an asset type
        api_response = api_instance.put_asset_type_by_name(asset_type_name, asset_type, expansions=expansions)
        print("The response of AssetTypesApi->put_asset_type_by_name:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetTypesApi->put_asset_type_by_name: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| The name of the asset type | 
 **asset_type** | [**AssetType**](AssetType.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AssetType**](AssetType.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing asset type |  -  |
**404** | Asset type with name not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

