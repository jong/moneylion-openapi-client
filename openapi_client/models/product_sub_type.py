# coding: utf-8

"""
    Engine by MoneyLion API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.58.0
    Contact: help@engine.tech
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class ProductSubType(str, Enum):
    """
    A type of financial product
    """

    """
    allowed enum values
    """
    CREDIT_CARD = 'credit_card'
    SECURED_CARD = 'secured_card'
    PERSONAL_LOAN = 'personal_loan'
    SECURED_LOAN = 'secured_loan'
    STUDENT_LOAN_REFINANCE = 'student_loan_refinance'
    CO_APPLICANT_LOAN = 'co_applicant_loan'
    LINE_OF_CREDIT = 'line_of_credit'
    AUTOMOBILE_REFINANCE = 'automobile_refinance'
    HOME_EQUITY_LINE_OF_CREDIT = 'home_equity_line_of_credit'
    PURCHASE = 'purchase'
    REFINANCE = 'refinance'
    SAVINGS_ACCOUNT = 'savings_account'
    MONEY_MARKET_ACCOUNT = 'money_market_account'
    CERTIFICATE_OF_DEPOSIT = 'certificate_of_deposit'
    INDIVIDUAL_RETIREMENT_ACCOUNT = 'individual_retirement_account'
    CASH_MANAGEMENT_ACCOUNT = 'cash_management_account'
    HIGH_INTEREST_CHECKING = 'high_interest_checking'
    CHECKING = 'checking'
    ACCIDENTAL_DEATH_BENEFITS = 'accidental_death_benefits'
    TERM_LIFE = 'term_life'
    TERM_LIFE_INSTANT = 'term_life_instant'
    WHOLE_LIFE = 'whole_life'
    DEBT_RELIEF = 'debt_relief'
    INSTALLMENT_LOANS = 'installment_loans'
    CREDIT_BUILDER = 'credit_builder'
    CASH_ADVANCE = 'cash_advance'
    CREDIT_REPAIR = 'credit_repair'
    EDUCATION_OFFERS = 'education_offers'
    EMPLOYMENT_OPPORTUNITY = 'employment_opportunity'
    FINANCIAL_WELLNESS = 'financial_wellness'
    DIRECT_AFFILIATE = 'direct_affiliate'
    OVERDRAFT_PROTECTION = 'overdraft_protection'
    REVENUE_BASED_FINANCING = 'revenue_based_financing'
    UNCATEGORIZED = 'uncategorized'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of ProductSubType from a JSON string"""
        return cls(json.loads(json_str))


