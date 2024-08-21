# FinancialInstitutionLoanReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | The unique identifier for the financial institution. | 
**name** | **str** | The name of the financial institution. | 
**logo_url** | **str** | A URL of a logo for the financial institution. | [optional] 
**probabilities** | [**List[LoanProbability]**](LoanProbability.md) | The approval probabilities for the financial intitution. | 

## Example

```python
from openapi_client.models.financial_institution_loan_report import FinancialInstitutionLoanReport

# TODO update the JSON string below
json = "{}"
# create an instance of FinancialInstitutionLoanReport from a JSON string
financial_institution_loan_report_instance = FinancialInstitutionLoanReport.from_json(json)
# print the JSON string representation of the object
print(FinancialInstitutionLoanReport.to_json())

# convert the object into a dict
financial_institution_loan_report_dict = financial_institution_loan_report_instance.to_dict()
# create an instance of FinancialInstitutionLoanReport from a dict
financial_institution_loan_report_from_dict = FinancialInstitutionLoanReport.from_dict(financial_institution_loan_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


