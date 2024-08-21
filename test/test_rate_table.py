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

from openapi_client.models.rate_table import RateTable

class TestRateTable(unittest.TestCase):
    """RateTable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RateTable:
        """Test RateTable
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RateTable`
        """
        model = RateTable()
        if include_optional:
            return RateTable(
                uuid = '',
                lead_uuid = '',
                loan_amount = 56,
                embed_url = '',
                partner_page_url = '',
                credit_card_offers = [
                    openapi_client.models.credit_card_offer.CreditCardOffer(
                        details = openapi_client.models.credit_card_offer_details.CreditCardOfferDetails(
                            card_name = '', 
                            card_image_url = '', 
                            card_purposes = [
                                'balance_transfer'
                                ], 
                            rates_url = '', 
                            max_purchase_apr = 1.337, 
                            min_purchase_apr = 1.337, 
                            purchase_apr_text = '', 
                            max_purchase_intro_apr = 1.337, 
                            min_purchase_intro_apr = 1.337, 
                            purchase_intro_apr_term = 56, 
                            purchase_intro_apr_term_unit = 'day', 
                            purchase_intro_apr_text = '', 
                            max_cash_advance_apr = 1.337, 
                            min_cash_advance_apr = 1.337, 
                            cash_advance_apr_text = '', 
                            max_cash_advance_intro_apr = 1.337, 
                            min_cash_advance_intro_apr = 1.337, 
                            cash_advance_intro_apr_term = 56, 
                            cash_advance_intro_apr_term_unit = 'day', 
                            cash_advance_intro_apr_text = '', 
                            max_balance_transfer_apr = 1.337, 
                            min_balance_transfer_apr = 1.337, 
                            balance_transfer_apr_text = '', 
                            max_balance_transfer_intro_apr = 1.337, 
                            min_balance_transfer_intro_apr = 1.337, 
                            balance_transfer_intro_apr_term = 56, 
                            balance_transfer_intro_apr_term_unit = 'day', 
                            balance_transfer_intro_apr_text = '', 
                            max_annual_fee = 1.337, 
                            min_annual_fee = 1.337, 
                            annual_intro_fee = 1.337, 
                            annual_intro_fee_term = 56, 
                            intro_offer_amount = 1.337, 
                            intro_offer_text = '', 
                            intro_offer_type = 'miles', 
                            additional_details = [
                                ''
                                ], 
                            card_type = 'visa', 
                            minimum_credit_line = 1.337, 
                            minimum_penalty_apr = 1.337, 
                            maximum_penalty_apr = 1.337, 
                            balance_transfer_fee = 1.337, 
                            cash_advance_fee = 1.337, 
                            late_fee = 1.337, 
                            foreign_exchange_fee = 1.337, 
                            account_opening_fee = 1.337, 
                            return_payment_fee = 1.337, 
                            monthly_service_fee = 1.337, 
                            recommended_credit_ratings = [
                                'excellent'
                                ], 
                            pre_qualified = True, 
                            pre_approved = True, 
                            pre_selected = True, 
                            foreign_transaction_fee = 1.337, 
                            card_benefits = [
                                'No Foreign Transaction Fees'
                                ], ), )
                    ],
                loan_offers = [
                    openapi_client.models.loan_offer.LoanOffer(
                        uuid = '', 
                        product_type = 'credit_card', 
                        product_sub_type = 'credit_card', 
                        product_sub_type_disclaimer = '', 
                        url = '', 
                        originator = openapi_client.models.originator.Originator(
                            key = '', 
                            name = '', 
                            description = '', 
                            images = [
                                openapi_client.models.originator_image.OriginatorImage(
                                    size_key = '', 
                                    url = '', )
                                ], 
                            disclaimer = '', 
                            company_uuid = '', 
                            financial_institution_uuid = '', ), 
                        originator_id = '', 
                        pre_qualified = True, 
                        pre_approved = True, 
                        secured = True, 
                        co_applicant = True, 
                        sponsored = True, 
                        max_amount = 56, 
                        min_amount = 56, 
                        term_length = 56, 
                        term_unit = 'day', 
                        display_term_unit = '', 
                        term_description = '', 
                        max_apr = 1.337, 
                        min_apr = 1.337, 
                        mean_apr = 1.337, 
                        apr_type = 'variable', 
                        apr_description = '', 
                        fee_rate = 1.337, 
                        max_fee_rate = 1.337, 
                        min_fee_rate = 1.337, 
                        fee_fixed = 1.337, 
                        max_fee_fixed = 1.337, 
                        min_fee_fixed = 1.337, 
                        allow_prepayment = True, 
                        prepayment_fee = 1.337, 
                        monthly_payment = 1.337, 
                        max_monthly_payment = 1.337, 
                        min_monthly_payment = 1.337, 
                        monthly_payment_description = '', 
                        mean_monthly_payment = 1.337, 
                        max_total_payment = 1.337, 
                        min_total_payment = 1.337, 
                        mean_total_payment = 1.337, 
                        recommendation_score = 1.337, 
                        payout = 1.337, 
                        conversion_probability = 1.337, 
                        terms = '', 
                        amount_prefix = '', )
                    ],
                mortgage_offers = [
                    openapi_client.models.mortgage_offer.MortgageOffer(
                        details = openapi_client.models.mortgage_offer_details.MortgageOfferDetails(
                            interest_rate = 1.337, 
                            loan_type = 'fifteen_year_fixed', 
                            price_adjustment = 1.337, 
                            monthly_payment = 1.337, 
                            net_closing_costs = 1.337, 
                            apr = 1.337, 
                            loan_term = 56, 
                            adjustment_type = 'credits', ), )
                    ],
                savings_offers = [
                    openapi_client.models.savings_offer.SavingsOffer(
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
                            cd_term_length = 56, ), )
                    ],
                special_offers = [
                    openapi_client.models.special_offer.SpecialOffer(
                        uuid = '', 
                        name = '', 
                        desc = '', 
                        url = '', 
                        partner_name = '', 
                        partner_image_url = '', 
                        recommendation_score = 1.337, 
                        payout = 1.337, 
                        product_sub_type = 'credit_card', 
                        disclaimer = '', 
                        financial_institution_uuid = '', )
                    ],
                pending_originators = [
                    openapi_client.models.originator.Originator(
                        key = '', 
                        name = '', 
                        description = '', 
                        images = [
                            openapi_client.models.originator_image.OriginatorImage(
                                size_key = '', 
                                url = '', )
                            ], 
                        disclaimer = '', 
                        company_uuid = '', 
                        financial_institution_uuid = '', )
                    ],
                pending_responses = [
                    openapi_client.models.pending_response.PendingResponse(
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
                        product_types = [
                            'credit_card'
                            ], )
                    ]
            )
        else:
            return RateTable(
                uuid = '',
                lead_uuid = '',
                credit_card_offers = [
                    openapi_client.models.credit_card_offer.CreditCardOffer(
                        details = openapi_client.models.credit_card_offer_details.CreditCardOfferDetails(
                            card_name = '', 
                            card_image_url = '', 
                            card_purposes = [
                                'balance_transfer'
                                ], 
                            rates_url = '', 
                            max_purchase_apr = 1.337, 
                            min_purchase_apr = 1.337, 
                            purchase_apr_text = '', 
                            max_purchase_intro_apr = 1.337, 
                            min_purchase_intro_apr = 1.337, 
                            purchase_intro_apr_term = 56, 
                            purchase_intro_apr_term_unit = 'day', 
                            purchase_intro_apr_text = '', 
                            max_cash_advance_apr = 1.337, 
                            min_cash_advance_apr = 1.337, 
                            cash_advance_apr_text = '', 
                            max_cash_advance_intro_apr = 1.337, 
                            min_cash_advance_intro_apr = 1.337, 
                            cash_advance_intro_apr_term = 56, 
                            cash_advance_intro_apr_term_unit = 'day', 
                            cash_advance_intro_apr_text = '', 
                            max_balance_transfer_apr = 1.337, 
                            min_balance_transfer_apr = 1.337, 
                            balance_transfer_apr_text = '', 
                            max_balance_transfer_intro_apr = 1.337, 
                            min_balance_transfer_intro_apr = 1.337, 
                            balance_transfer_intro_apr_term = 56, 
                            balance_transfer_intro_apr_term_unit = 'day', 
                            balance_transfer_intro_apr_text = '', 
                            max_annual_fee = 1.337, 
                            min_annual_fee = 1.337, 
                            annual_intro_fee = 1.337, 
                            annual_intro_fee_term = 56, 
                            intro_offer_amount = 1.337, 
                            intro_offer_text = '', 
                            intro_offer_type = 'miles', 
                            additional_details = [
                                ''
                                ], 
                            card_type = 'visa', 
                            minimum_credit_line = 1.337, 
                            minimum_penalty_apr = 1.337, 
                            maximum_penalty_apr = 1.337, 
                            balance_transfer_fee = 1.337, 
                            cash_advance_fee = 1.337, 
                            late_fee = 1.337, 
                            foreign_exchange_fee = 1.337, 
                            account_opening_fee = 1.337, 
                            return_payment_fee = 1.337, 
                            monthly_service_fee = 1.337, 
                            recommended_credit_ratings = [
                                'excellent'
                                ], 
                            pre_qualified = True, 
                            pre_approved = True, 
                            pre_selected = True, 
                            foreign_transaction_fee = 1.337, 
                            card_benefits = [
                                'No Foreign Transaction Fees'
                                ], ), )
                    ],
                loan_offers = [
                    openapi_client.models.loan_offer.LoanOffer(
                        uuid = '', 
                        product_type = 'credit_card', 
                        product_sub_type = 'credit_card', 
                        product_sub_type_disclaimer = '', 
                        url = '', 
                        originator = openapi_client.models.originator.Originator(
                            key = '', 
                            name = '', 
                            description = '', 
                            images = [
                                openapi_client.models.originator_image.OriginatorImage(
                                    size_key = '', 
                                    url = '', )
                                ], 
                            disclaimer = '', 
                            company_uuid = '', 
                            financial_institution_uuid = '', ), 
                        originator_id = '', 
                        pre_qualified = True, 
                        pre_approved = True, 
                        secured = True, 
                        co_applicant = True, 
                        sponsored = True, 
                        max_amount = 56, 
                        min_amount = 56, 
                        term_length = 56, 
                        term_unit = 'day', 
                        display_term_unit = '', 
                        term_description = '', 
                        max_apr = 1.337, 
                        min_apr = 1.337, 
                        mean_apr = 1.337, 
                        apr_type = 'variable', 
                        apr_description = '', 
                        fee_rate = 1.337, 
                        max_fee_rate = 1.337, 
                        min_fee_rate = 1.337, 
                        fee_fixed = 1.337, 
                        max_fee_fixed = 1.337, 
                        min_fee_fixed = 1.337, 
                        allow_prepayment = True, 
                        prepayment_fee = 1.337, 
                        monthly_payment = 1.337, 
                        max_monthly_payment = 1.337, 
                        min_monthly_payment = 1.337, 
                        monthly_payment_description = '', 
                        mean_monthly_payment = 1.337, 
                        max_total_payment = 1.337, 
                        min_total_payment = 1.337, 
                        mean_total_payment = 1.337, 
                        recommendation_score = 1.337, 
                        payout = 1.337, 
                        conversion_probability = 1.337, 
                        terms = '', 
                        amount_prefix = '', )
                    ],
                mortgage_offers = [
                    openapi_client.models.mortgage_offer.MortgageOffer(
                        details = openapi_client.models.mortgage_offer_details.MortgageOfferDetails(
                            interest_rate = 1.337, 
                            loan_type = 'fifteen_year_fixed', 
                            price_adjustment = 1.337, 
                            monthly_payment = 1.337, 
                            net_closing_costs = 1.337, 
                            apr = 1.337, 
                            loan_term = 56, 
                            adjustment_type = 'credits', ), )
                    ],
                savings_offers = [
                    openapi_client.models.savings_offer.SavingsOffer(
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
                            cd_term_length = 56, ), )
                    ],
                special_offers = [
                    openapi_client.models.special_offer.SpecialOffer(
                        uuid = '', 
                        name = '', 
                        desc = '', 
                        url = '', 
                        partner_name = '', 
                        partner_image_url = '', 
                        recommendation_score = 1.337, 
                        payout = 1.337, 
                        product_sub_type = 'credit_card', 
                        disclaimer = '', 
                        financial_institution_uuid = '', )
                    ],
                pending_originators = [
                    openapi_client.models.originator.Originator(
                        key = '', 
                        name = '', 
                        description = '', 
                        images = [
                            openapi_client.models.originator_image.OriginatorImage(
                                size_key = '', 
                                url = '', )
                            ], 
                        disclaimer = '', 
                        company_uuid = '', 
                        financial_institution_uuid = '', )
                    ],
                pending_responses = [
                    openapi_client.models.pending_response.PendingResponse(
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
                        product_types = [
                            'credit_card'
                            ], )
                    ],
        )
        """

    def testRateTable(self):
        """Test RateTable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()