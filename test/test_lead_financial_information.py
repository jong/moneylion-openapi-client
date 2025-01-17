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

from openapi_client.models.lead_financial_information import LeadFinancialInformation

class TestLeadFinancialInformation(unittest.TestCase):
    """LeadFinancialInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LeadFinancialInformation:
        """Test LeadFinancialInformation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LeadFinancialInformation`
        """
        model = LeadFinancialInformation()
        if include_optional:
            return LeadFinancialInformation(
                employment_status = 'employed',
                employment_pay_frequency = 'weekly',
                annual_income = 56,
                monthly_net_income = 56,
                bank_name = '',
                bank_routing_number = '',
                bank_account_type = 'checking',
                credit_card_debt = 56,
                months_at_bank = 56,
                bank_account_number = '',
                monthly_debt = 56,
                total_assets = 56,
                monthly_housing_payment = 56,
                available_assets = 56,
                additional_income = 56,
                additional_income_frequency = 'weekly',
                has_direct_deposit = True,
                total_unsecured_debt = 56
            )
        else:
            return LeadFinancialInformation(
        )
        """

    def testLeadFinancialInformation(self):
        """Test LeadFinancialInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
