# EventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 
**reject_reason** | [**RejectReason**](RejectReason.md) |  | [optional] 
**amount** | **int** | The dollar amount of the offer that was listed.  | [optional] 
**payout_in_cents** | **int** | The number of cents paid out for the conversion event.  | [optional] 

## Example

```python
from openapi_client.models.event_data import EventData

# TODO update the JSON string below
json = "{}"
# create an instance of EventData from a JSON string
event_data_instance = EventData.from_json(json)
# print the JSON string representation of the object
print(EventData.to_json())

# convert the object into a dict
event_data_dict = event_data_instance.to_dict()
# create an instance of EventData from a dict
event_data_from_dict = EventData.from_dict(event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


