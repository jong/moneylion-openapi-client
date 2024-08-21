# FundedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The dollar amount of the offer that was funded.  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.funded_event_data import FundedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of FundedEventData from a JSON string
funded_event_data_instance = FundedEventData.from_json(json)
# print the JSON string representation of the object
print(FundedEventData.to_json())

# convert the object into a dict
funded_event_data_dict = funded_event_data_instance.to_dict()
# create an instance of FundedEventData from a dict
funded_event_data_from_dict = FundedEventData.from_dict(funded_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


