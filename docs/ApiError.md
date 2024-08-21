# ApiError


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attribute** | **str** | The attribute that this error applies to. Omitted if this error is not in the context of a resource, or cannot be isolated to a single attribute.  | [optional] 
**type** | **str** | A classification for this error, which can be used to render the appropriate custom error template, or take other programmatic actions.  | [optional] 
**details** | **Dict[str, str]** | Variables associated with this error that can be injected into a custom error template, or used to parameterize any other programatic actions.  | [optional] 
**message** | **str** | A human-readable, English description of the error.  | [optional] 

## Example

```python
from openapi_client.models.api_error import ApiError

# TODO update the JSON string below
json = "{}"
# create an instance of ApiError from a JSON string
api_error_instance = ApiError.from_json(json)
# print the JSON string representation of the object
print(ApiError.to_json())

# convert the object into a dict
api_error_dict = api_error_instance.to_dict()
# create an instance of ApiError from a dict
api_error_from_dict = ApiError.from_dict(api_error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


