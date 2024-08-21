# LoanReportCreateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**annual_income** | **int** | The user&#39;s annual income in dollars. | 
**credit_rating** | [**ProvidedCreditRating**](ProvidedCreditRating.md) | The user&#39;s credit score range. | 
**total_debt** | **int** | The user&#39;s total debt in dollars. | [optional] 
**count_of_derogatories** | **int** | The number of derogatory accounts listed on the user&#39;s credit report. | [optional] 
**state** | [**State**](State.md) | The user&#39;s state of residence. | [optional] 
**loan_purpose** | [**LoanPurpose**](LoanPurpose.md) | The reason for the loan. | [optional] 
**loan_amount** | **int** | The size of the the loan. | [optional] 

## Example

```python
from openapi_client.models.loan_report_create_data import LoanReportCreateData

# TODO update the JSON string below
json = "{}"
# create an instance of LoanReportCreateData from a JSON string
loan_report_create_data_instance = LoanReportCreateData.from_json(json)
# print the JSON string representation of the object
print(LoanReportCreateData.to_json())

# convert the object into a dict
loan_report_create_data_dict = loan_report_create_data_instance.to_dict()
# create an instance of LoanReportCreateData from a dict
loan_report_create_data_from_dict = LoanReportCreateData.from_dict(loan_report_create_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


