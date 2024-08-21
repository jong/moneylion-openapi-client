# SavingsOffer

An offer for a savings account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**SavingsOfferDetails**](SavingsOfferDetails.md) |  | 
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
from openapi_client.models.savings_offer import SavingsOffer

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsOffer from a JSON string
savings_offer_instance = SavingsOffer.from_json(json)
# print the JSON string representation of the object
print(SavingsOffer.to_json())

# convert the object into a dict
savings_offer_dict = savings_offer_instance.to_dict()
# create an instance of SavingsOffer from a dict
savings_offer_from_dict = SavingsOffer.from_dict(savings_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


