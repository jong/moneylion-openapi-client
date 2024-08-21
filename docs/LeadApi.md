# openapi_client.LeadApi

All URIs are relative to *https://api.engine.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lead**](LeadApi.md#get_lead) | **GET** /leads/{uuid} | Get lead
[**get_rate_table**](LeadApi.md#get_rate_table) | **GET** /originator/rateTables/{uuid} | Get rate table
[**get_rate_table_for_specified_lead**](LeadApi.md#get_rate_table_for_specified_lead) | **POST** /leads/{leadUuid}/rateTables | Submit a lead and get a rate table
[**submit_lead**](LeadApi.md#submit_lead) | **POST** /leads/rateTables | Submit lead
[**update_lead**](LeadApi.md#update_lead) | **PATCH** /leads/{uuid} | Update a lead


# **get_lead**
> Lead get_lead(uuid)

Get lead

Get the lead for a specified UUID. If the UUID is unkown, a `404 Not Found` response will be returned.

### Example

* Bearer Authentication (confidentialBearerToken):

```python
import openapi_client
from openapi_client.models.lead import Lead
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

# Configure Bearer authorization: confidentialBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LeadApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get lead
        api_response = api_instance.get_lead(uuid)
        print("The response of LeadApi->get_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeadApi->get_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**Lead**](Lead.md)

### Authorization

[confidentialBearerToken](../README.md#confidentialBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Malformed request |  -  |
**401** | Unauthorized request |  -  |
**404** | Unknown UUID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_table**
> RateTable get_rate_table(uuid)

Get rate table

Get the rate table for a specified UUID. If the UUID is unkown, a `404 Not Found` response will be returned.  Usually used to poll a rate table that has pending responses immediately after creation via the \"Submit lead\" endpoint. For more details see [the Lead overview](https://engine.tech/docs/api-reference/#even-financial-api-lead).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.rate_table import RateTable
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
    api_instance = openapi_client.LeadApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get rate table
        api_response = api_instance.get_rate_table(uuid)
        print("The response of LeadApi->get_rate_table:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeadApi->get_rate_table: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**RateTable**](RateTable.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Malformed request |  -  |
**401** | Unauthorized request |  -  |
**404** | Unknown UUID |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_rate_table_for_specified_lead**
> RateTable get_rate_table_for_specified_lead(lead_uuid, lead_create_data)

Submit a lead and get a rate table

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.lead_create_data import LeadCreateData
from openapi_client.models.rate_table import RateTable
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
    api_instance = openapi_client.LeadApi(api_client)
    lead_uuid = 'lead_uuid_example' # str | The UUID of the lead we want to create a rate table for.
    lead_create_data = openapi_client.LeadCreateData() # LeadCreateData | A Lead object

    try:
        # Submit a lead and get a rate table
        api_response = api_instance.get_rate_table_for_specified_lead(lead_uuid, lead_create_data)
        print("The response of LeadApi->get_rate_table_for_specified_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeadApi->get_rate_table_for_specified_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_uuid** | **str**| The UUID of the lead we want to create a rate table for. | 
 **lead_create_data** | [**LeadCreateData**](LeadCreateData.md)| A Lead object | 

### Return type

[**RateTable**](RateTable.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The generated &#x60;RateTable&#x60; |  -  |
**400** | Bad Request |  -  |
**401** | Unauthorized request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **submit_lead**
> RateTable submit_lead(lead_create_data)

Submit lead

Submit a lead and get a rate table. If the rate table has a non-empty `pendingResponses` array, reload it via the \"Get rate table\" endpoint. For more details see [the Lead overview](https://engine.tech/docs/api-reference/#even-financial-api-lead).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.lead_create_data import LeadCreateData
from openapi_client.models.rate_table import RateTable
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
    api_instance = openapi_client.LeadApi(api_client)
    lead_create_data = {"productTypes":["loan"],"personalInformation":{"firstName":"John","lastName":"Doe","email":"john@example.com","city":"New York","state":"NY","primaryPhone":"2125556789","address1":"175 5th Ave","zipcode":"10010","monthsAtAddress":72,"activeMilitary":false,"militaryVeteran":false,"dateOfBirth":"1993-10-09","ssn":"111-22-3333"},"personalReferenceInformation":{},"loanInformation":{"purpose":"debt_consolidation","loanAmount":10000},"mortgageInformation":{"propertyStatus":"own_with_mortgage"},"creditCardInformation":{},"savingsInformation":{},"creditInformation":{"providedCreditRating":"good"},"financialInformation":{"employmentStatus":"employed","employmentPayFrequency":"biweekly","annualIncome":80000},"employmentInformation":{},"legalInformation":{"consentsToFcra":true,"consentsToTcpa":true,"consentsToSms":false,"fcraLanguage":"By checking this box/clicking 'agree' I hereby consent to the 'E-Sign Agreement', the 'Credit Authorization Agreement', the Terms of Service and Privacy Policy, and I am providing written consent under the Fair Credit Reporting Act (FCRA) for [Engine by MoneyLion and/or Insert Company Name], its partners and financial institutions to obtain consumer report information from my credit profile. I request that my information be provided to their partners, lenders, and financial services partners to provide me with financial recommendations, which may also include debt relief, credit repair, credit monitoring or other related services","tcpaLanguage":"I agree to be contacted by [Engine by MoneyLion and/or Insert Company Name] its partners and their affiliated companies and financial institutions via email, postal mail service and/or at the telephone number(s) I have provided above to explore various financial products and services I inquired about, including contact through automatic dialing systems, artificial or pre-recorded voice messaging, or text message. Consent is not required as a condition to utilize the service, and you may choose to be contacted by an individual customer care representative(s) by calling XXXXX or emailing XXXX"},"educationInformation":{"educationLevel":"bachelors"},"coApplicantInformation":{},"healthInformation":{},"lifeInsuranceInformation":{},"refinanceLoans":[],"identificationInformation":{},"clientTags":{"transid":["fk912234"],"subid":["ag67125"]},"isTest":false,"sessionUuid":"c363ec58-c5f0-54ff-b8f7-0f5f630213d9"} # LeadCreateData | 

    try:
        # Submit lead
        api_response = api_instance.submit_lead(lead_create_data)
        print("The response of LeadApi->submit_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeadApi->submit_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lead_create_data** | [**LeadCreateData**](LeadCreateData.md)|  | 

### Return type

[**RateTable**](RateTable.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Invalid request |  -  |
**401** | Unauthorized request |  -  |
**409** | Duplicate lead |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_lead**
> LeadUuid update_lead(uuid, lead_create_data)

Update a lead

Update a `Lead` by its UUID. Array fields (like `productTypes`) with new values are _merged_ with existing values.

### Example

* Bearer Authentication (confidentialBearerToken):

```python
import openapi_client
from openapi_client.models.lead_create_data import LeadCreateData
from openapi_client.models.lead_uuid import LeadUuid
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

# Configure Bearer authorization: confidentialBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.LeadApi(api_client)
    uuid = 'uuid_example' # str | 
    lead_create_data = openapi_client.LeadCreateData() # LeadCreateData | A LeadCreateData object

    try:
        # Update a lead
        api_response = api_instance.update_lead(uuid, lead_create_data)
        print("The response of LeadApi->update_lead:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LeadApi->update_lead: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 
 **lead_create_data** | [**LeadCreateData**](LeadCreateData.md)| A LeadCreateData object | 

### Return type

[**LeadUuid**](LeadUuid.md)

### Authorization

[confidentialBearerToken](../README.md#confidentialBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Lead updated |  -  |
**400** | Invalid data |  -  |
**401** | Unauthorized request |  -  |
**404** | &#x60;Lead&#x60; with the given UUID does not exist |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

