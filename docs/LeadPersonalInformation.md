# LeadPersonalInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** |  | [optional] 
**last_name** | **str** |  | [optional] 
**alias_first_name** | **str** | The first name the lead uses as an alias | [optional] 
**alias_last_name** | **str** | The last name the lead uses as an alias | [optional] 
**email** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**work_phone** | **str** |  | [optional] 
**primary_phone** | **str** |  | [optional] 
**best_time_to_call** | [**LeadBestTimeToCall**](LeadBestTimeToCall.md) |  | [optional] 
**address1** | **str** | Street address (primary address line) | [optional] 
**address2** | **str** | Secondary address line | [optional] 
**address_move_in_date** | **date** | The date the lead moved into their current address | [optional] 
**zipcode** | **str** |  | [optional] 
**months_at_address** | **int** | Number of months the provided address has been the lead&#39;s primary residence | [optional] 
**drivers_license_number** | **str** |  | [optional] 
**drivers_license_state** | **str** | State in which the driver&#39;s license was issued | [optional] 
**ip_address** | **str** | IP address | [optional] 
**active_military** | **bool** | Whether the lead is currently in the military (not a veteran) | [optional] 
**military_veteran** | **bool** | Whether the lead is a veteran (should not be used if the lead is active in the military) | [optional] 
**date_of_birth** | **date** |  | [optional] 
**education_level** | [**EducationLevel**](EducationLevel.md) |  | [optional] 
**ssn** | **str** |  | [optional] 
**citizenship_status** | [**CitizenshipStatus**](CitizenshipStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.lead_personal_information import LeadPersonalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadPersonalInformation from a JSON string
lead_personal_information_instance = LeadPersonalInformation.from_json(json)
# print the JSON string representation of the object
print(LeadPersonalInformation.to_json())

# convert the object into a dict
lead_personal_information_dict = lead_personal_information_instance.to_dict()
# create an instance of LeadPersonalInformation from a dict
lead_personal_information_from_dict = LeadPersonalInformation.from_dict(lead_personal_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


