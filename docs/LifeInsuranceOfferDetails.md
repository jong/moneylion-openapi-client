# LifeInsuranceOfferDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_amount** | **int** | Policy amount, in dollars | 
**term_length** | **int** |  | [optional] 
**term_unit** | [**TermUnit**](TermUnit.md) |  | [optional] 
**monthly_premium_amount** | **float** | Monthly premium amount, in dollars | 
**annual_premium_amount** | **float** | Annual premium amount, in dollars | [optional] 
**semi_annual_premium_amount** | **float** | Semi-annual premium amount, in dollars | [optional] 
**online_app_available** | **bool** | Online application is available | [optional] 
**no_medical_test** | **bool** |  | [optional] 
**package_type** | [**PackageType**](PackageType.md) |  | [optional] 
**recommended** | **bool** | Policy is recommended | [optional] 
**medical_exam** | [**MedicalExam**](MedicalExam.md) |  | [optional] 
**policy_name** | **str** | The name of policy | [optional] 
**carrier_decision_type** | [**CarrierDecisionType**](CarrierDecisionType.md) |  | [optional] 
**partner_quote_id** | **str** |  | [optional] 
**convert_to_permanent** | **bool** |  | [optional] 
**child_rider** | **str** |  | [optional] 
**accelerated_death_benefit** | **bool** |  | [optional] 
**waiver_of_premium** | **str** |  | [optional] 
**is_online_application** | **bool** |  | [optional] 
**delivery_method** | **str** |  | [optional] 
**exam_required** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.life_insurance_offer_details import LifeInsuranceOfferDetails

# TODO update the JSON string below
json = "{}"
# create an instance of LifeInsuranceOfferDetails from a JSON string
life_insurance_offer_details_instance = LifeInsuranceOfferDetails.from_json(json)
# print the JSON string representation of the object
print(LifeInsuranceOfferDetails.to_json())

# convert the object into a dict
life_insurance_offer_details_dict = life_insurance_offer_details_instance.to_dict()
# create an instance of LifeInsuranceOfferDetails from a dict
life_insurance_offer_details_from_dict = LifeInsuranceOfferDetails.from_dict(life_insurance_offer_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


