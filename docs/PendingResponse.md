# PendingResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**partner** | [**Partner**](Partner.md) |  | 
**product_types** | [**List[ProductType]**](ProductType.md) |  | 

## Example

```python
from openapi_client.models.pending_response import PendingResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PendingResponse from a JSON string
pending_response_instance = PendingResponse.from_json(json)
# print the JSON string representation of the object
print(PendingResponse.to_json())

# convert the object into a dict
pending_response_dict = pending_response_instance.to_dict()
# create an instance of PendingResponse from a dict
pending_response_from_dict = PendingResponse.from_dict(pending_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


