# LeadIdentificationInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id_number** | **str** | The ID number supplied by the lead | [optional] 
**id_state** | **str** | The state of issue of the supplied ID | [optional] 
**id_type** | [**IdType**](IdType.md) |  | [optional] 

## Example

```python
from openapi_client.models.lead_identification_information import LeadIdentificationInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadIdentificationInformation from a JSON string
lead_identification_information_instance = LeadIdentificationInformation.from_json(json)
# print the JSON string representation of the object
print(LeadIdentificationInformation.to_json())

# convert the object into a dict
lead_identification_information_dict = lead_identification_information_instance.to_dict()
# create an instance of LeadIdentificationInformation from a dict
lead_identification_information_from_dict = LeadIdentificationInformation.from_dict(lead_identification_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


