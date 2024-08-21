# SpecialOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**name** | **str** |  | 
**desc** | **str** | Description | 
**url** | **str** |  | 
**partner_name** | **str** |  | 
**partner_image_url** | **str** |  | 
**recommendation_score** | **float** |  | [optional] 
**payout** | **float** |  | [optional] 
**product_sub_type** | [**ProductSubType**](ProductSubType.md) |  | 
**disclaimer** | **str** |  | [optional] 
**financial_institution_uuid** | **str** | A unique identifier for the associated financial institution. Only present for event types associated with financial institutions.  | [optional] 

## Example

```python
from openapi_client.models.special_offer import SpecialOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SpecialOffer from a JSON string
special_offer_instance = SpecialOffer.from_json(json)
# print the JSON string representation of the object
print(SpecialOffer.to_json())

# convert the object into a dict
special_offer_dict = special_offer_instance.to_dict()
# create an instance of SpecialOffer from a dict
special_offer_from_dict = SpecialOffer.from_dict(special_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


