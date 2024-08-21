# OfferClickedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.offer_clicked_event_data import OfferClickedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of OfferClickedEventData from a JSON string
offer_clicked_event_data_instance = OfferClickedEventData.from_json(json)
# print the JSON string representation of the object
print(OfferClickedEventData.to_json())

# convert the object into a dict
offer_clicked_event_data_dict = offer_clicked_event_data_instance.to_dict()
# create an instance of OfferClickedEventData from a dict
offer_clicked_event_data_from_dict = OfferClickedEventData.from_dict(offer_clicked_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


