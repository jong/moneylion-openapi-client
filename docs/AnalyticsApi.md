# openapi_client.AnalyticsApi

All URIs are relative to *https://api.engine.tech*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_lead_client_tags**](AnalyticsApi.md#get_lead_client_tags) | **GET** /supplyAnalytics/leadClientTags | Get lead client tags
[**get_lead_events**](AnalyticsApi.md#get_lead_events) | **GET** /supplyAnalytics/leadEvents | Get lead events
[**get_lead_payouts**](AnalyticsApi.md#get_lead_payouts) | **GET** /supplyAnalytics/leadPayouts | Get lead payouts


# **get_lead_client_tags**
> LeadClientTagsResponse get_lead_client_tags(timestamp)

Get lead client tags

### What is the Lead Client Tags API used for?  Client tags (also known as Custom Lead Attributes) are arbitrary key:value pairs of information that can be set using the API or URL of a partner page to enable custom segmentation. Client tags provides you a method to be able to segment leads to support uses cases like:    - See how various traffic sources on the supply partners site perform  - See what preferences their users from different segments have   The lead client tag endpoint returns client tags associated with a lead.  ### What use cases does it support?  You have the ability to append client tags, which are your specific identifiers (ie. traffic source, article, unique user identifier, etc.), to leads sent to Engine by MoneyLion's API via a partner page, embed, or the native API integration. Below are instructions on how to implement these client tags by integration so Engine by MoneyLion can ingest and report this data back to you.  In the below examples, the channel partner is appending two custom lead attributes: `traffic_source` and `article`. The values of `1234` and `5678` for `traffic_source` and `article`, respectively, are sample values and typically correspond to identifiers in the Channel Partner’s data.  #### Partner Page Custom lead attributes are appended to the partner page URL:  ``` https://hifiona.com/even-testing/loans?tag.traffic_source=1234&tag.clientid= ```  `traffic_source` is given a unique value, in this case, `1234`, to identify that any leads arriving marked with the attribute `traffic_source` and the attribute value `1234` have come from this particular source, which could be a particular subsection of your website, an article, an emailing list, etc. Custom lead attributes like traffic_source are especially useful if you plan on deploying your partner page in multiple locations, such as multiple pages on your website, or in multiple articles, to help identify the origin of leads and analyze which traffic sources are performing the most optimally.  `clientid` is not given a unique value, which means that any leads arriving marked with the attribute `clientid` will be assigned a unique value, most commonly an alphanumeric string, such as `202102021abcde1`, which will then be reported back to you via Client Tags API, so that you can understand and analyze metrics on a lead level.  Note that `traffic_source` and `clientid` are just two examples of Client tags, and that these can be any identifier that you wish. Other common custom lead attributes include subid and article.  It's also possible for a single key to have multiple values (eg `traffic_source=1234`, `traffic_source=abcd`, etc) and as such don't assume only the last value set for a key will persist.  Additionally it's worth noting that Engine by MoneyLion's own platform uses client tags mechanism in some cases hence don't be surprised to see client tags appear that you don't anticipate.  #### Embed Custom lead attributes are embedded to the source URL of the embed code:  ``` src=\"https://embed.hifiona.com/ui/multi-product/index.html?partner=even-testing&access_token={access_token}&company_uuid={company_uuid}&productType=loan&available_products=loan&tag.traffic_source=1234&tag.article=5678 ```  #### Native API In the `clientTags` section of the post request to Engine by MoneyLion's API, include custom lead attributes keys and values:  ``` {\"clientTags\": {\"traffic_source\": [\"1234\"], \"article\": [\"5678\"]}} ```  ### How does it work?  The endpoint is designed for paging forward through data in order to populate your local database. By relying on the “nextUrl” parameter provided in the preceding call’s response, we can guarantee a) you will see no gaps, and b) you will see no duplicates.  This endpoint should be polled hourly on the 15 minute mark to fetch new events. Data for this endpoint is made available with an 1 hour SLA. If the current time is '2020-01-01T08:15:00Z' UTC, making a request to this endpoint with the timestamp set to '2020-01-01T08:00:00Z' will error because of the 1 hour SLA. Making a request with a timestamp of '2020-01-01T07:00:00Z' however, will succeed.  For convenience, we provide a `shouldContinuePolling` flag to signal if data has been published at the location of the `nextUrl`.  The endpoint is cursor based. You can consume batches of events 1 hour at a time for the product tied to your company uuid. All that is required is a bearer token and timestamp. The endpoint will respond with all of the events that have happened from that timestamp forward for one hour. It will also include a pointer to the next timestamp to be used for a subsequent call. This endpoint should be polled hourly on the 15 minute mark to fetch new events. 

### Example

* Bearer Authentication (confidentialBearerToken):

```python
import openapi_client
from openapi_client.models.lead_client_tags_response import LeadClientTagsResponse
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
    api_instance = openapi_client.AnalyticsApi(api_client)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime | The lower bound for when an event hit Engine by MoneyLion's system. 

    try:
        # Get lead client tags
        api_response = api_instance.get_lead_client_tags(timestamp)
        print("The response of AnalyticsApi->get_lead_client_tags:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_lead_client_tags: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **datetime**| The lower bound for when an event hit Engine by MoneyLion&#39;s system.  | 

### Return type

[**LeadClientTagsResponse**](LeadClientTagsResponse.md)

### Authorization

[confidentialBearerToken](../README.md#confidentialBearerToken)

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

# **get_lead_events**
> LeadEventResponse get_lead_events(timestamp)

Get lead events

### What is the Lead Events API used for?  With the Lead Events API, you can pull KPI related data for your funnel, measure conversions, and iterate so that you can meet your business goals.  The endpoint returns events associated with each lead. The event type is indicated by the eventType property. Each event will also include metadata applicable to the eventType. It allows easy consumption of the events into your database so that you can integrate it into your BI framework and compare it alongside data from other systems to assess performance holistically.  ### How does it work?  The endpoint is cursor based. You can consume batches of events 1 hour at a time for the product tied to your company uuid. All that is required is a bearer token and timestamp. The endpoint will respond with all of the events that have happened from that timestamp forward for one hour. It will also include a pointer to the next timestamp to be used for a subsequent call. This endpoint should be polled hourly on the 15 minute mark to fetch new events.  For convenience, we provide a `shouldContinuePolling` flag to signal if data has been published at the location of the `nextUrl`.  The endpoint is designed for paging forward through data in order to populate your local database. By relying on the `nextUrl` parameter provided in the preceding call's response, we can guarantee a) you will see no gaps, and b) you will see no duplicates.  This endpoint should be polled hourly on the 15 minute mark to fetch new events. Data for this endpoint is made available with a 1 hour SLA.  If the current time is '2020-01-01T08:15:00Z' UTC, making a request to this endpoint with the timestamp set to '2020-01-01T08:00:00Z' will error because of the 1 hour SLA. Making a request with a timestamp of '2020-01-01T07:10:00Z' however, will succeed.  ### Event Definitions  Common Attributes  <table>   <thead>     <tr>       <th>Attribute Name</th>       <th>Type</th>       <th>Format</th>       <th>Enum</th>     </tr>   </thead>   <tbody>     <tr>       <td>eventType</td>       <td>string</td>       <td>&#xa0;</td>       <td>leadCreated appSubmitted apiApproved apiRejected offerClicked applied approved listed opened funded conversation lenderQualifiedLead</td>     </tr>     <tr>       <td>leadUuid</td>       <td>string</td>       <td>uuid</td>       <td>&#xa0;</td>     </tr>     <tr>       <td>leadCreatedAt</td>       <td>string</td>       <td>date-time</td>       <td>&#xa0;</td>     </tr>     <tr>       <td>eventCreatedAt</td>       <td>string</td>       <td>date-time</td>       <td>&#xa0;</td>     </tr>     <tr>       <td>amountInCents</td>       <td>int</td>       <td>&#xa0;</td>       <td>&#xa0;</td>     </tr>     <tr>       <td>financialInstitutionName</td>       <td>string</td>       <td>&#xa0;</td>       <td>&#xa0;</td>     </tr>     <tr>       <td>financialInstitutionUuid</td>       <td>string</td>       <td>uuid</td>       <td>&#xa0;</td>     </tr>     <tr>       <td>productType</td>       <td>string</td>       <td>&#xa0;</td>       <td>creditCard insurance lifeInsurance loan mortgage savings other</td>     </tr>     <tr>       <td>isTest</td>       <td>boolean</td>       <td>&#xa0;</td>       <td>Whether a Lead was created using a test access token</td>     </tr>   </tbody> </table>  Common Event Types  <table>   <thead>     <tr>       <th> Event Type </th>       <th> Required Attributes </th>       <th> Optional Attributes </th>     </tr>   </thead>   <tbody>     <tr>       <td> leadCreated </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt </td>       <td> </td>     </tr>     <tr>       <td> appSubmitted </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt </td>       <td> </td>     </tr>     <tr>       <td> apiApproved </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> apiRejected </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> offerClicked </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> applied </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> approved </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> listed </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> opened </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>   </tbody> </table>  Event Types for Personal Loans Funnel  <table>   <thead>     <tr>       <th> Event Type </th>       <th> Definition </th>       <th> Required Attributes </th>       <th> Optional Attributes </th>     </tr>   </thead>   <tbody>     <tr>       <td> leadCreated </td>       <td> A user enters the marketplace funnel </td>       <td> See under common event types </td>       <td></td>     </tr>     <tr>       <td> appSubmitted </td>       <td> The lead has filled out the information in the Engine by MoneyLion application and a rate table has been created </td>       <td> See under common event types </td>       <td></td>     </tr>     <tr>       <td> apiApproved </td>       <td> Financial institution has pre-approved or pre-qualified a user for at least one offer </td>       <td> See under common event types </td>       <td></td>     </tr>     <tr>       <td> apiRejected </td>       <td> Financial institution has not pre-approved or pre-qualified a user for any offers </td>       <td> See under common event types </td>       <td></td>     </tr>     <tr>       <td> offerClicked </td>       <td> The user clicks on or is auto redirected into an offer </td>       <td> See under common event types </td>       <td></td>     </tr>     <tr>       <td> applied </td>       <td> The user applied for an offer in the financial institution's experience </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType amountInCents </td>     </tr>     <tr>       <td> approved </td>       <td> The user was approved for an offer after applying in the financial institution's experience </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType amountInCents  </td>     </tr>     <tr>       <td> listed </td>       <td> The user's loan was listed on the financial institution's marketplace for funding </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType amountInCents </td>     </tr>     <tr>       <td> funded </td>       <td> The user has a loan funded </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType amountInCents </td>     </tr>     <tr>       <td> opened </td>       <td> The user monetizes with a special offer </td>       <td> See under common events </td>       <td></td>     </tr>     <tr>       <td> conversion </td>       <td> This event varies by lender, and will be deprecated. </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid </td>       <td> productType </td>     </tr>     <tr>       <td> lenderQualifiedLead </td>       <td> Financial institution further collected information from a lead </td>       <td> eventType leadUuid leadCreatedAt eventCreatedAt financialInstitutionName financialInstitutionUuid amountInCents </td>       <td> productType </td>     </tr>   </tbody> </table> 

### Example

* Bearer Authentication (confidentialBearerToken):

```python
import openapi_client
from openapi_client.models.lead_event_response import LeadEventResponse
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
    api_instance = openapi_client.AnalyticsApi(api_client)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime | The lower bound for when an event hit Engine by MoneyLion's system. 

    try:
        # Get lead events
        api_response = api_instance.get_lead_events(timestamp)
        print("The response of AnalyticsApi->get_lead_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_lead_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **datetime**| The lower bound for when an event hit Engine by MoneyLion&#39;s system.  | 

### Return type

[**LeadEventResponse**](LeadEventResponse.md)

### Authorization

[confidentialBearerToken](../README.md#confidentialBearerToken)

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

# **get_lead_payouts**
> LeadPayoutResponse get_lead_payouts(timestamp)

Get lead payouts

### What is the Lead Payouts API used for?  With Lead payout API you can collect granular payout information for leads you have submitted. It returns payout events associated with a lead. Event data is limited to the amount that was paid out, and when the payout was booked.  We recently added two additional optional fields to the payout event information tied to leads:     - `financialInstitutionUuid`   - `financialInstitutionName`   These fields will tie conversion events to specific Financial Institutions (Lenders) for your knowledge and analytical use. We include these additional fields to disambiguate which financial institution a given payout originates from in the case of multiple payouts against a given lead. Not all lead payout events can be traced back to a financial institution, so these fields are optional. The Financial Institution Name is not guaranteed to be a stable identifier of the entity; Financial Institution UUID is.  LeadPayout `deletedAt` will report the time that the payout was deleted. Payouts get deleted when there are post dated Contract changes or partner reporting errors requiring reingestion of EDEs.  ### How does it work?  The endpoint is cursor based. You can consume batches of events 1 hour at a time for the product tied to your company uuid. All that is required is a bearer token and timestamp. The endpoint will respond with all of the events that have happened from that timestamp forward for one hour. It will also include a pointer to the next timestamp to be used for a subsequent call. This endpoint should be polled hourly on the 15 minute mark to fetch new events.  For convenience, we provide a `shouldContinuePolling` flag to signal if data has yet been published at the location of the nextUrl.  The endpoint is designed for paging forward through data in order to populate your local database. By relying on the `nextUrl` parameter provided in the preceding call's response, we can guarantee a) you will see no gaps, and b) you will see no duplicates.  This endpoint should be polled hourly on the 15 minute mark to fetch new events. Data for this endpoint is made available with an 1 hour SLA. If the current time is '2020-01-01T08:15:00Z' UTC, making a request to this endpoint with the timestamp set to '2020-01-01T08:00:00Z' will error because of the 1 hour SLA. Making a request with a timestamp of '2020-01-01T07:00:00Z' however, will succeed. 

### Example

* Bearer Authentication (confidentialBearerToken):

```python
import openapi_client
from openapi_client.models.lead_payout_response import LeadPayoutResponse
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
    api_instance = openapi_client.AnalyticsApi(api_client)
    timestamp = '2013-10-20T19:20:30+01:00' # datetime | The lower bound for when an event hits Engine by MoneyLion's system. 

    try:
        # Get lead payouts
        api_response = api_instance.get_lead_payouts(timestamp)
        print("The response of AnalyticsApi->get_lead_payouts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnalyticsApi->get_lead_payouts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **timestamp** | **datetime**| The lower bound for when an event hits Engine by MoneyLion&#39;s system.  | 

### Return type

[**LeadPayoutResponse**](LeadPayoutResponse.md)

### Authorization

[confidentialBearerToken](../README.md#confidentialBearerToken)

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

