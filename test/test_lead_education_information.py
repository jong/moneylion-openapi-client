# coding: utf-8

"""
    Engine by MoneyLion API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.58.0
    Contact: help@engine.tech
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.models.lead_education_information import LeadEducationInformation

class TestLeadEducationInformation(unittest.TestCase):
    """LeadEducationInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeadEducationInformation:
        """Test LeadEducationInformation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeadEducationInformation`
        """
        model = LeadEducationInformation()
        if include_optional:
            return LeadEducationInformation(
                education_level = 'high_school',
                graduate_degree_type = 'doctor_of_medicine',
                university_attended = '',
                university_ope_id = '0480724a',
                graduation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                graduate_graduation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                graduate_last_attended_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                graduate_university_attended = '',
                graduate_university_ope_id = '0480724a',
                undergraduate_graduation_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                undergraduate_last_attended_date = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date(),
                undergraduate_university_attended = '',
                undergraduate_university_ope_id = '0480724a'
            )
        else:
            return LeadEducationInformation(
        )
        """

    def testLeadEducationInformation(self):
        """Test LeadEducationInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()