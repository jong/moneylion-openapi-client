# openapi_client.OfferPreviewApi

All URIs are relative to *https://api.engine.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_preview_credit_card_offers**](OfferPreviewApi.md#get_preview_credit_card_offers) | **GET** /offerPreview/creditCardOffers | Get preview credit card offers
[**get_preview_loan_offers**](OfferPreviewApi.md#get_preview_loan_offers) | **GET** /offerPreview/loanOffers | Get preview loan offers
[**get_preview_savings_offers**](OfferPreviewApi.md#get_preview_savings_offers) | **GET** /offerPreview/savingsOffers | Get preview savings offers


# **get_preview_credit_card_offers**
> List[CreditCardOffer] get_preview_credit_card_offers(provided_credit_rating=provided_credit_rating, zip_code=zip_code, card_purposes=card_purposes)

Get preview credit card offers

Get a list of non-personalized credit card offers that match the specified critieria.

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.card_purpose import CardPurpose
from openapi_client.models.credit_card_offer import CreditCardOffer
from openapi_client.models.provided_credit_rating import ProvidedCreditRating
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.engine.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.engine.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: publishableBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OfferPreviewApi(api_client)
    provided_credit_rating = openapi_client.ProvidedCreditRating() # ProvidedCreditRating |  (optional)
    zip_code = 'zip_code_example' # str |  (optional)
    card_purposes = openapi_client.CardPurpose() # CardPurpose |  (optional)

    try:
        # Get preview credit card offers
        api_response = api_instance.get_preview_credit_card_offers(provided_credit_rating=provided_credit_rating, zip_code=zip_code, card_purposes=card_purposes)
        print("The response of OfferPreviewApi->get_preview_credit_card_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPreviewApi->get_preview_credit_card_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provided_credit_rating** | [**ProvidedCreditRating**](.md)|  | [optional] 
 **zip_code** | **str**|  | [optional] 
 **card_purposes** | [**CardPurpose**](.md)|  | [optional] 

### Return type

[**List[CreditCardOffer]**](CreditCardOffer.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_loan_offers**
> List[LoanOffer] get_preview_loan_offers(loan_amount=loan_amount, provided_credit_rating=provided_credit_rating, loan_purpose=loan_purpose, zip_code=zip_code)

Get preview loan offers

Get a list of non-personalized loan offers that match the specified critieria.

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.loan_offer import LoanOffer
from openapi_client.models.loan_purpose import LoanPurpose
from openapi_client.models.provided_credit_rating import ProvidedCreditRating
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.engine.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.engine.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: publishableBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OfferPreviewApi(api_client)
    loan_amount = 56 # int |  (optional)
    provided_credit_rating = openapi_client.ProvidedCreditRating() # ProvidedCreditRating |  (optional)
    loan_purpose = openapi_client.LoanPurpose() # LoanPurpose |  (optional)
    zip_code = 'zip_code_example' # str |  (optional)

    try:
        # Get preview loan offers
        api_response = api_instance.get_preview_loan_offers(loan_amount=loan_amount, provided_credit_rating=provided_credit_rating, loan_purpose=loan_purpose, zip_code=zip_code)
        print("The response of OfferPreviewApi->get_preview_loan_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPreviewApi->get_preview_loan_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_amount** | **int**|  | [optional] 
 **provided_credit_rating** | [**ProvidedCreditRating**](.md)|  | [optional] 
 **loan_purpose** | [**LoanPurpose**](.md)|  | [optional] 
 **zip_code** | **str**|  | [optional] 

### Return type

[**List[LoanOffer]**](LoanOffer.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_preview_savings_offers**
> List[SavingsOffer] get_preview_savings_offers(max_deposit_amount=max_deposit_amount, min_deposit_amount=min_deposit_amount, zip_code=zip_code)

Get preview savings offers

Get a list of non-personalized savings offers that match the specified critieria.

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.savings_offer import SavingsOffer
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.engine.tech
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://api.engine.tech"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: publishableBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.OfferPreviewApi(api_client)
    max_deposit_amount = 56 # int |  (optional)
    min_deposit_amount = 56 # int |  (optional)
    zip_code = 'zip_code_example' # str |  (optional)

    try:
        # Get preview savings offers
        api_response = api_instance.get_preview_savings_offers(max_deposit_amount=max_deposit_amount, min_deposit_amount=min_deposit_amount, zip_code=zip_code)
        print("The response of OfferPreviewApi->get_preview_savings_offers:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OfferPreviewApi->get_preview_savings_offers: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **max_deposit_amount** | **int**|  | [optional] 
 **min_deposit_amount** | **int**|  | [optional] 
 **zip_code** | **str**|  | [optional] 

### Return type

[**List[SavingsOffer]**](SavingsOffer.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**401** | Unauthorized request |  -  |
**404** | Resource not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

