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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from openapi_client.models.personal_reference_relation_type import PersonalReferenceRelationType
from typing import Optional, Set
from typing_extensions import Self

class PersonalReferenceInformation(BaseModel):
    """
    PersonalReferenceInformation
    """ # noqa: E501
    first_name: Optional[StrictStr] = Field(default=None, description="The first name of the personal reference supplied by the lead", alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, description="The last name of the personal reference supplied by the lead", alias="lastName")
    primary_phone: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The phone number of the personal reference supplied by the lead", alias="primaryPhone")
    relation_type: Optional[PersonalReferenceRelationType] = Field(default=None, alias="relationType")
    __properties: ClassVar[List[str]] = ["firstName", "lastName", "primaryPhone", "relationType"]

    @field_validator('primary_phone')
    def primary_phone_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"^1?\d{10}$", value):
            raise ValueError(r"must validate the regular expression /^1?\d{10}$/")
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
        """Create an instance of PersonalReferenceInformation from a JSON string"""
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
        """Create an instance of PersonalReferenceInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "primaryPhone": obj.get("primaryPhone"),
            "relationType": obj.get("relationType")
        })
        return _obj


