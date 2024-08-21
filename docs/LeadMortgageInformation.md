# LeadMortgageInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_type** | [**PropertyType**](PropertyType.md) |  | [optional] 
**property_value** | **int** |  | [optional] 
**mortgage_balance** | **int** |  | [optional] 
**lender_name** | **str** |  | [optional] 
**has_fha_loan** | **bool** |  | [optional] 
**current_with_loan** | **bool** |  | [optional] 
**property_status** | [**PropertyStatus**](PropertyStatus.md) |  | [optional] 
**mortgage_type** | [**MortgageType**](MortgageType.md) |  | [optional] 
**mortgage_amount** | **int** | Amount the lead will borrow | [optional] 
**down_payment_amount** | **int** |  | [optional] 
**property_state** | **str** |  | [optional] 
**property_county** | **str** |  | [optional] 
**property_address1** | **str** | Street address (primary address line) | [optional] 
**property_address2** | **str** | Secondary address line | [optional] 
**property_zipcode** | **str** |  | [optional] 
**property_city** | **str** |  | [optional] 
**refinance_amount** | **int** | Amount the lead will borrow for refinancing an existing mortgage | [optional] 
**cash_out_amount** | **int** | Additional amount the lead will borrow against existing home equity in the case of refinance | [optional] 
**occupancy_type** | [**OccupancyType**](OccupancyType.md) |  | [optional] 
**refinance_type** | [**RefinanceType**](RefinanceType.md) |  | [optional] 
**property_search_status** | [**PropertySearchStatus**](PropertySearchStatus.md) |  | [optional] 
**num_units** | **int** | The number of legal units on the property | [optional] 
**closing_date** | **date** |  | [optional] 
**purchase_status** | [**PurchaseStatus**](PurchaseStatus.md) |  | [optional] 
**purchase_date** | **date** |  | [optional] 
**monthly_hoa_fee** | **float** | The amount of the HOA fee for the lead | [optional] 
**mortgage_company** | **str** | The name of the company holding the lead&#39;s mortgage | [optional] 
**mortgage_escrow_amount** | **float** | The amount of escrow the lead pays | [optional] 

## Example

```python
from openapi_client.models.lead_mortgage_information import LeadMortgageInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadMortgageInformation from a JSON string
lead_mortgage_information_instance = LeadMortgageInformation.from_json(json)
# print the JSON string representation of the object
print(LeadMortgageInformation.to_json())

# convert the object into a dict
lead_mortgage_information_dict = lead_mortgage_information_instance.to_dict()
# create an instance of LeadMortgageInformation from a dict
lead_mortgage_information_from_dict = LeadMortgageInformation.from_dict(lead_mortgage_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


