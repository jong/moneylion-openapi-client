# LeadAction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** |  | 
**action_type** | [**LeadActionType**](LeadActionType.md) |  | 
**action_date** | **datetime** |  | 
**originator_key** | **str** |  | [optional] 
**demand_sub_account_id** | **int** |  | 
**reject_reason** | [**RejectReason**](RejectReason.md) |  | [optional] 
**amount** | **int** |  | [optional] 
**origination_fee** | **int** |  | [optional] 
**offer_click_id** | **int** |  | [optional] 
**created_at** | **datetime** |  | 
**deleted_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.lead_action import LeadAction

# TODO update the JSON string below
json = "{}"
# create an instance of LeadAction from a JSON string
lead_action_instance = LeadAction.from_json(json)
# print the JSON string representation of the object
print(LeadAction.to_json())

# convert the object into a dict
lead_action_dict = lead_action_instance.to_dict()
# create an instance of LeadAction from a dict
lead_action_from_dict = LeadAction.from_dict(lead_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


