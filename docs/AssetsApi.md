# eliona.api_client2.AssetsApi

All URIs are relative to *https://name.eliona.io/api/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_asset_by_id**](AssetsApi.md#delete_asset_by_id) | **DELETE** /assets/{asset-id} | Delete an asset
[**delete_bulk_assets**](AssetsApi.md#delete_bulk_assets) | **DELETE** /assets-bulk | Delete a list of assets
[**dry_run_delete_bulk_assets**](AssetsApi.md#dry_run_delete_bulk_assets) | **DELETE** /assets-bulk/dry-run | Dry-run for deleting a list of assets
[**dry_run_post_bulk_assets**](AssetsApi.md#dry_run_post_bulk_assets) | **POST** /assets-bulk/dry-run | Dry-run for creating a list of assets
[**dry_run_put_bulk_assets**](AssetsApi.md#dry_run_put_bulk_assets) | **PUT** /assets-bulk/dry-run | Dry-run for creating or updating a list of assets
[**get_asset_by_id**](AssetsApi.md#get_asset_by_id) | **GET** /assets/{asset-id} | Information about an asset
[**get_assets**](AssetsApi.md#get_assets) | **GET** /assets | Information about assets
[**get_attribute_display**](AssetsApi.md#get_attribute_display) | **GET** /attribute-display | How attributes are displayed
[**listen_asset**](AssetsApi.md#listen_asset) | **GET** /asset-listener | WebSocket connection for asset changes
[**post_asset**](AssetsApi.md#post_asset) | **POST** /assets | Create an asset
[**post_bulk_assets**](AssetsApi.md#post_bulk_assets) | **POST** /assets-bulk | Create a list of assets
[**put_asset**](AssetsApi.md#put_asset) | **PUT** /assets | Create or update an asset
[**put_asset_by_id**](AssetsApi.md#put_asset_by_id) | **PUT** /assets/{asset-id} | Update an asset
[**put_attribute_display**](AssetsApi.md#put_attribute_display) | **PUT** /attribute-display | Create or update how attributes are displayed
[**put_bulk_assets**](AssetsApi.md#put_bulk_assets) | **PUT** /assets-bulk | Create or update a list of assets


# **delete_asset_by_id**
> delete_asset_by_id(asset_id)

Delete an asset

Deletes an asset

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset

    try:
        # Delete an asset
        api_instance.delete_asset_by_id(asset_id)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_asset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset | 

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
**204** | Successfully deleted the asset |  -  |
**404** | Asset type with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_bulk_assets**
> delete_bulk_assets(request_body, identify_by=identify_by, expansions=expansions)

Delete a list of assets

Delete multiple assets based on the identifiers defined by the 'identifyBy' parameter.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Delete a list of assets
        api_instance.delete_bulk_assets(request_body, identify_by=identify_by, expansions=expansions)
    except Exception as e:
        print("Exception when calling AssetsApi->delete_bulk_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

void (empty response body)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | The complete list of assets have been successfully deleted. |  -  |
**422** | Issues may arise during the deletion process. If at least one asset encounters an error and cannot be deleted or is not found, no changes will be applied to any of the assets in the list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_delete_bulk_assets**
> List[AssetDryRun] dry_run_delete_bulk_assets(request_body, identify_by=identify_by, expansions=expansions)

Dry-run for deleting a list of assets

Simulates the process of deleting multiple assets via the 'DELETE /assets-bulk' without actually persisting any changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_dry_run import AssetDryRun
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    request_body = ['request_body_example'] # List[str] | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Dry-run for deleting a list of assets
        api_response = api_instance.dry_run_delete_bulk_assets(request_body, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->dry_run_delete_bulk_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->dry_run_delete_bulk_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**List[str]**](str.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[AssetDryRun]**](AssetDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of expected results if the request is actually performed. The content displays the list of expected results in the same order as the initial request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_post_bulk_assets**
> List[AssetDryRun] dry_run_post_bulk_assets(asset, identify_by=identify_by, expansions=expansions)

Dry-run for creating a list of assets

Simulates the process of creating assets via the 'POST /assets-bulk' endpoint without actually persisting any changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.models.asset_dry_run import AssetDryRun
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset = [eliona.api_client2.Asset()] # List[Asset] | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Dry-run for creating a list of assets
        api_response = api_instance.dry_run_post_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->dry_run_post_bulk_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->dry_run_post_bulk_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**List[Asset]**](Asset.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[AssetDryRun]**](AssetDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of expected results if the request is actually performed. The content displays the list of expected results in the same order as the initial request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **dry_run_put_bulk_assets**
> List[AssetDryRun] dry_run_put_bulk_assets(asset, identify_by=identify_by, expansions=expansions)

Dry-run for creating or updating a list of assets

Simulates the process of creating or updating assets via the 'PUT /assets-bulk' endpoint without actually persisting any changes.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.models.asset_dry_run import AssetDryRun
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset = [eliona.api_client2.Asset()] # List[Asset] | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Dry-run for creating or updating a list of assets
        api_response = api_instance.dry_run_put_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->dry_run_put_bulk_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->dry_run_put_bulk_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**List[Asset]**](Asset.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[AssetDryRun]**](AssetDryRun.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The list of expected results if the request is actually performed. The content displays the list of expected results in the same order as the initial request. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_id**
> Asset get_asset_by_id(asset_id, expansions=expansions)

Information about an asset

Gets information about an asset.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about an asset
        api_response = api_instance.get_asset_by_id(asset_id, expansions=expansions)
        print("The response of AssetsApi->get_asset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_asset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the asset by id. |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> List[Asset] get_assets(asset_type_name=asset_type_name, project_id=project_id, expansions=expansions)

Information about assets

Gets a list of assets

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset_type_name = 'weather_location' # str | Filter the name of the asset type (optional)
    project_id = 'project_id_example' # str | Filter for a specific project (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Information about assets
        api_response = api_instance.get_assets(asset_type_name=asset_type_name, project_id=project_id, expansions=expansions)
        print("The response of AssetsApi->get_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_type_name** | **str**| Filter the name of the asset type | [optional] 
 **project_id** | **str**| Filter for a specific project | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned the list of assets |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_attribute_display**
> AttributeDisplay get_attribute_display()

How attributes are displayed

Gets information about how attributes for specific assets are displayed in frontend.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.attribute_display import AttributeDisplay
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)

    try:
        # How attributes are displayed
        api_response = api_instance.get_attribute_display()
        print("The response of AssetsApi->get_attribute_display:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->get_attribute_display: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AttributeDisplay**](AttributeDisplay.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully returned display information for attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **listen_asset**
> AssetListen listen_asset(asset_id=asset_id, asset_type_name=asset_type_name, tag=tag, expansions=expansions)

WebSocket connection for asset changes

Open a WebSocket connection to get informed when asset is created, updated or deleted.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset_listen import AssetListen
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset_id = 4711 # int | Filter for a specific asset id (optional)
    asset_type_name = 'weather_location' # str | Filter the name of the asset type (optional)
    tag = 'building' # str | Filter the tag (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # WebSocket connection for asset changes
        api_response = api_instance.listen_asset(asset_id=asset_id, asset_type_name=asset_type_name, tag=tag, expansions=expansions)
        print("The response of AssetsApi->listen_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->listen_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| Filter for a specific asset id | [optional] 
 **asset_type_name** | **str**| Filter the name of the asset type | [optional] 
 **tag** | **str**| Filter the tag | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**AssetListen**](AssetListen.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully opened a connection to asset WebSocket |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset**
> Asset post_asset(asset, identify_by=identify_by, expansions=expansions)

Create an asset

This process involves creating an asset. The determination if the asset already exists and cannot be created is done by the 'identifyBy' parameter, which specifies the field used for identification. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset = eliona.api_client2.Asset() # Asset | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create an asset
        api_response = api_instance.post_asset(asset, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->post_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->post_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Successfully created a new asset  |  -  |
**422** | Issues arisen during the creation or updating process.  |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_bulk_assets**
> List[Asset] post_bulk_assets(asset, identify_by=identify_by, expansions=expansions)

Create a list of assets

This process involves creating the assets in the list. The determination if the asset already exists and cannot be created is done by the 'identifyBy' parameter, which specifies the field used for identification.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset = [eliona.api_client2.Asset()] # List[Asset] | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create a list of assets
        api_response = api_instance.post_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->post_bulk_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->post_bulk_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**List[Asset]**](Asset.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The complete list of assets has been successfully created. The content displays the list of assets in the same order as the initial request, along with some generated or default values (e.g. timestamps, IDs). |  -  |
**422** | Issues may arise during the creation process when handling the assets in the list. In such cases, if at least one asset encounters an error and cannot be created, no changes will be applied to any of the assets in the list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset**
> Asset put_asset(asset, identify_by=identify_by, expansions=expansions)

Create or update an asset

This process involves creating or updating an asset. The choice between updating or creating is determined by the 'identifyBy' parameter, which specifies the field used for identification. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset = eliona.api_client2.Asset() # Asset | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create or update an asset
        api_response = api_instance.put_asset(asset, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->put_asset:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->put_asset: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**Asset**](Asset.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully created a new or updated an existing asset |  -  |
**422** | Issues arisen during the creation or updating process. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_asset_by_id**
> Asset put_asset_by_id(asset_id, asset, expansions=expansions)

Update an asset

Deprecated: use the 'PUT /asset' method and optionally the 'identifyBy' parameter to update a specific asset. 

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset_id = 4711 # int | The id of the asset
    asset = eliona.api_client2.Asset() # Asset | 
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Update an asset
        api_response = api_instance.put_asset_by_id(asset_id, asset, expansions=expansions)
        print("The response of AssetsApi->put_asset_by_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->put_asset_by_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**| The id of the asset | 
 **asset** | [**Asset**](Asset.md)|  | 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**Asset**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated an existing asset |  -  |
**404** | Asset with id not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_attribute_display**
> AttributeDisplay put_attribute_display(attribute_display)

Create or update how attributes are displayed

Create or update how attributes are displayed in frontend. Uses the unique combination of asset id, subtype and attribute name for updating.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.attribute_display import AttributeDisplay
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    attribute_display = eliona.api_client2.AttributeDisplay() # AttributeDisplay | 

    try:
        # Create or update how attributes are displayed
        api_response = api_instance.put_attribute_display(attribute_display)
        print("The response of AssetsApi->put_attribute_display:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->put_attribute_display: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attribute_display** | [**AttributeDisplay**](AttributeDisplay.md)|  | 

### Return type

[**AttributeDisplay**](AttributeDisplay.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated or created display information for attributes |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_bulk_assets**
> List[Asset] put_bulk_assets(asset, identify_by=identify_by, expansions=expansions)

Create or update a list of assets

This process involves creating or updating assets. The choice between updating or creating an asset is determined by the 'identifyBy' parameter, which specifies the field used for identification.

### Example

* Api Key Authentication (ApiKeyAuth):
* Bearer (JWT) Authentication (BearerAuth):

```python
import time
import os
import eliona.api_client2
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://name.eliona.io/api/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = eliona.api_client2.Configuration(
    host = "https://name.eliona.io/api/v2"
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
    api_instance = eliona.api_client2.AssetsApi(api_client)
    asset = [eliona.api_client2.Asset()] # List[Asset] | 
    identify_by = 'resourceId' # str | Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn't defined, all field names are used in the order defined. So if there is no 'resourceId' present in the request body, the 'deviceId' is used and when there is also no deviceId present the 'id' field (assetId) is used.  (optional)
    expansions = ['expansions_example'] # List[str] | List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows 'ObjectName.fieldName'. (optional)

    try:
        # Create or update a list of assets
        api_response = api_instance.put_bulk_assets(asset, identify_by=identify_by, expansions=expansions)
        print("The response of AssetsApi->put_bulk_assets:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AssetsApi->put_bulk_assets: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset** | [**List[Asset]**](Asset.md)|  | 
 **identify_by** | **str**| Serves the field name send in the request body as a unique identifier for the asset, essential for operations like updates or deletions. Please refer to the Asset schema definition for further information about this fields.  In cases where this parameter isn&#39;t defined, all field names are used in the order defined. So if there is no &#39;resourceId&#39; present in the request body, the &#39;deviceId&#39; is used and when there is also no deviceId present the &#39;id&#39; field (assetId) is used.  | [optional] 
 **expansions** | [**List[str]**](str.md)| List of referenced data to load, insert or update. Each entry defines the full qualified name of the field to be expanded as follows &#39;ObjectName.fieldName&#39;. | [optional] 

### Return type

[**List[Asset]**](Asset.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The complete list of assets has been successfully created or updated. The content displays the list of assets in the same order as the initial request, along with some generated or default values (e.g. timestamps, IDs). |  -  |
**422** | Issues may arise during the creation or updating process when handling the assets in the list. In such cases, if at least one asset encounters an error and cannot be created or updated, no changes will be applied to any of the assets in the list. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

