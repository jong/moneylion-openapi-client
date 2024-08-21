# RefinanceLoanInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_number** | **str** | The account number for a loan the lead is refinancing | [optional] 
**income_based_repayment** | **bool** | If the repayment is income-based for a loan the lead is refinancing | [optional] 
**interest_rate** | **float** | The interest rate for a loan the lead is refinancing | [optional] 
**loan_amount** | **int** | The loan amount for a loan the lead is refinancing | [optional] 
**loan_servicer** | **str** | The name of a loan servicer of a loan the lead is refinancing | [optional] 
**loan_type** | [**RefinanceLoanType**](RefinanceLoanType.md) |  | [optional] 
**next_payment_amount** | **float** | The amount the next payment will be on a loan the lead is refinancing | [optional] 
**next_payment_date** | **date** | The next payment date for a loan the lead is refinancing | [optional] 

## Example

```python
from openapi_client.models.refinance_loan_information import RefinanceLoanInformation

# TODO update the JSON string below
json = "{}"
# create an instance of RefinanceLoanInformation from a JSON string
refinance_loan_information_instance = RefinanceLoanInformation.from_json(json)
# print the JSON string representation of the object
print(RefinanceLoanInformation.to_json())

# convert the object into a dict
refinance_loan_information_dict = refinance_loan_information_instance.to_dict()
# create an instance of RefinanceLoanInformation from a dict
refinance_loan_information_from_dict = RefinanceLoanInformation.from_dict(refinance_loan_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


