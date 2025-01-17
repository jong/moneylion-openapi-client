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


class CardPurpose(str, Enum):
    """
    Purposes or categories related to a credit card
    """

    """
    allowed enum values
    """
    BALANCE_TRANSFER = 'balance_transfer'
    CASH_BACK = 'cash_back'
    EARNING_REWARDS = 'earning_rewards'
    IMPROVE_CREDIT = 'improve_credit'
    LOW_INTEREST = 'low_interest'
    NEW_TO_CREDIT = 'new_to_credit'
    STUDENT = 'student'
    TRAVEL_INCENTIVES = 'travel_incentives'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of CardPurpose from a JSON string"""
        return cls(json.loads(json_str))


