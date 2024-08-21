# LeadCreditInformation

Credit history information relating to a `Lead`

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provided_credit_rating** | [**ProvidedCreditRating**](ProvidedCreditRating.md) |  | [optional] 
**provided_numeric_credit_score** | **int** | FICO credit score provided by a &#x60;Lead&#x60; | [optional] 

## Example

```python
from openapi_client.models.lead_credit_information import LeadCreditInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadCreditInformation from a JSON string
lead_credit_information_instance = LeadCreditInformation.from_json(json)
# print the JSON string representation of the object
print(LeadCreditInformation.to_json())

# convert the object into a dict
lead_credit_information_dict = lead_credit_information_instance.to_dict()
# create an instance of LeadCreditInformation from a dict
lead_credit_information_from_dict = LeadCreditInformation.from_dict(lead_credit_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


