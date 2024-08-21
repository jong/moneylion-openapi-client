# LeadEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**next_url** | **str** | The URL for the next request.  | 
**should_continue_polling** | **bool** | If true, data is currently available at &#x60;nextUrl&#x60;.    Calling the &#x60;nextUrl&#x60; at the current time will return the next batch of data.   If false, calling &#x60;nextUrl&#x60; at the current time will return an error response from the API.     Data will be made available at a later time (at the next hour mark).  | 
**data** | [**List[LeadEvent]**](LeadEvent.md) | Lead event data for the requested time window.  | 

## Example

```python
from openapi_client.models.lead_event_response import LeadEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of LeadEventResponse from a JSON string
lead_event_response_instance = LeadEventResponse.from_json(json)
# print the JSON string representation of the object
print(LeadEventResponse.to_json())

# convert the object into a dict
lead_event_response_dict = lead_event_response_instance.to_dict()
# create an instance of LeadEventResponse from a dict
lead_event_response_from_dict = LeadEventResponse.from_dict(lead_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


