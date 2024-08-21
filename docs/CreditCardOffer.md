# CreditCardOffer

An offer for a credit card

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**CreditCardOfferDetails**](CreditCardOfferDetails.md) |  | 
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
from openapi_client.models.credit_card_offer import CreditCardOffer

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardOffer from a JSON string
credit_card_offer_instance = CreditCardOffer.from_json(json)
# print the JSON string representation of the object
print(CreditCardOffer.to_json())

# convert the object into a dict
credit_card_offer_dict = credit_card_offer_instance.to_dict()
# create an instance of CreditCardOffer from a dict
credit_card_offer_from_dict = CreditCardOffer.from_dict(credit_card_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


