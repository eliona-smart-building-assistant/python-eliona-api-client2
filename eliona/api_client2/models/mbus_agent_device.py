# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.12
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from eliona.api_client2.models.agent_class import AgentClass
from typing import Optional, Set
from typing_extensions import Self

class MbusAgentDevice(BaseModel):
    """
    MbusAgentDevice
    """ # noqa: E501
    var_class: Optional[AgentClass] = Field(default=None, alias="class")
    id: Optional[StrictInt] = Field(default=None, description="Unique id for the device")
    agent_id: Optional[StrictInt] = Field(default=None, description="The id of the agent the device belongs to", alias="agentId")
    enable: Optional[StrictBool] = Field(default=False, description="Is the device enabled or not")
    manufacturer: Optional[StrictStr] = None
    model: Optional[StrictStr] = None
    address: Optional[StrictInt] = None
    sec_address: Optional[StrictStr] = Field(default=None, alias="secAddress")
    raster: Optional[StrictStr] = None
    max_fail: Optional[StrictInt] = Field(default=4, alias="maxFail")
    max_retry: Optional[StrictInt] = Field(default=3, alias="maxRetry")
    send_nke: Optional[StrictBool] = Field(default=False, alias="sendNke")
    app_reset_subcode: Optional[StrictInt] = Field(default=None, alias="appResetSubcode")
    multi_frames: Optional[StrictInt] = Field(default=0, alias="multiFrames")
    __properties: ClassVar[List[str]] = ["class", "id", "agentId", "enable", "manufacturer", "model", "address", "secAddress", "raster", "maxFail", "maxRetry", "sendNke", "appResetSubcode", "multiFrames"]

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
        """Create an instance of MbusAgentDevice from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "agent_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if var_class (nullable) is None
        # and model_fields_set contains the field
        if self.var_class is None and "var_class" in self.model_fields_set:
            _dict['class'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if agent_id (nullable) is None
        # and model_fields_set contains the field
        if self.agent_id is None and "agent_id" in self.model_fields_set:
            _dict['agentId'] = None

        # set to None if manufacturer (nullable) is None
        # and model_fields_set contains the field
        if self.manufacturer is None and "manufacturer" in self.model_fields_set:
            _dict['manufacturer'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if address (nullable) is None
        # and model_fields_set contains the field
        if self.address is None and "address" in self.model_fields_set:
            _dict['address'] = None

        # set to None if sec_address (nullable) is None
        # and model_fields_set contains the field
        if self.sec_address is None and "sec_address" in self.model_fields_set:
            _dict['secAddress'] = None

        # set to None if raster (nullable) is None
        # and model_fields_set contains the field
        if self.raster is None and "raster" in self.model_fields_set:
            _dict['raster'] = None

        # set to None if max_fail (nullable) is None
        # and model_fields_set contains the field
        if self.max_fail is None and "max_fail" in self.model_fields_set:
            _dict['maxFail'] = None

        # set to None if max_retry (nullable) is None
        # and model_fields_set contains the field
        if self.max_retry is None and "max_retry" in self.model_fields_set:
            _dict['maxRetry'] = None

        # set to None if send_nke (nullable) is None
        # and model_fields_set contains the field
        if self.send_nke is None and "send_nke" in self.model_fields_set:
            _dict['sendNke'] = None

        # set to None if app_reset_subcode (nullable) is None
        # and model_fields_set contains the field
        if self.app_reset_subcode is None and "app_reset_subcode" in self.model_fields_set:
            _dict['appResetSubcode'] = None

        # set to None if multi_frames (nullable) is None
        # and model_fields_set contains the field
        if self.multi_frames is None and "multi_frames" in self.model_fields_set:
            _dict['multiFrames'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MbusAgentDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "class": obj.get("class"),
            "id": obj.get("id"),
            "agentId": obj.get("agentId"),
            "enable": obj.get("enable") if obj.get("enable") is not None else False,
            "manufacturer": obj.get("manufacturer"),
            "model": obj.get("model"),
            "address": obj.get("address"),
            "secAddress": obj.get("secAddress"),
            "raster": obj.get("raster"),
            "maxFail": obj.get("maxFail") if obj.get("maxFail") is not None else 4,
            "maxRetry": obj.get("maxRetry") if obj.get("maxRetry") is not None else 3,
            "sendNke": obj.get("sendNke") if obj.get("sendNke") is not None else False,
            "appResetSubcode": obj.get("appResetSubcode"),
            "multiFrames": obj.get("multiFrames") if obj.get("multiFrames") is not None else 0
        })
        return _obj


