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
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class LeadEmploymentInformation(BaseModel):
    """
    LeadEmploymentInformation
    """ # noqa: E501
    employer_name: Optional[StrictStr] = Field(default=None, alias="employerName")
    employer_address: Optional[StrictStr] = Field(default=None, alias="employerAddress")
    employer_address2: Optional[StrictStr] = Field(default=None, alias="employerAddress2")
    employer_city: Optional[StrictStr] = Field(default=None, alias="employerCity")
    employer_phone: Optional[StrictStr] = Field(default=None, alias="employerPhone")
    employer_state: Optional[StrictStr] = Field(default=None, alias="employerState")
    employer_zip: Optional[StrictStr] = Field(default=None, alias="employerZip")
    job_title: Optional[StrictStr] = Field(default=None, alias="jobTitle")
    months_employed: Optional[StrictInt] = Field(default=None, alias="monthsEmployed")
    direct_deposit: Optional[StrictBool] = Field(default=None, description="Whether a `Lead` uses direct deposit for their salary", alias="directDeposit")
    pay_date1: Optional[date] = Field(default=None, alias="payDate1")
    pay_date2: Optional[date] = Field(default=None, alias="payDate2")
    start_date: Optional[date] = Field(default=None, description="The date the lead started working at their current employer (YYYY-MM-DD)", alias="startDate")
    __properties: ClassVar[List[str]] = ["employerName", "employerAddress", "employerAddress2", "employerCity", "employerPhone", "employerState", "employerZip", "jobTitle", "monthsEmployed", "directDeposit", "payDate1", "payDate2", "startDate"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of LeadEmploymentInformation from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeadEmploymentInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "employerName": obj.get("employerName"),
            "employerAddress": obj.get("employerAddress"),
            "employerAddress2": obj.get("employerAddress2"),
            "employerCity": obj.get("employerCity"),
            "employerPhone": obj.get("employerPhone"),
            "employerState": obj.get("employerState"),
            "employerZip": obj.get("employerZip"),
            "jobTitle": obj.get("jobTitle"),
            "monthsEmployed": obj.get("monthsEmployed"),
            "directDeposit": obj.get("directDeposit"),
            "payDate1": obj.get("payDate1"),
            "payDate2": obj.get("payDate2"),
            "startDate": obj.get("startDate")
        })
        return _obj


