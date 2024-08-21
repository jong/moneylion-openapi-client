# LoanReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | A unique identifier for this report. | 
**annual_income** | **int** | The user&#39;s annual income in dollars. | 
**credit_rating** | [**ProvidedCreditRating**](ProvidedCreditRating.md) | The user&#39;s credit score range. | 
**total_debt** | **int** | The user&#39;s total debt in dollars. | [optional] 
**count_of_derogatories** | **int** | The number of derogatory accounts listed on the user&#39;s credit report. | [optional] 
**state** | [**State**](State.md) | The user&#39;s state of residence. | [optional] 
**loan_purpose** | [**LoanPurpose**](LoanPurpose.md) | The reason for the loan. | [optional] 
**loan_amount** | **int** | The size of the the loan. | [optional] 
**network_probabilities** | [**List[LoanProbability]**](LoanProbability.md) | Probabilities for classes of loans, irrespective of financial institution. | 
**financial_insitutions** | [**List[FinancialInstitutionLoanReport]**](FinancialInstitutionLoanReport.md) | Probabilities broken out for specific financial institutions. | 
**created_at** | **datetime** | When this report was created. | 

## Example

```python
from openapi_client.models.loan_report import LoanReport

# TODO update the JSON string below
json = "{}"
# create an instance of LoanReport from a JSON string
loan_report_instance = LoanReport.from_json(json)
# print the JSON string representation of the object
print(LoanReport.to_json())

# convert the object into a dict
loan_report_dict = loan_report_instance.to_dict()
# create an instance of LoanReport from a dict
loan_report_from_dict = LoanReport.from_dict(loan_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


