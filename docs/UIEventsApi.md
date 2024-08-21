# openapi_client.UIEventsApi

All URIs are relative to *https://api.engine.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_offer_display**](UIEventsApi.md#create_offer_display) | **POST** /uiEvent/offerDisplays | Record offer display
[**create_session_init**](UIEventsApi.md#create_session_init) | **POST** /uiEvent/sessionInits | Record new session


# **create_offer_display**
> OfferDisplay create_offer_display(offer_display_create_data=offer_display_create_data)

Record offer display

Records that an offer was displayed to a user.  You can also use a pixel to record this event, by rendering an `img` tag in the DOM alongside the offer, where the `src` URL follows this pattern: `/uiEvent/offerDisplays/{leadUuid}/{rateTableUuid}/{offerUuid}/pixel.gif`  So, for example: `<img src=\"https://api.engine.tech/uiEvent/offerDisplays/39197a3f-d2f4-43eb-9999-7f7a154d79bc/eb0e6cc4-df13-42fe-b254-c58c9b35a3d6/a698f56f-0946-4642-9720-5f280bc8b2e0/pixel.gif\">`  The URL will always respond successfully with a transparent 1x1 GIF. 

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.offer_display import OfferDisplay
from openapi_client.models.offer_display_create_data import OfferDisplayCreateData
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
    api_instance = openapi_client.UIEventsApi(api_client)
    offer_display_create_data = {"leadUuid":"f914eb07-a64f-51d8-b882-ff508a8c5c81","rateTableUuid":"952a1184-d369-5958-9a0f-bec903e11c48","offerUuid":"3426f971-1aa5-5cb0-91a9-cf2edcfa5dfa"} # OfferDisplayCreateData |  (optional)

    try:
        # Record offer display
        api_response = api_instance.create_offer_display(offer_display_create_data=offer_display_create_data)
        print("The response of UIEventsApi->create_offer_display:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIEventsApi->create_offer_display: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offer_display_create_data** | [**OfferDisplayCreateData**](OfferDisplayCreateData.md)|  | [optional] 

### Return type

[**OfferDisplay**](OfferDisplay.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Unauthorized request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_session_init**
> SessionInit create_session_init(session_init_create_data=session_init_create_data)

Record new session

Records that a user has begun a new session. A session can be any extended interaction with the Engine by MoneyLion API by an individual user.  The most common use case is to initiate a session when a user lands on a financial offer search experience. You can either supply `sessionUuid` in the request body, or submit an empty body and one will be generated for you. In either case, the returned `sessionUuid` should be included in the lead body of subsequent rate table requests. 

### Example

* Bearer Authentication (publishableBearerToken):

```python
import openapi_client
from openapi_client.models.session_init import SessionInit
from openapi_client.models.session_init_create_data import SessionInitCreateData
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
    api_instance = openapi_client.UIEventsApi(api_client)
    session_init_create_data = {"sessionUuid":"820cc28f-ae99-55a5-a364-6353efd4a48b"} # SessionInitCreateData |  (optional)

    try:
        # Record new session
        api_response = api_instance.create_session_init(session_init_create_data=session_init_create_data)
        print("The response of UIEventsApi->create_session_init:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UIEventsApi->create_session_init: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **session_init_create_data** | [**SessionInitCreateData**](SessionInitCreateData.md)|  | [optional] 

### Return type

[**SessionInit**](SessionInit.md)

### Authorization

[publishableBearerToken](../README.md#publishableBearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success |  -  |
**401** | Unauthorized request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

