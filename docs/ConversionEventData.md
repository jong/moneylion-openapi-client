# ConversionEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payout_in_cents** | **int** | The number of cents paid out for the conversion event.  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.conversion_event_data import ConversionEventData

# TODO update the JSON string below
json = "{}"
# create an instance of ConversionEventData from a JSON string
conversion_event_data_instance = ConversionEventData.from_json(json)
# print the JSON string representation of the object
print(ConversionEventData.to_json())

# convert the object into a dict
conversion_event_data_dict = conversion_event_data_instance.to_dict()
# create an instance of ConversionEventData from a dict
conversion_event_data_from_dict = ConversionEventData.from_dict(conversion_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


