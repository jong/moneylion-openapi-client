# ApiApprovedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_approved_event_data import ApiApprovedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiApprovedEventData from a JSON string
api_approved_event_data_instance = ApiApprovedEventData.from_json(json)
# print the JSON string representation of the object
print(ApiApprovedEventData.to_json())

# convert the object into a dict
api_approved_event_data_dict = api_approved_event_data_instance.to_dict()
# create an instance of ApiApprovedEventData from a dict
api_approved_event_data_from_dict = ApiApprovedEventData.from_dict(api_approved_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

