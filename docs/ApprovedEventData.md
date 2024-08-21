# ApprovedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The dollar amount of the approved offer.  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.approved_event_data import ApprovedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of ApprovedEventData from a JSON string
approved_event_data_instance = ApprovedEventData.from_json(json)
# print the JSON string representation of the object
print(ApprovedEventData.to_json())

# convert the object into a dict
approved_event_data_dict = approved_event_data_instance.to_dict()
# create an instance of ApprovedEventData from a dict
approved_event_data_from_dict = ApprovedEventData.from_dict(approved_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


