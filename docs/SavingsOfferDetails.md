# SavingsOfferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**details** | **str** |  | [optional] 
**rate** | **float** | Annual interest rate | [optional] 
**annual_percent_yield** | **float** |  | 
**compounding_method** | [**CompoundingMethod**](CompoundingMethod.md) |  | 
**introductory_period_months** | **int** |  | [optional] 
**introductory_rate** | **float** |  | [optional] 
**minimum_deposit** | **float** |  | 
**minimum_deposit_with_fees** | **float** |  | [optional] 
**monthly_fee** | **float** |  | 
**check_writing** | **bool** | Whether the account allows checks | [optional] 
**effective_as_of** | **datetime** | When the offer was last validated, formatted as yyyy-MM-ddTHH:mm:ss.SSSZZ | 
**federal_insurance_type** | [**FederalInsuranceType**](FederalInsuranceType.md) | The type of federal deposit insurance that applies to this offer, if it was provided by the financial institution. Could be one of &#x60;fdic&#x60; for the Federal Deposit Insurance Corporation, or &#x60;ncua&#x60; for the National Credit Union Administration.  | [optional] 
**incentive_details** | [**List[IncentiveDetails]**](IncentiveDetails.md) |  | [optional] 
**cd_term_unit** | [**TermUnit**](TermUnit.md) |  | [optional] 
**cd_term_length** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.savings_offer_details import SavingsOfferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of SavingsOfferDetails from a JSON string
savings_offer_details_instance = SavingsOfferDetails.from_json(json)
# print the JSON string representation of the object
print(SavingsOfferDetails.to_json())

# convert the object into a dict
savings_offer_details_dict = savings_offer_details_instance.to_dict()
# create an instance of SavingsOfferDetails from a dict
savings_offer_details_from_dict = SavingsOfferDetails.from_dict(savings_offer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


