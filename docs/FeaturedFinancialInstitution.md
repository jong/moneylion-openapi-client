# FeaturedFinancialInstitution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uuid** | **str** | A unique identifier for the financial institution.  | [readonly] 
**name** | **str** | The name of the financial institution. This value is subject to change, so &#x60;financialInstitutionUuid&#x60; should be used for grouping.  | [readonly] 
**logo_url** | **str** | The URL of an image logo for the associated financial institution.  | [readonly] 

## Example

```python
from openapi_client.models.featured_financial_institution import FeaturedFinancialInstitution

# TODO update the JSON string below
json = "{}"
# create an instance of FeaturedFinancialInstitution from a JSON string
featured_financial_institution_instance = FeaturedFinancialInstitution.from_json(json)
# print the JSON string representation of the object
print(FeaturedFinancialInstitution.to_json())

# convert the object into a dict
featured_financial_institution_dict = featured_financial_institution_instance.to_dict()
# create an instance of FeaturedFinancialInstitution from a dict
featured_financial_institution_from_dict = FeaturedFinancialInstitution.from_dict(featured_financial_institution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


