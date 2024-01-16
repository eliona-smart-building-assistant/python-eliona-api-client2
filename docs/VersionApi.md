# eliona.api_client2.VersionApi

All URIs are relative to *https://name.eliona.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_open_api**](VersionApi.md#get_open_api) | **GET** /version/openapi.json | OpenAPI specification for this API version
[**get_version**](VersionApi.md#get_version) | **GET** /version | Version of the API


# **get_open_api**
> get_open_api()

OpenAPI specification for this API version

Gets specification for this API version as an openapi.json file.

### Example


```python
import time
import os
import eliona.api_client2
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.VersionApi(api_client)

    try:
        # OpenAPI specification for this API version
        api_instance.get_open_api()
    except Exception as e:
        print("Exception when calling VersionApi->get_open_api: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the openapi.json file. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> object get_version()

Version of the API

Gets information about the APIs version.

### Example


```python
import time
import os
import eliona.api_client2
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
)


# Enter a context with an instance of the API client
with eliona.api_client2.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = eliona.api_client2.VersionApi(api_client)

    try:
        # Version of the API
        api_response = api_instance.get_version()
        print("The response of VersionApi->get_version:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling VersionApi->get_version: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the APIs version. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

