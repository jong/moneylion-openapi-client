# LeadCreateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_types** | [**List[ProductType]**](ProductType.md) | Product types in which the &#x60;Lead&#x60; is interested | [optional] 
**uuid** | **str** | Primary UUID for a &#x60;Lead&#x60; | [optional] 
**session_uuid** | **str** | UUID used to link leads across verticals, unique per user per supply sub-account | [optional] 
**device_id** | **str** | Unique identifier for the lead&#39;s device. | [optional] 
**loan_information** | [**LeadLoanInformation**](LeadLoanInformation.md) |  | [optional] 
**personal_information** | [**LeadPersonalInformation**](LeadPersonalInformation.md) |  | [optional] 
**personal_reference_information** | [**PersonalReferenceInformation**](PersonalReferenceInformation.md) |  | [optional] 
**mortgage_information** | [**LeadMortgageInformation**](LeadMortgageInformation.md) |  | [optional] 
**credit_card_information** | [**LeadCreditCardInformation**](LeadCreditCardInformation.md) |  | [optional] 
**savings_information** | [**LeadSavingsInformation**](LeadSavingsInformation.md) |  | [optional] 
**credit_information** | [**LeadCreditInformation**](LeadCreditInformation.md) |  | [optional] 
**financial_information** | [**LeadFinancialInformation**](LeadFinancialInformation.md) |  | [optional] 
**employment_information** | [**LeadEmploymentInformation**](LeadEmploymentInformation.md) |  | [optional] 
**legal_information** | [**LeadLegalInformation**](LeadLegalInformation.md) |  | [optional] 
**education_information** | [**LeadEducationInformation**](LeadEducationInformation.md) |  | [optional] 
**co_applicant_information** | [**LeadCoApplicantInformation**](LeadCoApplicantInformation.md) |  | [optional] 
**health_information** | [**LeadHealthInformation**](LeadHealthInformation.md) |  | [optional] 
**auto_insurance_information** | [**LeadAutoInsuranceInformation**](LeadAutoInsuranceInformation.md) |  | [optional] 
**refinance_loans** | [**List[RefinanceLoanInformation]**](RefinanceLoanInformation.md) | One or more loans that the lead wishes to refinance or consolidate | [optional] 
**identification_information** | [**LeadIdentificationInformation**](LeadIdentificationInformation.md) |  | [optional] 
**client_tags** | **Dict[str, List[str]]** | Arbitrary key-values mappings to associate with a &#x60;Lead&#x60;. This field can be use to attach &#x60;subid&#x60;s to a &#x60;Lead&#x60; | [optional] 
**session_information** | [**LeadSessionInformation**](LeadSessionInformation.md) |  | [optional] 
**form_completed** | **bool** | Whether the &#x60;Lead&#x60; has completed an application form | [optional] 
**referral_company_uuid** | **str** | UUID of company from which the &#x60;Lead&#x60; was referred | [optional] 
**tracking_uuid** | **str** | UUID for internal Engine by MoneyLion tracking purposes. This field should never be set by 3rd party API consumers | [optional] 

## Example

```python
from openapi_client.models.lead_create_data import LeadCreateData

# TODO update the JSON string below
json = "{}"
# create an instance of LeadCreateData from a JSON string
lead_create_data_instance = LeadCreateData.from_json(json)
# print the JSON string representation of the object
print(LeadCreateData.to_json())

# convert the object into a dict
lead_create_data_dict = lead_create_data_instance.to_dict()
# create an instance of LeadCreateData from a dict
lead_create_data_from_dict = LeadCreateData.from_dict(lead_create_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


