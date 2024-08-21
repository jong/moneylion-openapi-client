# CreditCardOfferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**card_name** | **str** | Display name of the card | [optional] 
**card_image_url** | **str** |  | 
**card_purposes** | [**List[CardPurpose]**](CardPurpose.md) |  | [optional] 
**rates_url** | **str** | External link to card rates, terms and conditions | [optional] 
**max_purchase_apr** | **float** |  | [optional] 
**min_purchase_apr** | **float** |  | [optional] 
**purchase_apr_text** | **str** |  | [optional] 
**max_purchase_intro_apr** | **float** |  | [optional] 
**min_purchase_intro_apr** | **float** |  | [optional] 
**purchase_intro_apr_term** | **int** |  | [optional] 
**purchase_intro_apr_term_unit** | [**TermUnit**](TermUnit.md) |  | [optional] 
**purchase_intro_apr_text** | **str** |  | [optional] 
**max_cash_advance_apr** | **float** |  | [optional] 
**min_cash_advance_apr** | **float** |  | [optional] 
**cash_advance_apr_text** | **str** |  | [optional] 
**max_cash_advance_intro_apr** | **float** |  | [optional] 
**min_cash_advance_intro_apr** | **float** |  | [optional] 
**cash_advance_intro_apr_term** | **int** |  | [optional] 
**cash_advance_intro_apr_term_unit** | [**TermUnit**](TermUnit.md) |  | [optional] 
**cash_advance_intro_apr_text** | **str** |  | [optional] 
**max_balance_transfer_apr** | **float** |  | [optional] 
**min_balance_transfer_apr** | **float** |  | [optional] 
**balance_transfer_apr_text** | **str** |  | [optional] 
**max_balance_transfer_intro_apr** | **float** |  | [optional] 
**min_balance_transfer_intro_apr** | **float** |  | [optional] 
**balance_transfer_intro_apr_term** | **int** |  | [optional] 
**balance_transfer_intro_apr_term_unit** | [**TermUnit**](TermUnit.md) |  | [optional] 
**balance_transfer_intro_apr_text** | **str** |  | [optional] 
**max_annual_fee** | **float** |  | [optional] 
**min_annual_fee** | **float** |  | [optional] 
**annual_intro_fee** | **float** |  | [optional] 
**annual_intro_fee_term** | **int** | Number of _years_ the introductory anual fee is in effect | [optional] 
**intro_offer_amount** | **float** |  | [optional] 
**intro_offer_text** | **str** |  | [optional] 
**intro_offer_type** | [**IntroOfferType**](IntroOfferType.md) |  | [optional] 
**details** | **List[str]** | List of card features which must be prominently displayed with the offer | [optional] 
**additional_details** | **List[str]** | List of card features which must be displayed with the offer | [optional] 
**card_type** | [**CardType**](CardType.md) |  | 
**minimum_credit_line** | **float** |  | [optional] 
**minimum_penalty_apr** | **float** |  | [optional] 
**maximum_penalty_apr** | **float** |  | [optional] 
**balance_transfer_fee** | **float** |  | [optional] 
**cash_advance_fee** | **float** |  | [optional] 
**late_fee** | **float** |  | [optional] 
**foreign_exchange_fee** | **float** |  | [optional] 
**account_opening_fee** | **float** |  | [optional] 
**return_payment_fee** | **float** |  | [optional] 
**monthly_service_fee** | **float** |  | [optional] 
**recommended_credit_ratings** | [**List[ProvidedCreditRating]**](ProvidedCreditRating.md) |  | [optional] 
**pre_qualified** | **bool** |  | 
**pre_approved** | **bool** |  | 
**pre_selected** | **bool** | Indicates that Engine by MoneyLion has determined that the user has an increased likelihood of being approved for this card. | 
**foreign_transaction_fee** | **float** | Percentage represented in decimal format added to all foreign transactions | [optional] 
**card_benefits** | [**List[CardBenefit]**](CardBenefit.md) |  | [optional] 

## Example

```python
from openapi_client.models.credit_card_offer_details import CreditCardOfferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CreditCardOfferDetails from a JSON string
credit_card_offer_details_instance = CreditCardOfferDetails.from_json(json)
# print the JSON string representation of the object
print(CreditCardOfferDetails.to_json())

# convert the object into a dict
credit_card_offer_details_dict = credit_card_offer_details_instance.to_dict()
# create an instance of CreditCardOfferDetails from a dict
credit_card_offer_details_from_dict = CreditCardOfferDetails.from_dict(credit_card_offer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


