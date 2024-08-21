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


class IdType(str, Enum):
    """
    IdType
    """

    """
    allowed enum values
    """
    DRIVER_LICENSE = 'driver_license'
    STATE_ID = 'state_id'
    PASSPORT = 'passport'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of IdType from a JSON string"""
        return cls(json.loads(json_str))


