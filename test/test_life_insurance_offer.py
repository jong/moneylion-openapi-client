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

from openapi_client.models.life_insurance_offer import LifeInsuranceOffer

class TestLifeInsuranceOffer(unittest.TestCase):
    """LifeInsuranceOffer unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> LifeInsuranceOffer:
        """Test LifeInsuranceOffer
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `LifeInsuranceOffer`
        """
        model = LifeInsuranceOffer()
        if include_optional:
            return LifeInsuranceOffer(
                details = openapi_client.models.life_insurance_offer_details.LifeInsuranceOfferDetails(
                    policy_amount = 56, 
                    term_length = 56, 
                    term_unit = 'day', 
                    monthly_premium_amount = 1.337, 
                    annual_premium_amount = 1.337, 
                    semi_annual_premium_amount = 1.337, 
                    online_app_available = True, 
                    no_medical_test = True, 
                    package_type = 'basic', 
                    recommended = True, 
                    medical_exam = 'no_exam_if_qualified', 
                    policy_name = '', 
                    carrier_decision_type = 'instant', 
                    partner_quote_id = '', 
                    convert_to_permanent = True, 
                    child_rider = '', 
                    accelerated_death_benefit = True, 
                    waiver_of_premium = '', 
                    is_online_application = True, 
                    delivery_method = '', 
                    exam_required = '', ),
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
            return LifeInsuranceOffer(
                details = openapi_client.models.life_insurance_offer_details.LifeInsuranceOfferDetails(
                    policy_amount = 56, 
                    term_length = 56, 
                    term_unit = 'day', 
                    monthly_premium_amount = 1.337, 
                    annual_premium_amount = 1.337, 
                    semi_annual_premium_amount = 1.337, 
                    online_app_available = True, 
                    no_medical_test = True, 
                    package_type = 'basic', 
                    recommended = True, 
                    medical_exam = 'no_exam_if_qualified', 
                    policy_name = '', 
                    carrier_decision_type = 'instant', 
                    partner_quote_id = '', 
                    convert_to_permanent = True, 
                    child_rider = '', 
                    accelerated_death_benefit = True, 
                    waiver_of_premium = '', 
                    is_online_application = True, 
                    delivery_method = '', 
                    exam_required = '', ),
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

    def testLifeInsuranceOffer(self):
        """Test LifeInsuranceOffer"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
