# LeadHealthInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gender** | [**Gender**](Gender.md) |  | [optional] 
**height_in_inches** | **int** |  | [optional] 
**weight_in_pounds** | **int** |  | [optional] 
**tobacco_smoker** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.lead_health_information import LeadHealthInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadHealthInformation from a JSON string
lead_health_information_instance = LeadHealthInformation.from_json(json)
# print the JSON string representation of the object
print(LeadHealthInformation.to_json())

# convert the object into a dict
lead_health_information_dict = lead_health_information_instance.to_dict()
# create an instance of LeadHealthInformation from a dict
lead_health_information_from_dict = LeadHealthInformation.from_dict(lead_health_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


