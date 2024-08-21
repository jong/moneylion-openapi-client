# openapi_client.UIUtilsApi

All URIs are relative to *https://api.engine.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_featured_financial_institutions**](UIUtilsApi.md#get_featured_financial_institutions) | **GET** /uiUtil/featuredFinancialInstitutions | Get featured financial institutions
[**get_universities**](UIUtilsApi.md#get_universities) | **GET** /leads/universities | Get university names
[**get_vehicle_makes**](UIUtilsApi.md#get_vehicle_makes) | **GET** /leads/vehicles/makes | Get vehicle makes
[**get_vehicle_models**](UIUtilsApi.md#get_vehicle_models) | **GET** /leads/vehicles/models | Get vehicle models
[**get_vehicle_trims**](UIUtilsApi.md#get_vehicle_trims) | **GET** /leads/vehicles/trims | Get vehicle trims
[**get_vehicle_years**](UIUtilsApi.md#get_vehicle_years) | **GET** /leads/vehicles/years | Get vehicle years


# **get_featured_financial_institutions**
> List[FeaturedFinancialInstitution] get_featured_financial_institutions()

Get featured financial institutions

Get a list of featured financial institution names and logos that can be displayed prior to collecting personal information in a search application to improve the user experience. 

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.featured_financial_institution import FeaturedFinancialInstitution
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
    api_instance = openapi_client.UIUtilsApi(api_client)

    try:
        # Get featured financial institutions
        api_response = api_instance.get_featured_financial_institutions()
        print("The response of UIUtilsApi->get_featured_financial_institutions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIUtilsApi->get_featured_financial_institutions: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FeaturedFinancialInstitution]**](FeaturedFinancialInstitution.md)

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
**422** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_universities**
> List[str] get_universities(limit, name=name, offset=offset)

Get university names

Get a list of university names that correspond to the specified fragment.  This is useful for implementing an autocomplete input for the `educationInformation.universityAttended` lead field when searching for student loan refinancing loans. See the [Student Loan Refinancing overview](https://engine.tech/docs/api-reference/#student-loan-refinancing).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
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
    api_instance = openapi_client.UIUtilsApi(api_client)
    limit = 56 # int | Maximum number of results to return.
    name = 'name_example' # str | Fragment of a university name to seach for. (optional)
    offset = 0 # int | Number of results to skip before the first returned result. (optional) (default to 0)

    try:
        # Get university names
        api_response = api_instance.get_universities(limit, name=name, offset=offset)
        print("The response of UIUtilsApi->get_universities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIUtilsApi->get_universities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Maximum number of results to return. | 
 **name** | **str**| Fragment of a university name to seach for. | [optional] 
 **offset** | **int**| Number of results to skip before the first returned result. | [optional] [default to 0]

### Return type

**List[str]**

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

# **get_vehicle_makes**
> List[str] get_vehicle_makes(year=year)

Get vehicle makes

Get all makes for the given vehicle year  This is useful for implementing a select input for vehicle makes when searching for auto loan refinancing loans. A valid combination of year, make, model, and trim corresponds to a vehicle UUID that can be used in the `vehicleInformation.vehicleUuid` field. See the [Auto Loan Refinancing overview](https://engine.tech/docs/api-reference/#auto-loan-refinancing).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
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
    api_instance = openapi_client.UIUtilsApi(api_client)
    year = 56 # int |  (optional)

    try:
        # Get vehicle makes
        api_response = api_instance.get_vehicle_makes(year=year)
        print("The response of UIUtilsApi->get_vehicle_makes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIUtilsApi->get_vehicle_makes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | [optional] 

### Return type

**List[str]**

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Makes for given vehicle year |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_models**
> List[str] get_vehicle_models(year=year, make=make)

Get vehicle models

Get all models for the given vehicle year and make  This is useful for implementing a select input for vehicle models when searching for auto loan refinancing loans. A valid combination of year, make, model, and trim corresponds to a vehicle UUID that can be used in the `vehicleInformation.vehicleUuid` field. See the [Auto Loan Refinancing overview](https://engine.tech/docs/api-reference/#auto-loan-refinancing).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
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
    api_instance = openapi_client.UIUtilsApi(api_client)
    year = 56 # int |  (optional)
    make = 'make_example' # str |  (optional)

    try:
        # Get vehicle models
        api_response = api_instance.get_vehicle_models(year=year, make=make)
        print("The response of UIUtilsApi->get_vehicle_models:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIUtilsApi->get_vehicle_models: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | [optional] 
 **make** | **str**|  | [optional] 

### Return type

**List[str]**

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Models for given vehicle year and make |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_trims**
> List[VehicleDetails] get_vehicle_trims(year=year, make=make, model=model)

Get vehicle trims

Get vehicle details, including trims and uuids, for the given year, make, and model  This is useful for implementing a select input for vehicle trims when searching for auto loan refinancing loans. A valid combination of year, make, model, and trim corresponds to a vehicle UUID that can be used in the `vehicleInformation.vehicleUuid` field. The uuid field returned in successful response objects corresponds to a valid `vehicleUuid`. See the [Auto Loan Refinancing overview](https://engine.tech/docs/api-reference/#auto-loan-refinancing).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.vehicle_details import VehicleDetails
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
    api_instance = openapi_client.UIUtilsApi(api_client)
    year = 56 # int |  (optional)
    make = 'make_example' # str |  (optional)
    model = 'model_example' # str |  (optional)

    try:
        # Get vehicle trims
        api_response = api_instance.get_vehicle_trims(year=year, make=make, model=model)
        print("The response of UIUtilsApi->get_vehicle_trims:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIUtilsApi->get_vehicle_trims: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  | [optional] 
 **make** | **str**|  | [optional] 
 **model** | **str**|  | [optional] 

### Return type

[**List[VehicleDetails]**](VehicleDetails.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Vehicle details, including trim and uuid, for the given year, make, model |  -  |
**400** | Invalid request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_vehicle_years**
> List[int] get_vehicle_years()

Get vehicle years

Get all available vehicle years  This is useful for implementing a select input for vehicle years when searching for auto loan refinancing loans. A valid combination of year, make, model, and trim corresponds to a vehicle UUID that can be used in the `vehicleInformation.vehicleUuid` field. See the [Auto Loan Refinancing overview](https://engine.tech/docs/api-reference/#auto-loan-refinancing).

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
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
    api_instance = openapi_client.UIUtilsApi(api_client)

    try:
        # Get vehicle years
        api_response = api_instance.get_vehicle_years()
        print("The response of UIUtilsApi->get_vehicle_years:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIUtilsApi->get_vehicle_years: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[int]**

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Valid vehicle years |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

