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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from openapi_client.models.apr_type import AprType
from openapi_client.models.originator import Originator
from openapi_client.models.product_sub_type import ProductSubType
from openapi_client.models.product_type import ProductType
from openapi_client.models.term_unit import TermUnit
from typing import Optional, Set
from typing_extensions import Self

class LoanOffer(BaseModel):
    """
    LoanOffer
    """ # noqa: E501
    uuid: StrictStr
    product_type: ProductType = Field(alias="productType")
    product_sub_type: ProductSubType = Field(alias="productSubType")
    product_sub_type_disclaimer: Optional[StrictStr] = Field(default=None, alias="productSubTypeDisclaimer")
    url: Optional[StrictStr] = None
    originator: Originator
    originator_id: Optional[StrictStr] = Field(default=None, alias="originatorId")
    pre_qualified: StrictBool = Field(alias="preQualified")
    pre_approved: StrictBool = Field(alias="preApproved")
    secured: StrictBool
    co_applicant: StrictBool = Field(alias="coApplicant")
    sponsored: StrictBool
    max_amount: StrictInt = Field(alias="maxAmount")
    min_amount: Optional[StrictInt] = Field(default=None, alias="minAmount")
    term_length: Optional[StrictInt] = Field(default=None, alias="termLength")
    term_unit: Optional[TermUnit] = Field(default=None, alias="termUnit")
    display_term_unit: Optional[StrictStr] = Field(default=None, alias="displayTermUnit")
    term_description: Optional[StrictStr] = Field(default=None, alias="termDescription")
    max_apr: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxApr")
    min_apr: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minApr")
    mean_apr: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="meanApr")
    apr_type: AprType = Field(alias="aprType")
    apr_description: Optional[StrictStr] = Field(default=None, alias="aprDescription")
    fee_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum percent of loan amount fee for an offer. `maxFeeRate` should be used instead", alias="feeRate")
    max_fee_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxFeeRate")
    min_fee_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minFeeRate")
    fee_fixed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The maximum fee, in dollars, for an offer. `maxFeeFixed` should be used instead", alias="feeFixed")
    max_fee_fixed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxFeeFixed")
    min_fee_fixed: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minFeeFixed")
    allow_prepayment: StrictBool = Field(alias="allowPrepayment")
    prepayment_fee: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="prepaymentFee")
    monthly_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The estimated maximum monthly payment, in dollars, for an offer. `maxMonthlyPayment` should be used instead", alias="monthlyPayment")
    max_monthly_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxMonthlyPayment")
    min_monthly_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minMonthlyPayment")
    monthly_payment_description: Optional[StrictStr] = Field(default=None, alias="monthlyPaymentDescription")
    mean_monthly_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="meanMonthlyPayment")
    max_total_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="maxTotalPayment")
    min_total_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="minTotalPayment")
    mean_total_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="meanTotalPayment")
    recommendation_score: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="recommendationScore")
    payout: Optional[Union[StrictFloat, StrictInt]] = None
    conversion_probability: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="conversionProbability")
    terms: Optional[StrictStr] = None
    amount_prefix: Optional[StrictStr] = Field(default=None, description="Some loan offers require a prefix (e.g. `up to*`) to be displayed to the left of the displayed loan amount. This is a nullable field that may be up to six characters long.", alias="amountPrefix")
    __properties: ClassVar[List[str]] = ["uuid", "productType", "productSubType", "productSubTypeDisclaimer", "url", "originator", "originatorId", "preQualified", "preApproved", "secured", "coApplicant", "sponsored", "maxAmount", "minAmount", "termLength", "termUnit", "displayTermUnit", "termDescription", "maxApr", "minApr", "meanApr", "aprType", "aprDescription", "feeRate", "maxFeeRate", "minFeeRate", "feeFixed", "maxFeeFixed", "minFeeFixed", "allowPrepayment", "prepaymentFee", "monthlyPayment", "maxMonthlyPayment", "minMonthlyPayment", "monthlyPaymentDescription", "meanMonthlyPayment", "maxTotalPayment", "minTotalPayment", "meanTotalPayment", "recommendationScore", "payout", "conversionProbability", "terms", "amountPrefix"]

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
        """Create an instance of LoanOffer from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of originator
        if self.originator:
            _dict['originator'] = self.originator.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LoanOffer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "uuid": obj.get("uuid"),
            "productType": obj.get("productType"),
            "productSubType": obj.get("productSubType"),
            "productSubTypeDisclaimer": obj.get("productSubTypeDisclaimer"),
            "url": obj.get("url"),
            "originator": Originator.from_dict(obj["originator"]) if obj.get("originator") is not None else None,
            "originatorId": obj.get("originatorId"),
            "preQualified": obj.get("preQualified"),
            "preApproved": obj.get("preApproved"),
            "secured": obj.get("secured"),
            "coApplicant": obj.get("coApplicant"),
            "sponsored": obj.get("sponsored"),
            "maxAmount": obj.get("maxAmount"),
            "minAmount": obj.get("minAmount"),
            "termLength": obj.get("termLength"),
            "termUnit": obj.get("termUnit"),
            "displayTermUnit": obj.get("displayTermUnit"),
            "termDescription": obj.get("termDescription"),
            "maxApr": obj.get("maxApr"),
            "minApr": obj.get("minApr"),
            "meanApr": obj.get("meanApr"),
            "aprType": obj.get("aprType"),
            "aprDescription": obj.get("aprDescription"),
            "feeRate": obj.get("feeRate"),
            "maxFeeRate": obj.get("maxFeeRate"),
            "minFeeRate": obj.get("minFeeRate"),
            "feeFixed": obj.get("feeFixed"),
            "maxFeeFixed": obj.get("maxFeeFixed"),
            "minFeeFixed": obj.get("minFeeFixed"),
            "allowPrepayment": obj.get("allowPrepayment"),
            "prepaymentFee": obj.get("prepaymentFee"),
            "monthlyPayment": obj.get("monthlyPayment"),
            "maxMonthlyPayment": obj.get("maxMonthlyPayment"),
            "minMonthlyPayment": obj.get("minMonthlyPayment"),
            "monthlyPaymentDescription": obj.get("monthlyPaymentDescription"),
            "meanMonthlyPayment": obj.get("meanMonthlyPayment"),
            "maxTotalPayment": obj.get("maxTotalPayment"),
            "minTotalPayment": obj.get("minTotalPayment"),
            "meanTotalPayment": obj.get("meanTotalPayment"),
            "recommendationScore": obj.get("recommendationScore"),
            "payout": obj.get("payout"),
            "conversionProbability": obj.get("conversionProbability"),
            "terms": obj.get("terms"),
            "amountPrefix": obj.get("amountPrefix")
        })
        return _obj

