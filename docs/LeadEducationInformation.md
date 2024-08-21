# LeadEducationInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**education_level** | [**EducationLevel**](EducationLevel.md) |  | [optional] 
**graduate_degree_type** | [**GraduateDegreeType**](GraduateDegreeType.md) |  | [optional] 
**university_attended** | **str** | Name of university where a lead received their undergraduate degree. A lookup service for possible universities is available from using the /leads/universities endpoint. To maximize returned offers, this string must match one of the names returned from the lookup.  | [optional] 
**university_ope_id** | **str** | identification number used by the U.S. Department of Education&#39;s Office of Postsecondary Education (OPE) to identify schools that have Program Participation Agreements (PPA) so that its students are eligible to participate in Federal Student Financial Assistance programs under Title IV regulations. This is a 6-digit number followed by a 2-digit suffix used to identify branches, additional locations, and other entities that are part of the eligible institution. | [optional] 
**graduation_date** | **date** | Date the lead graudated from undergrad (YYYY-MM-DD) | [optional] 
**graduate_graduation_date** | **date** | Lead&#39;s graduate school graduation date (YYYY-MM-DD) | [optional] 
**graduate_last_attended_date** | **date** | Lead&#39;s last attended month/year for graduate school (YYYY-MM-DD) | [optional] 
**graduate_university_attended** | **str** | Name of university where a lead received their graduate degree. A lookup service for possible universities is available from using the /leads/universities endpoint. To maximize returned offers, this string must match one of the names returned from the lookup.  | [optional] 
**graduate_university_ope_id** | **str** | identification number used by the U.S. Department of Education&#39;s Office of Postsecondary Education (OPE) to identify schools that have Program Participation Agreements (PPA) so that its students are eligible to participate in Federal Student Financial Assistance programs under Title IV regulations. This is a 6-digit number followed by a 2-digit suffix used to identify branches, additional locations, and other entities that are part of the eligible institution. | [optional] 
**undergraduate_graduation_date** | **date** | Date the lead graduated from undergrad (YYYY-MM-DD). | [optional] 
**undergraduate_last_attended_date** | **date** | Lead&#39;s last attended month/year for undergrad (YYYY-MM-DD) | [optional] 
**undergraduate_university_attended** | **str** | Name of university where a lead received their undergraduate degree. A lookup service for possible universities is available from using the /leads/universities endpoint. To maximize returned offers, this string must match one of the names returned from the lookup.  | [optional] 
**undergraduate_university_ope_id** | **str** | identification number used by the U.S. Department of Education&#39;s Office of Postsecondary Education (OPE) to identify schools that have Program Participation Agreements (PPA) so that its students are eligible to participate in Federal Student Financial Assistance programs under Title IV regulations. This is a 6-digit number followed by a 2-digit suffix used to identify branches, additional locations, and other entities that are part of the eligible institution. | [optional] 

## Example

```python
from openapi_client.models.lead_education_information import LeadEducationInformation

# TODO update the JSON string below
json = "{}"
# create an instance of LeadEducationInformation from a JSON string
lead_education_information_instance = LeadEducationInformation.from_json(json)
# print the JSON string representation of the object
print(LeadEducationInformation.to_json())

# convert the object into a dict
lead_education_information_dict = lead_education_information_instance.to_dict()
# create an instance of LeadEducationInformation from a dict
lead_education_information_from_dict = LeadEducationInformation.from_dict(lead_education_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


