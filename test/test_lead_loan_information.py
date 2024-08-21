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

from openapi_client.models.lead_loan_information import LeadLoanInformation

class TestLeadLoanInformation(unittest.TestCase):
    """LeadLoanInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeadLoanInformation:
        """Test LeadLoanInformation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeadLoanInformation`
        """
        model = LeadLoanInformation()
        if include_optional:
            return LeadLoanInformation(
                purpose = 'auto',
                loan_amount = 56
            )
        else:
            return LeadLoanInformation(
        )
        """

    def testLeadLoanInformation(self):
        """Test LeadLoanInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
