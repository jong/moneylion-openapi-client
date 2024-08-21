# Lead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_provider_name** | **str** | Name of company which provided the lead | 
**personal_information** | [**LeadPersonalInformation**](LeadPersonalInformation.md) |  | [optional] 
**personal_reference_information** | [**PersonalReferenceInformation**](PersonalReferenceInformation.md) |  | [optional] 
**loan_information** | [**LeadLoanInformation**](LeadLoanInformation.md) |  | [optional] 
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
**identification_information** | [**LeadIdentificationInformation**](LeadIdentificationInformation.md) |  | [optional] 
**auto_insurance_information** | [**LeadAutoInsuranceInformation**](LeadAutoInsuranceInformation.md) |  | [optional] 
**refinance_loans** | [**List[RefinanceLoanInformation]**](RefinanceLoanInformation.md) |  | [optional] 
**client_tags** | **Dict[str, List[str]]** | Arbitrary key-values mappings to associate with a &#x60;Lead&#x60;. This field can be use to attach &#x60;subid&#x60;s to a &#x60;Lead&#x60; | [optional] 
**session_information** | [**LeadSessionInformation**](LeadSessionInformation.md) |  | [optional] 
**lead_actions** | [**List[LeadAction]**](LeadAction.md) |  | [optional] 
**uuid** | **str** | Primary UUID for a &#x60;Lead&#x60; | 
**company_uuid** | **str** | UUID for a company which created the &#x60;Lead&#x60; | 
**session_uuid** | **str** | UUID used to link leads across verticals, unique per user per supply sub-account | [optional] 
**device_id** | **str** | Unique identifier for the lead&#39;s device. | [optional] 
**referral_company_uuid** | **str** |  | [optional] 
**tracking_uuid** | **str** |  | [optional] 
**is_test** | **bool** | Whether a &#x60;Lead&#x60; was created using a test access token | 
**status** | [**LeadActionType**](LeadActionType.md) | The furthest step of the funnel a &#x60;Lead&#x60; has reached | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 

## Example

```python
from openapi_client.models.lead import Lead

# TODO update the JSON string below
json = "{}"
# create an instance of Lead from a JSON string
lead_instance = Lead.from_json(json)
# print the JSON string representation of the object
print(Lead.to_json())

# convert the object into a dict
lead_dict = lead_instance.to_dict()
# create an instance of Lead from a dict
lead_from_dict = Lead.from_dict(lead_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


