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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.credit_card_offer_details import CreditCardOfferDetails
from openapi_client.models.partner import Partner
from openapi_client.models.product_sub_type import ProductSubType
from openapi_client.models.product_type import ProductType
from typing import Optional, Set
from typing_extensions import Self

class CreditCardOffer(BaseModel):
    """
    An offer for a credit card
    """ # noqa: E501
    details: CreditCardOfferDetails
    uuid: StrictStr
    partner: Partner
    marketplace: Optional[Partner] = None
    product_type: ProductType = Field(alias="productType")
    product_sub_type: ProductSubType = Field(alias="productSubType")
    url: StrictStr
    recommendation_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="recommendationScore")
    disclaimer: Optional[StrictStr] = None
    product_sub_type_disclaimer: Optional[StrictStr] = Field(default=None, alias="productSubTypeDisclaimer")
    expires_at: Optional[datetime] = Field(default=None, alias="expiresAt")
    __properties: ClassVar[List[str]] = ["uuid", "partner", "marketplace", "productType", "productSubType", "url", "recommendationScore", "disclaimer", "productSubTypeDisclaimer", "expiresAt"]

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
        """Create an instance of CreditCardOffer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of partner
        if self.partner:
            _dict['partner'] = self.partner.to_dict()
        # override the default output from pydantic by calling `to_dict()` of marketplace
        if self.marketplace:
            _dict['marketplace'] = self.marketplace.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreditCardOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "partner": Partner.from_dict(obj["partner"]) if obj.get("partner") is not None else None,
            "marketplace": Partner.from_dict(obj["marketplace"]) if obj.get("marketplace") is not None else None,
            "productType": obj.get("productType"),
            "productSubType": obj.get("productSubType"),
            "url": obj.get("url"),
            "recommendationScore": obj.get("recommendationScore"),
            "disclaimer": obj.get("disclaimer"),
            "productSubTypeDisclaimer": obj.get("productSubTypeDisclaimer"),
            "expiresAt": obj.get("expiresAt")
        })
        return _obj


