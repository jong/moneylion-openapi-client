# LoanProbability


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**probability** | **float** | The likelihood of approval for loans that match the criteria. | 
**apr_percent_min** | **float** | The minimum APR for loans with this approval probability. | 
**apr_percent_max** | **float** | The maximum APR for loans with this approval probability. | 
**term_months_min** | **int** | The minimum term length for loans with this approval probability. | 
**term_months_max** | **int** | The maximum term length for loans with this approval probability. | 
**product_sub_type** | [**ProductSubType**](ProductSubType.md) | The optional loan sub-type of loans with this approval probability. | [optional] 

## Example

```python
from openapi_client.models.loan_probability import LoanProbability

# TODO update the JSON string below
json = "{}"
# create an instance of LoanProbability from a JSON string
loan_probability_instance = LoanProbability.from_json(json)
# print the JSON string representation of the object
print(LoanProbability.to_json())

# convert the object into a dict
loan_probability_dict = loan_probability_instance.to_dict()
# create an instance of LoanProbability from a dict
loan_probability_from_dict = LoanProbability.from_dict(loan_probability_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


