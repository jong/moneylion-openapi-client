# SessionInitCreateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**session_uuid** | **str** | You may specify the session&#39;s UUID; if you don&#39;t, one will be generated for you.  | [optional] 

## Example

```python
from openapi_client.models.session_init_create_data import SessionInitCreateData

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInitCreateData from a JSON string
session_init_create_data_instance = SessionInitCreateData.from_json(json)
# print the JSON string representation of the object
print(SessionInitCreateData.to_json())

# convert the object into a dict
session_init_create_data_dict = session_init_create_data_instance.to_dict()
# create an instance of SessionInitCreateData from a dict
session_init_create_data_from_dict = SessionInitCreateData.from_dict(session_init_create_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


