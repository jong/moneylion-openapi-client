# LeadCoApplicantInformation

The personal information of a co-applicant that may be considered in the underwriting and approval of a loan. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**date_of_birth** | **date** |  | [optional] 
**annual_income** | **int** |  | [optional] 
**street_address1** | **str** | Street address (primary address line) | [optional] 
**street_address2** | **str** | Secondary address line | [optional] 
**city** | **str** |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**zipcode** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.lead_co_applicant_information import LeadCoApplicantInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadCoApplicantInformation from a JSON string
lead_co_applicant_information_instance = LeadCoApplicantInformation.from_json(json)
# print the JSON string representation of the object
print(LeadCoApplicantInformation.to_json())

# convert the object into a dict
lead_co_applicant_information_dict = lead_co_applicant_information_instance.to_dict()
# create an instance of LeadCoApplicantInformation from a dict
lead_co_applicant_information_from_dict = LeadCoApplicantInformation.from_dict(lead_co_applicant_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


