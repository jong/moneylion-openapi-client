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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.product_sub_type import ProductSubType
from typing import Optional, Set
from typing_extensions import Self

class SpecialOffer(BaseModel):
    """
    SpecialOffer
    """ # noqa: E501
    uuid: StrictStr
    name: StrictStr
    desc: StrictStr = Field(description="Description")
    url: StrictStr
    partner_name: StrictStr = Field(alias="partnerName")
    partner_image_url: StrictStr = Field(alias="partnerImageUrl")
    recommendation_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="recommendationScore")
    payout: Optional[Union[StrictFloat, StrictInt]] = None
    product_sub_type: ProductSubType = Field(alias="productSubType")
    disclaimer: Optional[StrictStr] = None
    financial_institution_uuid: Optional[StrictStr] = Field(default=None, description="A unique identifier for the associated financial institution. Only present for event types associated with financial institutions. ", alias="financialInstitutionUuid")
    __properties: ClassVar[List[str]] = ["uuid", "name", "desc", "url", "partnerName", "partnerImageUrl", "recommendationScore", "payout", "productSubType", "disclaimer", "financialInstitutionUuid"]

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
        """Create an instance of SpecialOffer from a JSON string"""
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
        """Create an instance of SpecialOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "name": obj.get("name"),
            "desc": obj.get("desc"),
            "url": obj.get("url"),
            "partnerName": obj.get("partnerName"),
            "partnerImageUrl": obj.get("partnerImageUrl"),
            "recommendationScore": obj.get("recommendationScore"),
            "payout": obj.get("payout"),
            "productSubType": obj.get("productSubType"),
            "disclaimer": obj.get("disclaimer"),
            "financialInstitutionUuid": obj.get("financialInstitutionUuid")
        })
        return _obj

