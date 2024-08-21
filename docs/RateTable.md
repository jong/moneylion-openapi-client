# RateTable

A `RateTable` customized to a `Lead` input

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | Primary UUID for a &#x60;RateTable&#x60; | 
**lead_uuid** | **str** | UUID of the associated &#x60;Lead&#x60; | 
**loan_amount** | **int** | &#x60;Lead&#x60;&#39;s provided loan amount at the time of &#x60;RateTable&#x60; creation | [optional] 
**embed_url** | **str** | A URL with which to build an iframe to embed rate table offer results in your experience. Only available to channels with integrations configured in control center. | [optional] 
**partner_page_url** | **str** | A partner page URL to send your user to see the rate table offer results. Only available to channels with integrations configured in control center. | [optional] 
**credit_card_offers** | [**List[CreditCardOffer]**](CreditCardOffer.md) |  | 
**loan_offers** | [**List[LoanOffer]**](LoanOffer.md) |  | 
**mortgage_offers** | [**List[MortgageOffer]**](MortgageOffer.md) |  | 
**savings_offers** | [**List[SavingsOffer]**](SavingsOffer.md) |  | 
**special_offers** | [**List[SpecialOffer]**](SpecialOffer.md) |  | 
**pending_originators** | [**List[Originator]**](Originator.md) | List of originators which have been queried, but have not responded yet. This list only contains loan originators, and should no longer be used | 
**pending_responses** | [**List[PendingResponse]**](PendingResponse.md) | List of demand partners which have been queried, but have not responded yet. It is a guarantee that no offers will be added to the rate table after this list is empty | 

## Example

```python
from openapi_client.models.rate_table import RateTable

# TODO update the JSON string below
json = "{}"
# create an instance of RateTable from a JSON string
rate_table_instance = RateTable.from_json(json)
# print the JSON string representation of the object
print(RateTable.to_json())

# convert the object into a dict
rate_table_dict = rate_table_instance.to_dict()
# create an instance of RateTable from a dict
rate_table_from_dict = RateTable.from_dict(rate_table_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


