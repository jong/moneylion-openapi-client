# LeadPayout


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lead_uuid** | **str** | The unique identifier for the associated lead.  | 
**booked_at** | **datetime** | The time that this payout to a supply partner was booked.  | 
**payout_in_cents** | **float** | The payout amount in cents made available to the supply partner. May be fractional.  | [optional] 
**uuid** | **str** | The unique identifier for the associated payout event.  | [optional] 
**deleted_at** | **datetime** | If a payout to a supply partner was revoked, this value will report the time that the payout was revoked.  | [optional] 
**financial_institution_name** | **str** | The name of the associated financial institution. This value is subject to change, so &#x60;financialInstitutionUuid&#x60; should be used as a stable identifier.  | [optional] 
**financial_institution_uuid** | **str** | A unique identifier for the associated financial institution. Only present for event types associated with financial institutions.  | [optional] 

## Example

```python
from openapi_client.models.lead_payout import LeadPayout

# TODO update the JSON string below
json = "{}"
# create an instance of LeadPayout from a JSON string
lead_payout_instance = LeadPayout.from_json(json)
# print the JSON string representation of the object
print(LeadPayout.to_json())

# convert the object into a dict
lead_payout_dict = lead_payout_instance.to_dict()
# create an instance of LeadPayout from a dict
lead_payout_from_dict = LeadPayout.from_dict(lead_payout_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


