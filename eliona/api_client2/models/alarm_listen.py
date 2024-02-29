# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.5
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from eliona.api_client2.models.alarm_priority import AlarmPriority
from eliona.api_client2.models.alarm_rule import AlarmRule
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.models.data_subtype import DataSubtype
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AlarmListen(BaseModel):
    """
    AlarmListen
    """ # noqa: E501
    rule_id: Optional[StrictInt] = Field(default=None, description="The id of the corresponding rule", alias="ruleId")
    asset_id: StrictInt = Field(description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: Optional[StrictStr] = Field(default=None, description="Name of the attribute of the asset type")
    priority: AlarmPriority
    requires_acknowledge: Optional[StrictBool] = Field(default=False, description="Requires the alarm an acknowledgment", alias="requiresAcknowledge")
    value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The value which triggers the alarm")
    timestamp: datetime = Field(description="Timestamp of the latest data change")
    gone_timestamp: Optional[datetime] = Field(default=None, description="Timestamp of the latest data change", alias="goneTimestamp")
    acknowledge_timestamp: Optional[datetime] = Field(default=None, description="Timestamp of the latest data change", alias="acknowledgeTimestamp")
    occurrences: StrictInt = Field(description="How often this alarm is triggered")
    acknowledge_text: Optional[StrictStr] = Field(default=None, description="Text of acknowledgement", alias="acknowledgeText")
    acknowledge_user_id: Optional[StrictStr] = Field(default=None, description="User who acknowledged the alarm", alias="acknowledgeUserId")
    message: Optional[Dict[str, Any]] = Field(default=None, description="Message.yaml texts for alarm")
    asset_info: Optional[Asset] = Field(default=None, alias="assetInfo")
    rule_info: Optional[AlarmRule] = Field(default=None, alias="ruleInfo")
    status_code: Optional[StrictInt] = Field(default=None, description="The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable ", alias="statusCode")
    __properties: ClassVar[List[str]] = ["ruleId", "assetId", "subtype", "attribute", "priority", "requiresAcknowledge", "value", "timestamp", "goneTimestamp", "acknowledgeTimestamp", "occurrences", "acknowledgeText", "acknowledgeUserId", "message", "assetInfo", "ruleInfo", "statusCode"]

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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlarmListen from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        _dict = self.model_dump(
            by_alias=True,
            exclude={
            },
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of asset_info
        if self.asset_info:
            _dict['assetInfo'] = self.asset_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rule_info
        if self.rule_info:
            _dict['ruleInfo'] = self.rule_info.to_dict()
        # set to None if rule_id (nullable) is None
        # and model_fields_set contains the field
        if self.rule_id is None and "rule_id" in self.model_fields_set:
            _dict['ruleId'] = None

        # set to None if attribute (nullable) is None
        # and model_fields_set contains the field
        if self.attribute is None and "attribute" in self.model_fields_set:
            _dict['attribute'] = None

        # set to None if value (nullable) is None
        # and model_fields_set contains the field
        if self.value is None and "value" in self.model_fields_set:
            _dict['value'] = None

        # set to None if gone_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.gone_timestamp is None and "gone_timestamp" in self.model_fields_set:
            _dict['goneTimestamp'] = None

        # set to None if acknowledge_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledge_timestamp is None and "acknowledge_timestamp" in self.model_fields_set:
            _dict['acknowledgeTimestamp'] = None

        # set to None if acknowledge_text (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledge_text is None and "acknowledge_text" in self.model_fields_set:
            _dict['acknowledgeText'] = None

        # set to None if acknowledge_user_id (nullable) is None
        # and model_fields_set contains the field
        if self.acknowledge_user_id is None and "acknowledge_user_id" in self.model_fields_set:
            _dict['acknowledgeUserId'] = None

        # set to None if message (nullable) is None
        # and model_fields_set contains the field
        if self.message is None and "message" in self.model_fields_set:
            _dict['message'] = None

        # set to None if asset_info (nullable) is None
        # and model_fields_set contains the field
        if self.asset_info is None and "asset_info" in self.model_fields_set:
            _dict['assetInfo'] = None

        # set to None if rule_info (nullable) is None
        # and model_fields_set contains the field
        if self.rule_info is None and "rule_info" in self.model_fields_set:
            _dict['ruleInfo'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AlarmListen from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ruleId": obj.get("ruleId"),
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype"),
            "attribute": obj.get("attribute"),
            "priority": obj.get("priority"),
            "requiresAcknowledge": obj.get("requiresAcknowledge") if obj.get("requiresAcknowledge") is not None else False,
            "value": obj.get("value"),
            "timestamp": obj.get("timestamp"),
            "goneTimestamp": obj.get("goneTimestamp"),
            "acknowledgeTimestamp": obj.get("acknowledgeTimestamp"),
            "occurrences": obj.get("occurrences"),
            "acknowledgeText": obj.get("acknowledgeText"),
            "acknowledgeUserId": obj.get("acknowledgeUserId"),
            "message": obj.get("message"),
            "assetInfo": Asset.from_dict(obj.get("assetInfo")) if obj.get("assetInfo") is not None else None,
            "ruleInfo": AlarmRule.from_dict(obj.get("ruleInfo")) if obj.get("ruleInfo") is not None else None,
            "statusCode": obj.get("statusCode")
        })
        return _obj


