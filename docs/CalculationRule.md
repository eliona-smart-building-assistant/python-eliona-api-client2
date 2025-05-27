# CalculationRule

Calculation rule to calculate asset attribute data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | The id of the rule | [optional] [readonly] 
**asset_id** | **int** | ID of the corresponding asset | 
**subtype** | [**DataSubtype**](DataSubtype.md) |  | [default to DataSubtype.NUMBER_SUBTYPE_INPUT]
**attribute** | **str** | Name of the attribute of the asset type to be calculated | 
**virtual** | **bool** | Is the calculation attribute virtual or not | [optional] 
**formula** | **str** | calculation rule to calculate the value for the attribute | [optional] 
**unit** | **str** | Physical unit of calculated data | [optional] 
**filter** | **object** | Filter definition for calculation rule | [optional] 

## Example

```python
from eliona.api_client2.models.calculation_rule import CalculationRule

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationRule from a JSON string
calculation_rule_instance = CalculationRule.from_json(json)
# print the JSON string representation of the object
print(CalculationRule.to_json())

# convert the object into a dict
calculation_rule_dict = calculation_rule_instance.to_dict()
# create an instance of CalculationRule from a dict
calculation_rule_from_dict = CalculationRule.from_dict(calculation_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


