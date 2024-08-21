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


class MortgageLoanType(str, Enum):
    """
    MortgageLoanType
    """

    """
    allowed enum values
    """
    FIFTEEN_YEAR_FIXED = 'fifteen_year_fixed'
    THIRTY_YEAR_FIXED = 'thirty_year_fixed'
    FIVE_ONE_ADJUSTABLE = 'five_one_adjustable'
    SEVEN_ONE_ADJUSTABLE = 'seven_one_adjustable'
    TEN_ONE_ADJUSTABLE = 'ten_one_adjustable'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of MortgageLoanType from a JSON string"""
        return cls(json.loads(json_str))

