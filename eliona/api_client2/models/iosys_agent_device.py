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

class IosysAgentDevice(BaseModel):
    """
    IosysAgentDevice
    """ # noqa: E501
    var_class: Optional[AgentClass] = Field(default=None, alias="class")
    id: Optional[StrictInt] = Field(default=None, description="Unique id for the device")
    agent_id: Optional[StrictInt] = Field(default=None, description="The id of the agent the device belongs to", alias="agentId")
    enable: Optional[StrictBool] = Field(default=False, description="Is the device enabled or not")
    port: Optional[StrictInt] = Field(default=None, description="Port of device")
    certificate: Optional[StrictStr] = Field(default=None, description="Certificate of device")
    key: Optional[StrictStr] = Field(default=None, description="Key for device")
    timeout: Optional[StrictInt] = Field(default=None, description="Time in seconds")
    reconnect: Optional[StrictInt] = Field(default=None, description="Reconnect")
    __properties: ClassVar[List[str]] = ["class", "id", "agentId", "enable", "port", "certificate", "key", "timeout", "reconnect"]

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
        """Create an instance of IosysAgentDevice from a JSON string"""
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

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if certificate (nullable) is None
        # and model_fields_set contains the field
        if self.certificate is None and "certificate" in self.model_fields_set:
            _dict['certificate'] = None

        # set to None if key (nullable) is None
        # and model_fields_set contains the field
        if self.key is None and "key" in self.model_fields_set:
            _dict['key'] = None

        # set to None if timeout (nullable) is None
        # and model_fields_set contains the field
        if self.timeout is None and "timeout" in self.model_fields_set:
            _dict['timeout'] = None

        # set to None if reconnect (nullable) is None
        # and model_fields_set contains the field
        if self.reconnect is None and "reconnect" in self.model_fields_set:
            _dict['reconnect'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IosysAgentDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "class": obj.get("class"),
            "id": obj.get("id"),
            "agentId": obj.get("agentId"),
            "enable": obj.get("enable") if obj.get("enable") is not None else False,
            "port": obj.get("port"),
            "certificate": obj.get("certificate"),
            "key": obj.get("key"),
            "timeout": obj.get("timeout"),
            "reconnect": obj.get("reconnect")
        })
        return _obj


