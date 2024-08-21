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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from openapi_client.models.loan_purpose import LoanPurpose
from openapi_client.models.provided_credit_rating import ProvidedCreditRating
from openapi_client.models.state import State
from typing import Optional, Set
from typing_extensions import Self

class LoanReportCreateData(BaseModel):
    """
    LoanReportCreateData
    """ # noqa: E501
    annual_income: StrictInt = Field(description="The user's annual income in dollars.", alias="annualIncome")
    credit_rating: ProvidedCreditRating = Field(description="The user's credit score range.", alias="creditRating")
    total_debt: Optional[StrictInt] = Field(default=None, description="The user's total debt in dollars.", alias="totalDebt")
    count_of_derogatories: Optional[StrictInt] = Field(default=None, description="The number of derogatory accounts listed on the user's credit report.", alias="countOfDerogatories")
    state: Optional[State] = Field(default=None, description="The user's state of residence.")
    loan_purpose: Optional[LoanPurpose] = Field(default=None, description="The reason for the loan.", alias="loanPurpose")
    loan_amount: Optional[StrictInt] = Field(default=None, description="The size of the the loan.", alias="loanAmount")
    __properties: ClassVar[List[str]] = ["annualIncome", "creditRating", "totalDebt", "countOfDerogatories", "state", "loanPurpose", "loanAmount"]

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
        """Create an instance of LoanReportCreateData from a JSON string"""
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
        """Create an instance of LoanReportCreateData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "annualIncome": obj.get("annualIncome"),
            "creditRating": obj.get("creditRating"),
            "totalDebt": obj.get("totalDebt"),
            "countOfDerogatories": obj.get("countOfDerogatories"),
            "state": obj.get("state"),
            "loanPurpose": obj.get("loanPurpose"),
            "loanAmount": obj.get("loanAmount")
        })
        return _obj

