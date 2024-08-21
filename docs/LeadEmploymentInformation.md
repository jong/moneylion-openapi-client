# LeadEmploymentInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**employer_name** | **str** |  | [optional] 
**employer_address** | **str** |  | [optional] 
**employer_address2** | **str** |  | [optional] 
**employer_city** | **str** |  | [optional] 
**employer_phone** | **str** |  | [optional] 
**employer_state** | **str** |  | [optional] 
**employer_zip** | **str** |  | [optional] 
**job_title** | **str** |  | [optional] 
**months_employed** | **int** |  | [optional] 
**direct_deposit** | **bool** | Whether a &#x60;Lead&#x60; uses direct deposit for their salary | [optional] 
**pay_date1** | **date** |  | [optional] 
**pay_date2** | **date** |  | [optional] 
**start_date** | **date** | The date the lead started working at their current employer (YYYY-MM-DD) | [optional] 

## Example

```python
from openapi_client.models.lead_employment_information import LeadEmploymentInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadEmploymentInformation from a JSON string
lead_employment_information_instance = LeadEmploymentInformation.from_json(json)
# print the JSON string representation of the object
print(LeadEmploymentInformation.to_json())

# convert the object into a dict
lead_employment_information_dict = lead_employment_information_instance.to_dict()
# create an instance of LeadEmploymentInformation from a dict
lead_employment_information_from_dict = LeadEmploymentInformation.from_dict(lead_employment_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


