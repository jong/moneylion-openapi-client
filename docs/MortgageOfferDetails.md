# MortgageOfferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**interest_rate** | **float** |  | 
**loan_type** | [**MortgageLoanType**](MortgageLoanType.md) |  | 
**price_adjustment** | **float** |  | 
**monthly_payment** | **float** |  | 
**net_closing_costs** | **float** |  | 
**apr** | **float** |  | 
**loan_term** | **int** |  | 
**adjustment_type** | [**MortgageAdjustmentType**](MortgageAdjustmentType.md) |  | 

## Example

```python
from openapi_client.models.mortgage_offer_details import MortgageOfferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of MortgageOfferDetails from a JSON string
mortgage_offer_details_instance = MortgageOfferDetails.from_json(json)
# print the JSON string representation of the object
print(MortgageOfferDetails.to_json())

# convert the object into a dict
mortgage_offer_details_dict = mortgage_offer_details_instance.to_dict()
# create an instance of MortgageOfferDetails from a dict
mortgage_offer_details_from_dict = MortgageOfferDetails.from_dict(mortgage_offer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


