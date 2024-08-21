# LeadSavingsInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_deposit_amount** | **int** | The minimum amount a &#x60;Lead&#x60; is interested in depositing when opening a new savings account | [optional] 
**max_deposit_amount** | **int** | The maximum amount a &#x60;Lead&#x60; is interested in depositing when opening a new savings account | [optional] 

## Example

```python
from openapi_client.models.lead_savings_information import LeadSavingsInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadSavingsInformation from a JSON string
lead_savings_information_instance = LeadSavingsInformation.from_json(json)
# print the JSON string representation of the object
print(LeadSavingsInformation.to_json())

# convert the object into a dict
lead_savings_information_dict = lead_savings_information_instance.to_dict()
# create an instance of LeadSavingsInformation from a dict
lead_savings_information_from_dict = LeadSavingsInformation.from_dict(lead_savings_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


