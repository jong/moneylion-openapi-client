# Originator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**images** | [**List[OriginatorImage]**](OriginatorImage.md) |  | 
**disclaimer** | **str** |  | [optional] 
**company_uuid** | **str** |  | [optional] 
**financial_institution_uuid** | **str** | A unique identifier for the associated financial institution. Only present for event types associated with financial institutions.  | [optional] 

## Example

```python
from openapi_client.models.originator import Originator

# TODO update the JSON string below
json = "{}"
# create an instance of Originator from a JSON string
originator_instance = Originator.from_json(json)
# print the JSON string representation of the object
print(Originator.to_json())

# convert the object into a dict
originator_dict = originator_instance.to_dict()
# create an instance of Originator from a dict
originator_from_dict = Originator.from_dict(originator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


