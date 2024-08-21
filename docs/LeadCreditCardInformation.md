# LeadCreditCardInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_annual_fee** | **bool** |  | [optional] 
**card_purposes** | [**List[CardPurpose]**](CardPurpose.md) | A list of card purposes in which the lead is interested | [optional] 

## Example

```python
from openapi_client.models.lead_credit_card_information import LeadCreditCardInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadCreditCardInformation from a JSON string
lead_credit_card_information_instance = LeadCreditCardInformation.from_json(json)
# print the JSON string representation of the object
print(LeadCreditCardInformation.to_json())

# convert the object into a dict
lead_credit_card_information_dict = lead_credit_card_information_instance.to_dict()
# create an instance of LeadCreditCardInformation from a dict
lead_credit_card_information_from_dict = LeadCreditCardInformation.from_dict(lead_credit_card_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


