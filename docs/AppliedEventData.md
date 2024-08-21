# AppliedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The dollar amount of the offer that was applied for.  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.applied_event_data import AppliedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of AppliedEventData from a JSON string
applied_event_data_instance = AppliedEventData.from_json(json)
# print the JSON string representation of the object
print(AppliedEventData.to_json())

# convert the object into a dict
applied_event_data_dict = applied_event_data_instance.to_dict()
# create an instance of AppliedEventData from a dict
applied_event_data_from_dict = AppliedEventData.from_dict(applied_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


