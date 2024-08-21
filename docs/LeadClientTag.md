# LeadClientTag


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash** | **str** | A unique hash for the client tag to assist with deduplication.  | 
**lead_uuid** | **str** | The UUID of the lead that this client tag belongs to.  | 
**key** | **str** | The key of this client tag.  | 
**value** | **str** | The latest value for the client tag key.  | 
**created_at** | **datetime** | The time that this client tag was added to the lead.  | 

## Example

```python
from openapi_client.models.lead_client_tag import LeadClientTag

# TODO update the JSON string below
json = "{}"
# create an instance of LeadClientTag from a JSON string
lead_client_tag_instance = LeadClientTag.from_json(json)
# print the JSON string representation of the object
print(LeadClientTag.to_json())

# convert the object into a dict
lead_client_tag_dict = lead_client_tag_instance.to_dict()
# create an instance of LeadClientTag from a dict
lead_client_tag_from_dict = LeadClientTag.from_dict(lead_client_tag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


