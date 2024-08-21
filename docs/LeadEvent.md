# LeadEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A hash of the &#x60;leadUuid&#x60;, &#x60;eventType&#x60; and &#x60;eventCreatedAt&#x60; which uniquely identifies a leadEvent.  | 
**lead_uuid** | **str** | The unique identifier for the associated lead.  | 
**lead_created_at** | **datetime** | The time that the associated lead was created.  | 
**event_type** | [**EventType**](EventType.md) |  | 
**event_created_at** | **datetime** | The time that the event occurred.  | 
**event_data** | [**EventData**](EventData.md) |  | [optional] 
**amount_in_cents** | **int** | The amount of liquidity provided to the end user by the FI. Only present for some events.  | [optional] 
**financial_institution_uuid** | **str** | A unique identifier for the associated financial institution. Only present for event types associated with financial institutions.  | [optional] 
**financial_institution_name** | **str** | The name of the associated financial institution. This value is subject to change, so &#x60;financialInstitutionUuid&#x60; should be used as a stable identifier. Only present for event types associated with financial institutions.  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 
**is_test** | **bool** | Whether a &#x60;Lead&#x60; was created using a test access token | 

## Example

```python
from openapi_client.models.lead_event import LeadEvent

# TODO update the JSON string below
json = "{}"
# create an instance of LeadEvent from a JSON string
lead_event_instance = LeadEvent.from_json(json)
# print the JSON string representation of the object
print(LeadEvent.to_json())

# convert the object into a dict
lead_event_dict = lead_event_instance.to_dict()
# create an instance of LeadEvent from a dict
lead_event_from_dict = LeadEvent.from_dict(lead_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


