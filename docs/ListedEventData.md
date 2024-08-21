# ListedEventData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The dollar amount of the offer that was listed.  | [optional] 
**product_type** | [**ProductType**](ProductType.md) |  | [optional] 

## Example

```python
from openapi_client.models.listed_event_data import ListedEventData

# TODO update the JSON string below
json = "{}"
# create an instance of ListedEventData from a JSON string
listed_event_data_instance = ListedEventData.from_json(json)
# print the JSON string representation of the object
print(ListedEventData.to_json())

# convert the object into a dict
listed_event_data_dict = listed_event_data_instance.to_dict()
# create an instance of ListedEventData from a dict
listed_event_data_from_dict = ListedEventData.from_dict(listed_event_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


