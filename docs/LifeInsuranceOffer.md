# LifeInsuranceOffer

An offer for a life insurance lead

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**details** | [**LifeInsuranceOfferDetails**](LifeInsuranceOfferDetails.md) |  | 
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
from openapi_client.models.life_insurance_offer import LifeInsuranceOffer

# TODO update the JSON string below
json = "{}"
# create an instance of LifeInsuranceOffer from a JSON string
life_insurance_offer_instance = LifeInsuranceOffer.from_json(json)
# print the JSON string representation of the object
print(LifeInsuranceOffer.to_json())

# convert the object into a dict
life_insurance_offer_dict = life_insurance_offer_instance.to_dict()
# create an instance of LifeInsuranceOffer from a dict
life_insurance_offer_from_dict = LifeInsuranceOffer.from_dict(life_insurance_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


