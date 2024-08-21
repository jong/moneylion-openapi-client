# SessionInit


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**uuid** | **str** |  | 
**session_uuid** | **str** |  | 
**created_at** | **datetime** |  | 
**created_by** | **str** |  | 

## Example

```python
from openapi_client.models.session_init import SessionInit

# TODO update the JSON string below
json = "{}"
# create an instance of SessionInit from a JSON string
session_init_instance = SessionInit.from_json(json)
# print the JSON string representation of the object
print(SessionInit.to_json())

# convert the object into a dict
session_init_dict = session_init_instance.to_dict()
# create an instance of SessionInit from a dict
session_init_from_dict = SessionInit.from_dict(session_init_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


