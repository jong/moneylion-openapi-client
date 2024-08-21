# openapi_client.ApprovalProbabilityApi

All URIs are relative to *https://api.engine.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_loans_approval_probability_report**](ApprovalProbabilityApi.md#create_loans_approval_probability_report) | **POST** /approvalProbability/loanReports | Get a loan approval probability report
[**get_loans_approval_probability_report**](ApprovalProbabilityApi.md#get_loans_approval_probability_report) | **GET** /approvalProbability/loanReports/{uuid} | Get approval probability loan report


# **create_loans_approval_probability_report**
> LoanReport create_loans_approval_probability_report(loan_report_create_data=loan_report_create_data)

Get a loan approval probability report

Get a report on approval probabilities for loan offers for a specified cohort of users.

### Example

* Bearer Authentication (experimentalBearerToken):

```python
import openapi_client
from openapi_client.models.loan_report import LoanReport
from openapi_client.models.loan_report_create_data import LoanReportCreateData
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

# Configure Bearer authorization: experimentalBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApprovalProbabilityApi(api_client)
    loan_report_create_data = {"annualIncome":75000,"creditRating":"excellent","totalDebt":10000,"countOfDerogatories":0,"state":"NY","loanPurpose":"debt_consolidation","loanAmount":10000} # LoanReportCreateData |  (optional)

    try:
        # Get a loan approval probability report
        api_response = api_instance.create_loans_approval_probability_report(loan_report_create_data=loan_report_create_data)
        print("The response of ApprovalProbabilityApi->create_loans_approval_probability_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalProbabilityApi->create_loans_approval_probability_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **loan_report_create_data** | [**LoanReportCreateData**](LoanReportCreateData.md)|  | [optional] 

### Return type

[**LoanReport**](LoanReport.md)

### Authorization

[experimentalBearerToken](../README.md#experimentalBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**400** | Malformed request |  -  |
**401** | Unauthorized request |  -  |
**422** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_loans_approval_probability_report**
> LoanReport get_loans_approval_probability_report(uuid)

Get approval probability loan report

Get the approval probability report for a specified UUID. If the UUID is unkown, a `404 Not Found` response will be returned.

### Example

* Bearer Authentication (experimentalBearerToken):

```python
import openapi_client
from openapi_client.models.loan_report import LoanReport
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

# Configure Bearer authorization: experimentalBearerToken
configuration = openapi_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ApprovalProbabilityApi(api_client)
    uuid = 'uuid_example' # str | 

    try:
        # Get approval probability loan report
        api_response = api_instance.get_loans_approval_probability_report(uuid)
        print("The response of ApprovalProbabilityApi->get_loans_approval_probability_report:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ApprovalProbabilityApi->get_loans_approval_probability_report: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **uuid** | **str**|  | 

### Return type

[**LoanReport**](LoanReport.md)

### Authorization

[experimentalBearerToken](../README.md#experimentalBearerToken)

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

