# LeadLegalInformation

Information regarding a `Lead`'s communication concent

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consents_to_fcra** | **bool** | Whether the lead was shown, and consented to a Fair Credit Reporting Act notice | [optional] 
**consents_to_sms** | **bool** | The lead agrees to recieve SMS text messages from the Financial Institution | [optional] 
**consents_to_tcpa** | **bool** | Whether the lead was shown, and consented to a Telephone Consumer Protection Act notice | [optional] 
**fcra_language** | **str** | The exact FCRA language to which the lead consented | [optional] 
**tcpa_language** | **str** | The exact TCPA language to which the lead consented | [optional] 

## Example

```python
from openapi_client.models.lead_legal_information import LeadLegalInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadLegalInformation from a JSON string
lead_legal_information_instance = LeadLegalInformation.from_json(json)
# print the JSON string representation of the object
print(LeadLegalInformation.to_json())

# convert the object into a dict
lead_legal_information_dict = lead_legal_information_instance.to_dict()
# create an instance of LeadLegalInformation from a dict
lead_legal_information_from_dict = LeadLegalInformation.from_dict(lead_legal_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


