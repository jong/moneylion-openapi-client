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

from openapi_client.models.savings_offer import SavingsOffer

class TestSavingsOffer(unittest.TestCase):
    """SavingsOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavingsOffer:
        """Test SavingsOffer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavingsOffer`
        """
        model = SavingsOffer()
        if include_optional:
            return SavingsOffer(
                details = openapi_client.models.savings_offer_details.SavingsOfferDetails(
                    name = '', 
                    description = '', 
                    rate = 1.337, 
                    annual_percent_yield = 1.337, 
                    compounding_method = 'annually', 
                    introductory_period_months = 56, 
                    introductory_rate = 1.337, 
                    minimum_deposit = 1.337, 
                    minimum_deposit_with_fees = 1.337, 
                    monthly_fee = 1.337, 
                    check_writing = True, 
                    effective_as_of = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    federal_insurance_type = null, 
                    incentive_details = [
                        openapi_client.models.incentive_details.IncentiveDetails(
                            amount = 1.337, 
                            unit = 'usd', 
                            display = '', 
                            type = 'cash_back', )
                        ], 
                    cd_term_unit = 'day', 
                    cd_term_length = 56, ),
                uuid = '',
                partner = openapi_client.models.partner.Partner(
                    uuid = '', 
                    name = '', 
                    description = '', 
                    disclaimer = '', 
                    supports_pre_select = True, 
                    should_display_pre_select = True, 
                    supports_personalized_offers = True, 
                    image_url = '', 
                    subtext_override = '', ),
                marketplace = openapi_client.models.partner.Partner(
                    uuid = '', 
                    name = '', 
                    description = '', 
                    disclaimer = '', 
                    supports_pre_select = True, 
                    should_display_pre_select = True, 
                    supports_personalized_offers = True, 
                    image_url = '', 
                    subtext_override = '', ),
                product_type = 'credit_card',
                product_sub_type = 'credit_card',
                url = '',
                recommendation_score = 1.337,
                disclaimer = '',
                product_sub_type_disclaimer = '',
                expires_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f')
            )
        else:
            return SavingsOffer(
                details = openapi_client.models.savings_offer_details.SavingsOfferDetails(
                    name = '', 
                    description = '', 
                    rate = 1.337, 
                    annual_percent_yield = 1.337, 
                    compounding_method = 'annually', 
                    introductory_period_months = 56, 
                    introductory_rate = 1.337, 
                    minimum_deposit = 1.337, 
                    minimum_deposit_with_fees = 1.337, 
                    monthly_fee = 1.337, 
                    check_writing = True, 
                    effective_as_of = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    federal_insurance_type = null, 
                    incentive_details = [
                        openapi_client.models.incentive_details.IncentiveDetails(
                            amount = 1.337, 
                            unit = 'usd', 
                            display = '', 
                            type = 'cash_back', )
                        ], 
                    cd_term_unit = 'day', 
                    cd_term_length = 56, ),
                uuid = '',
                partner = openapi_client.models.partner.Partner(
                    uuid = '', 
                    name = '', 
                    description = '', 
                    disclaimer = '', 
                    supports_pre_select = True, 
                    should_display_pre_select = True, 
                    supports_personalized_offers = True, 
                    image_url = '', 
                    subtext_override = '', ),
                product_type = 'credit_card',
                product_sub_type = 'credit_card',
                url = '',
        )
        """

    def testSavingsOffer(self):
        """Test SavingsOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
