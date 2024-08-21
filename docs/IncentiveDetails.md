# IncentiveDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **float** |  | 
**unit** | [**IncentiveUnit**](IncentiveUnit.md) |  | 
**display** | **str** |  | 
**type** | [**IncentiveType**](IncentiveType.md) |  | 

## Example

```python
from openapi_client.models.incentive_details import IncentiveDetails

# TODO update the JSON string below
json = "{}"
# create an instance of IncentiveDetails from a JSON string
incentive_details_instance = IncentiveDetails.from_json(json)
# print the JSON string representation of the object
print(IncentiveDetails.to_json())

# convert the object into a dict
incentive_details_dict = incentive_details_instance.to_dict()
# create an instance of IncentiveDetails from a dict
incentive_details_from_dict = IncentiveDetails.from_dict(incentive_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


