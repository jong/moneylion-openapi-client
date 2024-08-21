# PersonalReferenceInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**first_name** | **str** | The first name of the personal reference supplied by the lead | [optional] 
**last_name** | **str** | The last name of the personal reference supplied by the lead | [optional] 
**primary_phone** | **str** | The phone number of the personal reference supplied by the lead | [optional] 
**relation_type** | [**PersonalReferenceRelationType**](PersonalReferenceRelationType.md) |  | [optional] 

## Example

```python
from openapi_client.models.personal_reference_information import PersonalReferenceInformation

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalReferenceInformation from a JSON string
personal_reference_information_instance = PersonalReferenceInformation.from_json(json)
# print the JSON string representation of the object
print(PersonalReferenceInformation.to_json())

# convert the object into a dict
personal_reference_information_dict = personal_reference_information_instance.to_dict()
# create an instance of PersonalReferenceInformation from a dict
personal_reference_information_from_dict = PersonalReferenceInformation.from_dict(personal_reference_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


