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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.event_data import EventData
from openapi_client.models.event_type import EventType
from openapi_client.models.product_type import ProductType
from typing import Optional, Set
from typing_extensions import Self

class LeadEvent(BaseModel):
    """
    LeadEvent
    """ # noqa: E501
    id: StrictStr = Field(description="A hash of the `leadUuid`, `eventType` and `eventCreatedAt` which uniquely identifies a leadEvent. ")
    lead_uuid: StrictStr = Field(description="The unique identifier for the associated lead. ", alias="leadUuid")
    lead_created_at: datetime = Field(description="The time that the associated lead was created. ", alias="leadCreatedAt")
    event_type: EventType = Field(alias="eventType")
    event_created_at: datetime = Field(description="The time that the event occurred. ", alias="eventCreatedAt")
    event_data: Optional[EventData] = Field(default=None, alias="eventData")
    amount_in_cents: Optional[StrictInt] = Field(default=None, description="The amount of liquidity provided to the end user by the FI. Only present for some events. ", alias="amountInCents")
    financial_institution_uuid: Optional[StrictStr] = Field(default=None, description="A unique identifier for the associated financial institution. Only present for event types associated with financial institutions. ", alias="financialInstitutionUuid")
    financial_institution_name: Optional[StrictStr] = Field(default=None, description="The name of the associated financial institution. This value is subject to change, so `financialInstitutionUuid` should be used as a stable identifier. Only present for event types associated with financial institutions. ", alias="financialInstitutionName")
    product_type: Optional[ProductType] = Field(default=None, alias="productType")
    is_test: StrictBool = Field(description="Whether a `Lead` was created using a test access token", alias="isTest")
    __properties: ClassVar[List[str]] = ["id", "leadUuid", "leadCreatedAt", "eventType", "eventCreatedAt", "eventData", "amountInCents", "financialInstitutionUuid", "financialInstitutionName", "productType", "isTest"]

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
        """Create an instance of LeadEvent from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of event_data
        if self.event_data:
            _dict['eventData'] = self.event_data.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LeadEvent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "leadUuid": obj.get("leadUuid"),
            "leadCreatedAt": obj.get("leadCreatedAt"),
            "eventType": obj.get("eventType"),
            "eventCreatedAt": obj.get("eventCreatedAt"),
            "eventData": EventData.from_dict(obj["eventData"]) if obj.get("eventData") is not None else None,
            "amountInCents": obj.get("amountInCents"),
            "financialInstitutionUuid": obj.get("financialInstitutionUuid"),
            "financialInstitutionName": obj.get("financialInstitutionName"),
            "productType": obj.get("productType"),
            "isTest": obj.get("isTest")
        })
        return _obj


