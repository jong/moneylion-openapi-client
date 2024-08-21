# LeadFinancialInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employment_status** | [**EmploymentStatus**](EmploymentStatus.md) |  | [optional] 
**employment_pay_frequency** | [**EmploymentPayFrequency**](EmploymentPayFrequency.md) |  | [optional] 
**annual_income** | **int** |  | [optional] 
**monthly_net_income** | **int** |  | [optional] 
**bank_name** | **str** |  | [optional] 
**bank_routing_number** | **str** |  | [optional] 
**bank_account_type** | [**BankAccountType**](BankAccountType.md) |  | [optional] 
**credit_card_debt** | **int** |  | [optional] 
**months_at_bank** | **int** |  | [optional] 
**bank_account_number** | **str** |  | [optional] 
**monthly_debt** | **int** |  | [optional] 
**total_assets** | **int** |  | [optional] 
**monthly_housing_payment** | **int** |  | [optional] 
**available_assets** | **int** |  | [optional] 
**additional_income** | **int** | The amount of additional income the lead recieves | [optional] 
**additional_income_frequency** | [**EmploymentPayFrequency**](EmploymentPayFrequency.md) |  | [optional] 
**has_direct_deposit** | **bool** | Do you have a direct deposit? | [optional] 
**total_unsecured_debt** | **int** | Approximate total unsecured debt in dollars | [optional] 

## Example

```python
from openapi_client.models.lead_financial_information import LeadFinancialInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadFinancialInformation from a JSON string
lead_financial_information_instance = LeadFinancialInformation.from_json(json)
# print the JSON string representation of the object
print(LeadFinancialInformation.to_json())

# convert the object into a dict
lead_financial_information_dict = lead_financial_information_instance.to_dict()
# create an instance of LeadFinancialInformation from a dict
lead_financial_information_from_dict = LeadFinancialInformation.from_dict(lead_financial_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


