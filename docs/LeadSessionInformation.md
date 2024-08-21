# LeadSessionInformation

Browsing session information accociated with a `Lead`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip_address** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 
**browser_fingerprint** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.lead_session_information import LeadSessionInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadSessionInformation from a JSON string
lead_session_information_instance = LeadSessionInformation.from_json(json)
# print the JSON string representation of the object
print(LeadSessionInformation.to_json())

# convert the object into a dict
lead_session_information_dict = lead_session_information_instance.to_dict()
# create an instance of LeadSessionInformation from a dict
lead_session_information_from_dict = LeadSessionInformation.from_dict(lead_session_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


