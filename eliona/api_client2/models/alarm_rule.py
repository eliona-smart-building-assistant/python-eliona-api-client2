# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.11
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from eliona.api_client2.models.alarm_priority import AlarmPriority
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.models.data_subtype import DataSubtype
from typing import Optional, Set
from typing_extensions import Self

class AlarmRule(BaseModel):
    """
    Rule for an alarm
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The id of the rule")
    asset_id: StrictInt = Field(description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: StrictStr = Field(description="Name of the attribute of the asset type")
    enable: Optional[StrictBool] = Field(default=True, description="Rule enabled or not")
    priority: AlarmPriority
    requires_acknowledge: Optional[StrictBool] = Field(default=False, description="Requires the alarm an acknowledgment", alias="requiresAcknowledge")
    equal: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Triggers alarm if attribute value equals this value")
    low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Triggers alarm if attribute value is less than value")
    high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Triggers alarm if attribute value is greater than value")
    message: Optional[Dict[str, Any]] = Field(default=None, description="Texts for alarm")
    tags: Optional[List[StrictStr]] = Field(default=None, description="List of associated tags")
    subject: Optional[StrictStr] = Field(default=None, description="The subject for the alarm")
    urldoc: Optional[StrictStr] = Field(default=None, description="The url describing the alarm")
    notify_on: Optional[StrictStr] = Field(default=None, description="Notification", alias="notifyOn")
    dont_mask: Optional[StrictBool] = Field(default=False, description="Do not mask", alias="dontMask")
    check_type: Optional[StrictStr] = Field(default=None, description="Check type", alias="checkType")
    asset_info: Optional[Asset] = Field(default=None, alias="assetInfo")
    __properties: ClassVar[List[str]] = ["id", "assetId", "subtype", "attribute", "enable", "priority", "requiresAcknowledge", "equal", "low", "high", "message", "tags", "subject", "urldoc", "notifyOn", "dontMask", "checkType", "assetInfo"]

    @field_validator('check_type')
    def check_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['limits', 'validity', 'custom']):
            raise ValueError("must be one of enum values ('limits', 'validity', 'custom')")
        return value

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AlarmRule from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of asset_info
        if self.asset_info:
            _dict['assetInfo'] = self.asset_info.to_dict()
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if equal (nullable) is None
        # and model_fields_set contains the field
        if self.equal is None and "equal" in self.model_fields_set:
            _dict['equal'] = None

        # set to None if low (nullable) is None
        # and model_fields_set contains the field
        if self.low is None and "low" in self.model_fields_set:
            _dict['low'] = None

        # set to None if high (nullable) is None
        # and model_fields_set contains the field
        if self.high is None and "high" in self.model_fields_set:
            _dict['high'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if subject (nullable) is None
        # and model_fields_set contains the field
        if self.subject is None and "subject" in self.model_fields_set:
            _dict['subject'] = None

        # set to None if urldoc (nullable) is None
        # and model_fields_set contains the field
        if self.urldoc is None and "urldoc" in self.model_fields_set:
            _dict['urldoc'] = None

        # set to None if notify_on (nullable) is None
        # and model_fields_set contains the field
        if self.notify_on is None and "notify_on" in self.model_fields_set:
            _dict['notifyOn'] = None

        # set to None if dont_mask (nullable) is None
        # and model_fields_set contains the field
        if self.dont_mask is None and "dont_mask" in self.model_fields_set:
            _dict['dontMask'] = None

        # set to None if check_type (nullable) is None
        # and model_fields_set contains the field
        if self.check_type is None and "check_type" in self.model_fields_set:
            _dict['checkType'] = None

        # set to None if asset_info (nullable) is None
        # and model_fields_set contains the field
        if self.asset_info is None and "asset_info" in self.model_fields_set:
            _dict['assetInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AlarmRule from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype"),
            "attribute": obj.get("attribute"),
            "enable": obj.get("enable") if obj.get("enable") is not None else True,
            "priority": obj.get("priority"),
            "requiresAcknowledge": obj.get("requiresAcknowledge") if obj.get("requiresAcknowledge") is not None else False,
            "equal": obj.get("equal"),
            "low": obj.get("low"),
            "high": obj.get("high"),
            "message": obj.get("message"),
            "tags": obj.get("tags"),
            "subject": obj.get("subject"),
            "urldoc": obj.get("urldoc"),
            "notifyOn": obj.get("notifyOn"),
            "dontMask": obj.get("dontMask") if obj.get("dontMask") is not None else False,
            "checkType": obj.get("checkType"),
            "assetInfo": Asset.from_dict(obj["assetInfo"]) if obj.get("assetInfo") is not None else None
        })
        return _obj


