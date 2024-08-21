# LoanOffer


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**product_type** | [**ProductType**](ProductType.md) |  | 
**product_sub_type** | [**ProductSubType**](ProductSubType.md) |  | 
**product_sub_type_disclaimer** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**originator** | [**Originator**](Originator.md) |  | 
**originator_id** | **str** |  | [optional] 
**pre_qualified** | **bool** |  | 
**pre_approved** | **bool** |  | 
**secured** | **bool** |  | 
**co_applicant** | **bool** |  | 
**sponsored** | **bool** |  | 
**max_amount** | **int** |  | 
**min_amount** | **int** |  | [optional] 
**term_length** | **int** |  | [optional] 
**term_unit** | [**TermUnit**](TermUnit.md) |  | [optional] 
**display_term_unit** | **str** |  | [optional] 
**term_description** | **str** |  | [optional] 
**max_apr** | **float** |  | [optional] 
**min_apr** | **float** |  | [optional] 
**mean_apr** | **float** |  | [optional] 
**apr_type** | [**AprType**](AprType.md) |  | 
**apr_description** | **str** |  | [optional] 
**fee_rate** | **float** | The maximum percent of loan amount fee for an offer. &#x60;maxFeeRate&#x60; should be used instead | [optional] 
**max_fee_rate** | **float** |  | [optional] 
**min_fee_rate** | **float** |  | [optional] 
**fee_fixed** | **float** | The maximum fee, in dollars, for an offer. &#x60;maxFeeFixed&#x60; should be used instead | [optional] 
**max_fee_fixed** | **float** |  | [optional] 
**min_fee_fixed** | **float** |  | [optional] 
**allow_prepayment** | **bool** |  | 
**prepayment_fee** | **float** |  | [optional] 
**monthly_payment** | **float** | The estimated maximum monthly payment, in dollars, for an offer. &#x60;maxMonthlyPayment&#x60; should be used instead | [optional] 
**max_monthly_payment** | **float** |  | [optional] 
**min_monthly_payment** | **float** |  | [optional] 
**monthly_payment_description** | **str** |  | [optional] 
**mean_monthly_payment** | **float** |  | [optional] 
**max_total_payment** | **float** |  | [optional] 
**min_total_payment** | **float** |  | [optional] 
**mean_total_payment** | **float** |  | [optional] 
**recommendation_score** | **float** |  | [optional] 
**payout** | **float** |  | [optional] 
**conversion_probability** | **float** |  | [optional] 
**terms** | **str** |  | [optional] 
**amount_prefix** | **str** | Some loan offers require a prefix (e.g. &#x60;up to*&#x60;) to be displayed to the left of the displayed loan amount. This is a nullable field that may be up to six characters long. | [optional] 

## Example

```python
from openapi_client.models.loan_offer import LoanOffer

# TODO update the JSON string below
json = "{}"
# create an instance of LoanOffer from a JSON string
loan_offer_instance = LoanOffer.from_json(json)
# print the JSON string representation of the object
print(LoanOffer.to_json())

# convert the object into a dict
loan_offer_dict = loan_offer_instance.to_dict()
# create an instance of LoanOffer from a dict
loan_offer_from_dict = LoanOffer.from_dict(loan_offer_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


