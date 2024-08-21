# LeadAutoInsuranceInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number_of_vehicles** | **int** |  | [optional] 
**has_auto_insurance** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.lead_auto_insurance_information import LeadAutoInsuranceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadAutoInsuranceInformation from a JSON string
lead_auto_insurance_information_instance = LeadAutoInsuranceInformation.from_json(json)
# print the JSON string representation of the object
print(LeadAutoInsuranceInformation.to_json())

# convert the object into a dict
lead_auto_insurance_information_dict = lead_auto_insurance_information_instance.to_dict()
# create an instance of LeadAutoInsuranceInformation from a dict
lead_auto_insurance_information_from_dict = LeadAutoInsuranceInformation.from_dict(lead_auto_insurance_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


