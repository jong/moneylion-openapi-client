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

from openapi_client.models.incentive_details import IncentiveDetails

class TestIncentiveDetails(unittest.TestCase):
    """IncentiveDetails unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> IncentiveDetails:
        """Test IncentiveDetails
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `IncentiveDetails`
        """
        model = IncentiveDetails()
        if include_optional:
            return IncentiveDetails(
                amount = 1.337,
                unit = 'usd',
                display = '',
                type = 'cash_back'
            )
        else:
            return IncentiveDetails(
                amount = 1.337,
                unit = 'usd',
                display = '',
                type = 'cash_back',
        )
        """

    def testIncentiveDetails(self):
        """Test IncentiveDetails"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
