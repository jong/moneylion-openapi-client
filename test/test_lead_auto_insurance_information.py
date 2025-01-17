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

from openapi_client.models.lead_auto_insurance_information import LeadAutoInsuranceInformation

class TestLeadAutoInsuranceInformation(unittest.TestCase):
    """LeadAutoInsuranceInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeadAutoInsuranceInformation:
        """Test LeadAutoInsuranceInformation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeadAutoInsuranceInformation`
        """
        model = LeadAutoInsuranceInformation()
        if include_optional:
            return LeadAutoInsuranceInformation(
                number_of_vehicles = 56,
                has_auto_insurance = True
            )
        else:
            return LeadAutoInsuranceInformation(
        )
        """

    def testLeadAutoInsuranceInformation(self):
        """Test LeadAutoInsuranceInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
