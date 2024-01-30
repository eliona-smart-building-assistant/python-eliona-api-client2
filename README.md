# Python Eliona API client 2
The Eliona REST API enables unified access to the resources and data of an Eliona environment.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 2.6.1
- Package version: 2.6.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen
For more information, please visit [https://eliona.io](https://eliona.io)

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/eliona-smart-building-assistant/python-eliona-api-client.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/eliona-smart-building-assistant/python-eliona-api-client.git`)

Then import the package:
```python
import eliona.api_client2
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import eliona.api_client2
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
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
    api_instance = eliona.api_client2.AgentsApi(api_client)
    agent_id = 4711 # int | The id of the agent
    agent_class = 'iosys' # str | The class of an agent

    try:
        # Information about an agent
        api_response = api_instance.get_agent_by_class_and_id(agent_id, agent_class)
        print("The response of AgentsApi->get_agent_by_class_and_id:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AgentsApi->get_agent_by_class_and_id: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://name.eliona.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AgentsApi* | [**get_agent_by_class_and_id**](docs/AgentsApi.md#get_agent_by_class_and_id) | **GET** /agents/{agent-class}/{agent-id} | Information about an agent
*AgentsApi* | [**get_agent_device_by_id**](docs/AgentsApi.md#get_agent_device_by_id) | **GET** /agent-devices/{agent-class}/{agent-device-id} | Information about agent device
*AgentsApi* | [**get_agent_device_mapping_by_id**](docs/AgentsApi.md#get_agent_device_mapping_by_id) | **GET** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Information about agent device mapping
*AgentsApi* | [**get_agent_device_mappings_by_device_id**](docs/AgentsApi.md#get_agent_device_mappings_by_device_id) | **GET** /agent-devices/{agent-class}/{agent-device-id}/mappings | Information about agent device mappings
*AgentsApi* | [**get_agent_devices_by_agent_id**](docs/AgentsApi.md#get_agent_devices_by_agent_id) | **GET** /agents/{agent-class}/{agent-id}/devices | Information about agent devices
*AgentsApi* | [**get_agents**](docs/AgentsApi.md#get_agents) | **GET** /agents | Information about agents
*AgentsApi* | [**get_agents_by_class**](docs/AgentsApi.md#get_agents_by_class) | **GET** /agents/{agent-class} | Information about agents for a specific class
*AgentsApi* | [**post_agent_by_class**](docs/AgentsApi.md#post_agent_by_class) | **POST** /agents/{agent-class} | Create an agent
*AgentsApi* | [**post_agent_device_by_agent_id**](docs/AgentsApi.md#post_agent_device_by_agent_id) | **POST** /agents/{agent-class}/{agent-id}/devices | Create an agent device
*AgentsApi* | [**post_agent_device_mapping_by_device_id**](docs/AgentsApi.md#post_agent_device_mapping_by_device_id) | **POST** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create an agent device mapping
*AgentsApi* | [**put_agent_by_class**](docs/AgentsApi.md#put_agent_by_class) | **PUT** /agents/{agent-class} | Create or update an agent
*AgentsApi* | [**put_agent_by_class_and_id**](docs/AgentsApi.md#put_agent_by_class_and_id) | **PUT** /agents/{agent-class}/{agent-id} | Update an agent
*AgentsApi* | [**put_agent_device_by_agent_id**](docs/AgentsApi.md#put_agent_device_by_agent_id) | **PUT** /agents/{agent-class}/{agent-id}/devices | Create or update an agent device
*AgentsApi* | [**put_agent_device_by_id**](docs/AgentsApi.md#put_agent_device_by_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id} | Update an agent device
*AgentsApi* | [**put_agent_device_mapping_by_device_id**](docs/AgentsApi.md#put_agent_device_mapping_by_device_id) | **PUT** /agent-devices/{agent-class}/{agent-device-id}/mappings | Create or update an agent device mapping
*AgentsApi* | [**put_agent_device_mapping_by_id**](docs/AgentsApi.md#put_agent_device_mapping_by_id) | **PUT** /agent-device-mappings/{agent-class}/{agent-device-mapping-id} | Update an agent device mapping
*AggregationsApi* | [**delete_aggregation_by_id**](docs/AggregationsApi.md#delete_aggregation_by_id) | **DELETE** /aggregations/{aggregation-id} | Delete an aggregation
*AggregationsApi* | [**get_aggregation_by_id**](docs/AggregationsApi.md#get_aggregation_by_id) | **GET** /aggregations/{aggregation-id} | Information about an aggregation
*AggregationsApi* | [**get_aggregations**](docs/AggregationsApi.md#get_aggregations) | **GET** /aggregations | Information about aggregations
*AggregationsApi* | [**post_aggregation**](docs/AggregationsApi.md#post_aggregation) | **POST** /aggregations | Creates an aggregation
*AggregationsApi* | [**put_aggregation**](docs/AggregationsApi.md#put_aggregation) | **PUT** /aggregations | Creates or updates an aggregation
*AggregationsApi* | [**put_aggregation_by_id**](docs/AggregationsApi.md#put_aggregation_by_id) | **PUT** /aggregations/{aggregation-id} | Updates an aggregation
*AlarmRulesApi* | [**delete_alarm_rule_by_id**](docs/AlarmRulesApi.md#delete_alarm_rule_by_id) | **DELETE** /alarm-rules/{alarm-rule-id} | Delete an alarm rule
*AlarmRulesApi* | [**get_alarm_rule_by_id**](docs/AlarmRulesApi.md#get_alarm_rule_by_id) | **GET** /alarm-rules/{alarm-rule-id} | Information about an alarm rule
*AlarmRulesApi* | [**get_alarm_rules**](docs/AlarmRulesApi.md#get_alarm_rules) | **GET** /alarm-rules | Information about alarm rules
*AlarmRulesApi* | [**post_alarm_rule**](docs/AlarmRulesApi.md#post_alarm_rule) | **POST** /alarm-rules | Create an alarm rule
*AlarmRulesApi* | [**put_alarm_rule**](docs/AlarmRulesApi.md#put_alarm_rule) | **PUT** /alarm-rules | Create or update an alarm rule
*AlarmRulesApi* | [**put_alarm_rule_by_id**](docs/AlarmRulesApi.md#put_alarm_rule_by_id) | **PUT** /alarm-rules/{alarm-rule-id} | Update an alarm rule
*AlarmsApi* | [**get_alarm_by_id**](docs/AlarmsApi.md#get_alarm_by_id) | **GET** /alarms/{alarm-rule-id} | Information about alarm
*AlarmsApi* | [**get_alarm_history_by_id**](docs/AlarmsApi.md#get_alarm_history_by_id) | **GET** /alarms-history/{alarm-rule-id} | Information about alarm history
*AlarmsApi* | [**get_alarms**](docs/AlarmsApi.md#get_alarms) | **GET** /alarms | Information about alarms
*AlarmsApi* | [**get_alarms_history**](docs/AlarmsApi.md#get_alarms_history) | **GET** /alarms-history | Information about alarms history
*AlarmsApi* | [**get_highest_alarms**](docs/AlarmsApi.md#get_highest_alarms) | **GET** /alarms-highest | Information about most prioritized alarms
*AlarmsApi* | [**listen_alarm**](docs/AlarmsApi.md#listen_alarm) | **GET** /alarm-listener | WebSocket connection for alarm changes
*AlarmsApi* | [**patch_alarm_by_id**](docs/AlarmsApi.md#patch_alarm_by_id) | **PATCH** /alarms/{alarm-rule-id} | Update alarm
*AppsApi* | [**get_app_by_name**](docs/AppsApi.md#get_app_by_name) | **GET** /apps/{app-name} | Information about an app
*AppsApi* | [**get_patch_by_name**](docs/AppsApi.md#get_patch_by_name) | **GET** /apps/{app-name}/patches/{patch-name} | Information about a patch for an app
*AppsApi* | [**patch_app_by_name**](docs/AppsApi.md#patch_app_by_name) | **PATCH** /apps/{app-name} | Update an app
*AppsApi* | [**patch_patch_by_name**](docs/AppsApi.md#patch_patch_by_name) | **PATCH** /apps/{app-name}/patches/{patch-name} | Updates a patch
*AssetTypesApi* | [**delete_asset_type_by_name**](docs/AssetTypesApi.md#delete_asset_type_by_name) | **DELETE** /asset-types/{asset-type-name} | Delete an asset type
*AssetTypesApi* | [**get_asset_type_by_name**](docs/AssetTypesApi.md#get_asset_type_by_name) | **GET** /asset-types/{asset-type-name} | Information about an asset type
*AssetTypesApi* | [**get_asset_types**](docs/AssetTypesApi.md#get_asset_types) | **GET** /asset-types | List of asset types
*AssetTypesApi* | [**post_asset_type**](docs/AssetTypesApi.md#post_asset_type) | **POST** /asset-types | Create an asset type
*AssetTypesApi* | [**post_asset_type_attribute**](docs/AssetTypesApi.md#post_asset_type_attribute) | **POST** /asset-types/{asset-type-name}/attributes | Create asset type attribute
*AssetTypesApi* | [**put_asset_type**](docs/AssetTypesApi.md#put_asset_type) | **PUT** /asset-types | Create or update an asset type
*AssetTypesApi* | [**put_asset_type_attribute**](docs/AssetTypesApi.md#put_asset_type_attribute) | **PUT** /asset-types/{asset-type-name}/attributes | Create or update an asset type attribute
*AssetTypesApi* | [**put_asset_type_by_name**](docs/AssetTypesApi.md#put_asset_type_by_name) | **PUT** /asset-types/{asset-type-name} | Update an asset type
*AssetsApi* | [**delete_asset_by_id**](docs/AssetsApi.md#delete_asset_by_id) | **DELETE** /assets/{asset-id} | Delete an asset
*AssetsApi* | [**delete_bulk_assets**](docs/AssetsApi.md#delete_bulk_assets) | **DELETE** /assets-bulk | Delete a list of assets
*AssetsApi* | [**dry_run_delete_bulk_assets**](docs/AssetsApi.md#dry_run_delete_bulk_assets) | **DELETE** /assets-bulk/dry-run | Dry-run for deleting a list of assets
*AssetsApi* | [**dry_run_post_bulk_assets**](docs/AssetsApi.md#dry_run_post_bulk_assets) | **POST** /assets-bulk/dry-run | Dry-run for creating a list of assets
*AssetsApi* | [**dry_run_put_bulk_assets**](docs/AssetsApi.md#dry_run_put_bulk_assets) | **PUT** /assets-bulk/dry-run | Dry-run for creating or updating a list of assets
*AssetsApi* | [**get_asset_by_id**](docs/AssetsApi.md#get_asset_by_id) | **GET** /assets/{asset-id} | Information about an asset
*AssetsApi* | [**get_assets**](docs/AssetsApi.md#get_assets) | **GET** /assets | Information about assets
*AssetsApi* | [**get_attribute_display**](docs/AssetsApi.md#get_attribute_display) | **GET** /attribute-display | How attributes are displayed
*AssetsApi* | [**listen_asset**](docs/AssetsApi.md#listen_asset) | **GET** /asset-listener | WebSocket connection for asset changes
*AssetsApi* | [**post_asset**](docs/AssetsApi.md#post_asset) | **POST** /assets | Create an asset
*AssetsApi* | [**post_bulk_assets**](docs/AssetsApi.md#post_bulk_assets) | **POST** /assets-bulk | Create a list of assets
*AssetsApi* | [**put_asset**](docs/AssetsApi.md#put_asset) | **PUT** /assets | Create or update an asset
*AssetsApi* | [**put_asset_by_id**](docs/AssetsApi.md#put_asset_by_id) | **PUT** /assets/{asset-id} | Update an asset
*AssetsApi* | [**put_attribute_display**](docs/AssetsApi.md#put_attribute_display) | **PUT** /attribute-display | Create or update how attributes are displayed
*AssetsApi* | [**put_bulk_assets**](docs/AssetsApi.md#put_bulk_assets) | **PUT** /assets-bulk | Create or update a list of assets
*CommunicationApi* | [**get_message_receipt_by_id**](docs/CommunicationApi.md#get_message_receipt_by_id) | **GET** /message-receipts/{message-id} | Information about a message
*CommunicationApi* | [**post_mail**](docs/CommunicationApi.md#post_mail) | **POST** /send-mail | Send e-mail
*CommunicationApi* | [**post_notification**](docs/CommunicationApi.md#post_notification) | **POST** /send-notification | Send notification
*DashboardsApi* | [**get_dashboard_by_id**](docs/DashboardsApi.md#get_dashboard_by_id) | **GET** /dashboards/{dashboard-id} | Information about a dashboard
*DashboardsApi* | [**get_dashboards**](docs/DashboardsApi.md#get_dashboards) | **GET** /dashboards | Information about dashboards
*DashboardsApi* | [**post_dashboard**](docs/DashboardsApi.md#post_dashboard) | **POST** /dashboards | Creates a new dashboard
*DataApi* | [**get_data**](docs/DataApi.md#get_data) | **GET** /data | Gets all data
*DataApi* | [**get_data_aggregated**](docs/DataApi.md#get_data_aggregated) | **GET** /data-aggregated | Get aggregated data
*DataApi* | [**get_data_trends**](docs/DataApi.md#get_data_trends) | **GET** /data-trends | Get trend of historical data
*DataApi* | [**listen_data**](docs/DataApi.md#listen_data) | **GET** /data-listener | WebSocket connection for asset data changes
*DataApi* | [**put_bulk_data**](docs/DataApi.md#put_bulk_data) | **PUT** /data-bulk | Create or update multiple asset data
*DataApi* | [**put_data**](docs/DataApi.md#put_data) | **PUT** /data | Create or update asset data
*NodesApi* | [**get_node_by_ident**](docs/NodesApi.md#get_node_by_ident) | **GET** /nodes/{node-ident} | Information about a node
*NodesApi* | [**get_nodes**](docs/NodesApi.md#get_nodes) | **GET** /nodes | Information about nodes
*NodesApi* | [**post_node**](docs/NodesApi.md#post_node) | **POST** /nodes | Create a node
*NodesApi* | [**put_node**](docs/NodesApi.md#put_node) | **PUT** /nodes | Create or update a node
*NodesApi* | [**put_node_by_ident**](docs/NodesApi.md#put_node_by_ident) | **PUT** /nodes/{node-ident} | Update a node
*ProjectsApi* | [**get_project_by_id**](docs/ProjectsApi.md#get_project_by_id) | **GET** /projects/{project-id} | Information about a project
*ProjectsApi* | [**get_projects**](docs/ProjectsApi.md#get_projects) | **GET** /projects | Information about projects
*ProjectsApi* | [**put_project**](docs/ProjectsApi.md#put_project) | **PUT** /projects | Create or update a project
*QRCodesApi* | [**get_qr_code_by_asset_id**](docs/QRCodesApi.md#get_qr_code_by_asset_id) | **GET** /qr-codes/assets/{asset-id} | QR code for assets
*TagsApi* | [**get_tag_by_name**](docs/TagsApi.md#get_tag_by_name) | **GET** /tags/{tag-name} | Information about a tag
*TagsApi* | [**get_tags**](docs/TagsApi.md#get_tags) | **GET** /tags | Information about tags
*TagsApi* | [**put_tag**](docs/TagsApi.md#put_tag) | **PUT** /tags | Create or update a tag
*UsersApi* | [**get_user_by_id**](docs/UsersApi.md#get_user_by_id) | **GET** /users/{user-id} | Information about an user
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /users | Information about users
*UsersApi* | [**put_user**](docs/UsersApi.md#put_user) | **PUT** /users | Create or update an user
*VersionApi* | [**get_open_api**](docs/VersionApi.md#get_open_api) | **GET** /version/openapi.json | OpenAPI specification for this API version
*VersionApi* | [**get_version**](docs/VersionApi.md#get_version) | **GET** /version | Version of the API
*WidgetsApi* | [**get_dashboard_widgets**](docs/WidgetsApi.md#get_dashboard_widgets) | **GET** /dashboards/{dashboard-id}/widgets | Information about widgets on dashboard
*WidgetsApi* | [**post_dashboard_widget**](docs/WidgetsApi.md#post_dashboard_widget) | **POST** /dashboards/{dashboard-id}/widgets | Adds widget to dashboard
*WidgetsTypesApi* | [**delete_widget_type_by_name**](docs/WidgetsTypesApi.md#delete_widget_type_by_name) | **DELETE** /widget-types/{widget-type-name} | Delete a widget type
*WidgetsTypesApi* | [**get_widget_type_by_name**](docs/WidgetsTypesApi.md#get_widget_type_by_name) | **GET** /widget-types/{widget-type-name} | Information about a widget type
*WidgetsTypesApi* | [**get_widget_types**](docs/WidgetsTypesApi.md#get_widget_types) | **GET** /widget-types | List of widget types
*WidgetsTypesApi* | [**post_widget_type**](docs/WidgetsTypesApi.md#post_widget_type) | **POST** /widget-types | Create a widget type
*WidgetsTypesApi* | [**put_widget_type**](docs/WidgetsTypesApi.md#put_widget_type) | **PUT** /widget-types | Create or update a widget type
*WidgetsTypesApi* | [**put_widget_type_by_name**](docs/WidgetsTypesApi.md#put_widget_type_by_name) | **PUT** /widget-types/{widget-type-name} | Update a widget type


## Documentation For Models

 - [Agent](docs/Agent.md)
 - [AgentClass](docs/AgentClass.md)
 - [AgentDevice](docs/AgentDevice.md)
 - [AgentDeviceGeneral](docs/AgentDeviceGeneral.md)
 - [AgentDeviceMapping](docs/AgentDeviceMapping.md)
 - [AgentDeviceMappingGeneral](docs/AgentDeviceMappingGeneral.md)
 - [Aggregation](docs/Aggregation.md)
 - [Alarm](docs/Alarm.md)
 - [AlarmListen](docs/AlarmListen.md)
 - [AlarmPriority](docs/AlarmPriority.md)
 - [AlarmRule](docs/AlarmRule.md)
 - [App](docs/App.md)
 - [Asset](docs/Asset.md)
 - [AssetDryRun](docs/AssetDryRun.md)
 - [AssetIdentifyBy](docs/AssetIdentifyBy.md)
 - [AssetListen](docs/AssetListen.md)
 - [AssetType](docs/AssetType.md)
 - [AssetTypeAttribute](docs/AssetTypeAttribute.md)
 - [Attachment](docs/Attachment.md)
 - [AttributeDisplay](docs/AttributeDisplay.md)
 - [Dashboard](docs/Dashboard.md)
 - [Data](docs/Data.md)
 - [DataAggregated](docs/DataAggregated.md)
 - [DataListen](docs/DataListen.md)
 - [DataSubtype](docs/DataSubtype.md)
 - [DryRunGeneral](docs/DryRunGeneral.md)
 - [IosysAgentDevice](docs/IosysAgentDevice.md)
 - [IosysAgentDeviceMapping](docs/IosysAgentDeviceMapping.md)
 - [MbusAgentDevice](docs/MbusAgentDevice.md)
 - [MbusAgentDeviceMapping](docs/MbusAgentDeviceMapping.md)
 - [Message](docs/Message.md)
 - [MessageReceipt](docs/MessageReceipt.md)
 - [Node](docs/Node.md)
 - [Notification](docs/Notification.md)
 - [Patch](docs/Patch.md)
 - [Project](docs/Project.md)
 - [Tag](docs/Tag.md)
 - [Translation](docs/Translation.md)
 - [User](docs/User.md)
 - [ValueMapping](docs/ValueMapping.md)
 - [Widget](docs/Widget.md)
 - [WidgetData](docs/WidgetData.md)
 - [WidgetType](docs/WidgetType.md)
 - [WidgetTypeElement](docs/WidgetTypeElement.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="ApiKeyAuth"></a>
### ApiKeyAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header

<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication (JWT)


## Author

hello@eliona.io


