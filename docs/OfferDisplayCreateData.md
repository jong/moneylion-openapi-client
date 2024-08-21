# OfferDisplayCreateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_uuid** | **str** |  | 
**rate_table_uuid** | **str** |  | 
**offer_uuid** | **str** |  | 

## Example

```python
from openapi_client.models.offer_display_create_data import OfferDisplayCreateData

# TODO update the JSON string below
json = "{}"
# create an instance of OfferDisplayCreateData from a JSON string
offer_display_create_data_instance = OfferDisplayCreateData.from_json(json)
# print the JSON string representation of the object
print(OfferDisplayCreateData.to_json())

# convert the object into a dict
offer_display_create_data_dict = offer_display_create_data_instance.to_dict()
# create an instance of OfferDisplayCreateData from a dict
offer_display_create_data_from_dict = OfferDisplayCreateData.from_dict(offer_display_create_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


