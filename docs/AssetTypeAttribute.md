# AssetTypeAttribute

Named attribute to store data of assets

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asset_type_name** | **str** | The unique name for the asset type | [optional] 
**name** | **str** | Unique key of asset data | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**type** | **str** | Name of the type for this attribute: air_quality, battery-voltage, brightness, co2, current, device-info, device-status, energy, flow, frequency, humidity, inputs-and-switches, level, motion, operating-status, people-count, power, presence, pressure, temperature, vehicle-detector, voltage, weather, voc | [optional] 
**enable** | **bool** | Is data active or not | [optional] [default to False]
**translation** | [**Translation**](Translation.md) |  | [optional] 
**unit** | **str** | Physical unit of numeric data | [optional] 
**precision** | **int** | Number of decimal places | [optional] 
**min** | **float** | Lower limit | [optional] 
**max** | **float** | Upper limit | [optional] 
**aggregation_mode** | **str** | Deprecated: Use the &#39;GET /data-trend-aggregated&#39; endpoint to retrieve aggregated data for periodic rasters without defining aggregations. Aggregation calculation mode.  | [optional] 
**aggregation_rasters** | **List[str]** |  | [optional] 
**viewer** | **bool** | Should the attribute be displayed in viewer | [optional] [default to False]
**ar** | **bool** | Should the attribute be displayed in AR | [optional] [default to False]
**sequence** | **int** | Sequence in AR display | [optional] 
**virtual** | **bool** | Is the attribute virtual or not | [optional] 
**formula** | **str** | calculation rule to calculate the value for this attribute | [optional] 
**scale** | **float** | value scale | [optional] 
**zero** | **float** | value scale | [optional] 
**map** | **List[object]** | list of mapping between value and custom text | [optional] 
**source_path** | **List[str]** | source path for attribute value | [optional] 
**is_digital** | **bool** | is attribute digital | [optional] 

## Example

```python
from eliona.api_client2.models.asset_type_attribute import AssetTypeAttribute

# TODO update the JSON string below
json = "{}"
# create an instance of AssetTypeAttribute from a JSON string
asset_type_attribute_instance = AssetTypeAttribute.from_json(json)
# print the JSON string representation of the object
print(AssetTypeAttribute.to_json())

# convert the object into a dict
asset_type_attribute_dict = asset_type_attribute_instance.to_dict()
# create an instance of AssetTypeAttribute from a dict
asset_type_attribute_from_dict = AssetTypeAttribute.from_dict(asset_type_attribute_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


