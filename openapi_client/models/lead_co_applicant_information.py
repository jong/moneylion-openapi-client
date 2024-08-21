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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class LeadCoApplicantInformation(BaseModel):
    """
    The personal information of a co-applicant that may be considered in the underwriting and approval of a loan. 
    """ # noqa: E501
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    date_of_birth: Optional[date] = Field(default=None, alias="dateOfBirth")
    annual_income: Optional[StrictInt] = Field(default=None, alias="annualIncome")
    street_address1: Optional[StrictStr] = Field(default=None, description="Street address (primary address line)", alias="streetAddress1")
    street_address2: Optional[StrictStr] = Field(default=None, description="Secondary address line", alias="streetAddress2")
    city: Optional[StrictStr] = None
    state: Optional[State] = None
    zipcode: Optional[Annotated[str, Field(strict=True)]] = None
    __properties: ClassVar[List[str]] = ["firstName", "lastName", "dateOfBirth", "annualIncome", "streetAddress1", "streetAddress2", "city", "state", "zipcode"]

    @field_validator('zipcode')
    def zipcode_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^\d{5}([-\s]\d{4})?$", value):
            raise ValueError(r"must validate the regular expression /^\d{5}([-\s]\d{4})?$/")
        return value

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
        """Create an instance of LeadCoApplicantInformation from a JSON string"""
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
        """Create an instance of LeadCoApplicantInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "dateOfBirth": obj.get("dateOfBirth"),
            "annualIncome": obj.get("annualIncome"),
            "streetAddress1": obj.get("streetAddress1"),
            "streetAddress2": obj.get("streetAddress2"),
            "city": obj.get("city"),
            "state": obj.get("state"),
            "zipcode": obj.get("zipcode")
        })
        return _obj


