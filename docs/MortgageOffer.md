# MortgageOffer

An offer for a mortgage

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**MortgageOfferDetails**](MortgageOfferDetails.md) |  | 
**uuid** | **str** |  | 
**partner** | [**Partner**](Partner.md) |  | 
**marketplace** | [**Partner**](Partner.md) |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | 
**product_sub_type** | [**ProductSubType**](ProductSubType.md) |  | 
**url** | **str** |  | 
**recommendation_score** | **float** |  | [optional] 
**disclaimer** | **str** |  | [optional] 
**product_sub_type_disclaimer** | **str** |  | [optional] 
**expires_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.mortgage_offer import MortgageOffer

# TODO update the JSON string below
json = "{}"
# create an instance of MortgageOffer from a JSON string
mortgage_offer_instance = MortgageOffer.from_json(json)
# print the JSON string representation of the object
print(MortgageOffer.to_json())

# convert the object into a dict
mortgage_offer_dict = mortgage_offer_instance.to_dict()
# create an instance of MortgageOffer from a dict
mortgage_offer_from_dict = MortgageOffer.from_dict(mortgage_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


