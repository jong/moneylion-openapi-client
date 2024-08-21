# ApiRejectedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reject_reason** | [**RejectReason**](RejectReason.md) |  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.api_rejected_event_data import ApiRejectedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of ApiRejectedEventData from a JSON string
api_rejected_event_data_instance = ApiRejectedEventData.from_json(json)
# print the JSON string representation of the object
print(ApiRejectedEventData.to_json())

# convert the object into a dict
api_rejected_event_data_dict = api_rejected_event_data_instance.to_dict()
# create an instance of ApiRejectedEventData from a dict
api_rejected_event_data_from_dict = ApiRejectedEventData.from_dict(api_rejected_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


