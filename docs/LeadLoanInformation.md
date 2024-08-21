# LeadLoanInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**purpose** | [**LoanPurpose**](LoanPurpose.md) |  | [optional] 
**loan_amount** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.lead_loan_information import LeadLoanInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadLoanInformation from a JSON string
lead_loan_information_instance = LeadLoanInformation.from_json(json)
# print the JSON string representation of the object
print(LeadLoanInformation.to_json())

# convert the object into a dict
lead_loan_information_dict = lead_loan_information_instance.to_dict()
# create an instance of LeadLoanInformation from a dict
lead_loan_information_from_dict = LeadLoanInformation.from_dict(lead_loan_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


