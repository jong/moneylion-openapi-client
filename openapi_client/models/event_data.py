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
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from openapi_client.models.api_approved_event_data import ApiApprovedEventData
from openapi_client.models.api_rejected_event_data import ApiRejectedEventData
from openapi_client.models.applied_event_data import AppliedEventData
from openapi_client.models.approved_event_data import ApprovedEventData
from openapi_client.models.conversion_event_data import ConversionEventData
from openapi_client.models.funded_event_data import FundedEventData
from openapi_client.models.listed_event_data import ListedEventData
from openapi_client.models.offer_clicked_event_data import OfferClickedEventData
from openapi_client.models.opened_event_data import OpenedEventData
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

EVENTDATA_ONE_OF_SCHEMAS = ["ApiApprovedEventData", "ApiRejectedEventData", "AppliedEventData", "ApprovedEventData", "ConversionEventData", "FundedEventData", "ListedEventData", "OfferClickedEventData", "OpenedEventData"]

class EventData(BaseModel):
    """
    EventData
    """
    # data type: ApiApprovedEventData
    oneof_schema_1_validator: Optional[ApiApprovedEventData] = None
    # data type: ApiRejectedEventData
    oneof_schema_2_validator: Optional[ApiRejectedEventData] = None
    # data type: AppliedEventData
    oneof_schema_3_validator: Optional[AppliedEventData] = None
    # data type: ApprovedEventData
    oneof_schema_4_validator: Optional[ApprovedEventData] = None
    # data type: ConversionEventData
    oneof_schema_5_validator: Optional[ConversionEventData] = None
    # data type: FundedEventData
    oneof_schema_6_validator: Optional[FundedEventData] = None
    # data type: ListedEventData
    oneof_schema_7_validator: Optional[ListedEventData] = None
    # data type: OfferClickedEventData
    oneof_schema_8_validator: Optional[OfferClickedEventData] = None
    # data type: OpenedEventData
    oneof_schema_9_validator: Optional[OpenedEventData] = None
    actual_instance: Optional[Union[ApiApprovedEventData, ApiRejectedEventData, AppliedEventData, ApprovedEventData, ConversionEventData, FundedEventData, ListedEventData, OfferClickedEventData, OpenedEventData]] = None
    one_of_schemas: Set[str] = { "ApiApprovedEventData", "ApiRejectedEventData", "AppliedEventData", "ApprovedEventData", "ConversionEventData", "FundedEventData", "ListedEventData", "OfferClickedEventData", "OpenedEventData" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = EventData.model_construct()
        error_messages = []
        match = 0
        # validate data type: ApiApprovedEventData
        if not isinstance(v, ApiApprovedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiApprovedEventData`")
        else:
            match += 1
        # validate data type: ApiRejectedEventData
        if not isinstance(v, ApiRejectedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApiRejectedEventData`")
        else:
            match += 1
        # validate data type: AppliedEventData
        if not isinstance(v, AppliedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `AppliedEventData`")
        else:
            match += 1
        # validate data type: ApprovedEventData
        if not isinstance(v, ApprovedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ApprovedEventData`")
        else:
            match += 1
        # validate data type: ConversionEventData
        if not isinstance(v, ConversionEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ConversionEventData`")
        else:
            match += 1
        # validate data type: FundedEventData
        if not isinstance(v, FundedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `FundedEventData`")
        else:
            match += 1
        # validate data type: ListedEventData
        if not isinstance(v, ListedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ListedEventData`")
        else:
            match += 1
        # validate data type: OfferClickedEventData
        if not isinstance(v, OfferClickedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OfferClickedEventData`")
        else:
            match += 1
        # validate data type: OpenedEventData
        if not isinstance(v, OpenedEventData):
            error_messages.append(f"Error! Input type `{type(v)}` is not `OpenedEventData`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in EventData with oneOf schemas: ApiApprovedEventData, ApiRejectedEventData, AppliedEventData, ApprovedEventData, ConversionEventData, FundedEventData, ListedEventData, OfferClickedEventData, OpenedEventData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in EventData with oneOf schemas: ApiApprovedEventData, ApiRejectedEventData, AppliedEventData, ApprovedEventData, ConversionEventData, FundedEventData, ListedEventData, OfferClickedEventData, OpenedEventData. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ApiApprovedEventData
        try:
            instance.actual_instance = ApiApprovedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApiRejectedEventData
        try:
            instance.actual_instance = ApiRejectedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into AppliedEventData
        try:
            instance.actual_instance = AppliedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ApprovedEventData
        try:
            instance.actual_instance = ApprovedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ConversionEventData
        try:
            instance.actual_instance = ConversionEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into FundedEventData
        try:
            instance.actual_instance = FundedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into ListedEventData
        try:
            instance.actual_instance = ListedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OfferClickedEventData
        try:
            instance.actual_instance = OfferClickedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into OpenedEventData
        try:
            instance.actual_instance = OpenedEventData.from_json(json_str)
            match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into EventData with oneOf schemas: ApiApprovedEventData, ApiRejectedEventData, AppliedEventData, ApprovedEventData, ConversionEventData, FundedEventData, ListedEventData, OfferClickedEventData, OpenedEventData. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into EventData with oneOf schemas: ApiApprovedEventData, ApiRejectedEventData, AppliedEventData, ApprovedEventData, ConversionEventData, FundedEventData, ListedEventData, OfferClickedEventData, OpenedEventData. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ApiApprovedEventData, ApiRejectedEventData, AppliedEventData, ApprovedEventData, ConversionEventData, FundedEventData, ListedEventData, OfferClickedEventData, OpenedEventData]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())

