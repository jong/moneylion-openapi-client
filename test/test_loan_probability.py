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

from openapi_client.models.loan_probability import LoanProbability

class TestLoanProbability(unittest.TestCase):
    """LoanProbability unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LoanProbability:
        """Test LoanProbability
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LoanProbability`
        """
        model = LoanProbability()
        if include_optional:
            return LoanProbability(
                probability = 1.337,
                apr_percent_min = 1.337,
                apr_percent_max = 1.337,
                term_months_min = 56,
                term_months_max = 56,
                product_sub_type = 'credit_card'
            )
        else:
            return LoanProbability(
                probability = 1.337,
                apr_percent_min = 1.337,
                apr_percent_max = 1.337,
                term_months_min = 56,
                term_months_max = 56,
        )
        """

    def testLoanProbability(self):
        """Test LoanProbability"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()