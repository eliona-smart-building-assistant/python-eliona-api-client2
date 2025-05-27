# DataAggregated

Aggregated data combines multiple data points for a periodical raster

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregation_id** | **int** | ID of the aggregation | [optional] 
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**attribute** | **str** | Name of the attribute which holds the data points | [optional] 
**raster** | **str** | Calculation intervals. | 
**timestamp** | **datetime** | Timestamp of this aggregated data set. The timestamp when the timeslot based on raster starts. | [optional] 
**count** | **float** | Count of data points in this aggregated data set | [optional] 
**average** | **float** | Average of all data points for this aggregated data set | [optional] 
**sum** | **float** | Sum of all data points for this aggregated data set | [optional] 
**first** | **float** | First data point in this aggregated data set | [optional] 
**min** | **float** | Data point with the most minimal value in this aggregated data set | [optional] 
**max** | **float** | Data point with the most maximal value in this aggregated data set | [optional] 
**last** | **float** | Latest data point in this aggregated data set | [optional] 
**last_timestamp** | **datetime** | Timestamp of the latest data point | [optional] 
**asset_type_name** | **str** | The name of the corresponding asset type | [optional] [readonly] 

## Example

```python
from eliona.api_client2.models.data_aggregated import DataAggregated

# TODO update the JSON string below
json = "{}"
# create an instance of DataAggregated from a JSON string
data_aggregated_instance = DataAggregated.from_json(json)
# print the JSON string representation of the object
print(DataAggregated.to_json())

# convert the object into a dict
data_aggregated_dict = data_aggregated_instance.to_dict()
# create an instance of DataAggregated from a dict
data_aggregated_from_dict = DataAggregated.from_dict(data_aggregated_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


