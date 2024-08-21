# LeadClientTagsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_url** | **str** | A URL which identifies where the next batch of LeadClientTags can be queried for.  | 
**should_continue_polling** | **bool** | If true, data is currently available at &#x60;nextUrl&#x60;.    Calling the &#x60;nextUrl&#x60; at the current time will return the next batch of data.   If false, calling &#x60;nextUrl&#x60; at the current time will return an error response from the API.     Data will be made available at a later time (at the next hour mark).  | 
**data** | [**List[LeadClientTag]**](LeadClientTag.md) | Lead client tag data for the requested time window.  | 

## Example

```python
from openapi_client.models.lead_client_tags_response import LeadClientTagsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeadClientTagsResponse from a JSON string
lead_client_tags_response_instance = LeadClientTagsResponse.from_json(json)
# print the JSON string representation of the object
print(LeadClientTagsResponse.to_json())

# convert the object into a dict
lead_client_tags_response_dict = lead_client_tags_response_instance.to_dict()
# create an instance of LeadClientTagsResponse from a dict
lead_client_tags_response_from_dict = LeadClientTagsResponse.from_dict(lead_client_tags_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


