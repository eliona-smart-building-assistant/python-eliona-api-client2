# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.0
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from pydantic import Field
from eliona.api_client2.models.agent_class import AgentClass
from eliona.api_client2.models.data_subtype import DataSubtype
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class MbusAgentDeviceMapping(BaseModel):
    """
    MbusAgentDeviceMapping
    """ # noqa: E501
    var_class: Optional[AgentClass] = Field(default=None, alias="class")
    id: Optional[StrictInt] = Field(default=None, description="Unique id for the mapping")
    device_id: Optional[StrictInt] = Field(default=None, description="The id of the device the mapping belongs to", alias="deviceId")
    enable: Optional[StrictBool] = Field(default=True, description="Is the mapping enabled or not")
    asset_id: Optional[StrictInt] = Field(default=None, description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: StrictStr = Field(description="Name of the attribute to map")
    field: Optional[StrictInt] = None
    scale: Optional[Union[StrictFloat, StrictInt]] = None
    zero: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["class", "id", "deviceId", "enable", "assetId", "subtype", "attribute", "field", "scale", "zero"]

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
        """Create an instance of MbusAgentDeviceMapping from a JSON string"""
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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
                "device_id",
            },
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

        # set to None if device_id (nullable) is None
        # and model_fields_set contains the field
        if self.device_id is None and "device_id" in self.model_fields_set:
            _dict['deviceId'] = None

        # set to None if asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.asset_id is None and "asset_id" in self.model_fields_set:
            _dict['assetId'] = None

        # set to None if field (nullable) is None
        # and model_fields_set contains the field
        if self.field is None and "field" in self.model_fields_set:
            _dict['field'] = None

        # set to None if scale (nullable) is None
        # and model_fields_set contains the field
        if self.scale is None and "scale" in self.model_fields_set:
            _dict['scale'] = None

        # set to None if zero (nullable) is None
        # and model_fields_set contains the field
        if self.zero is None and "zero" in self.model_fields_set:
            _dict['zero'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of MbusAgentDeviceMapping from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "class": obj.get("class"),
            "id": obj.get("id"),
            "deviceId": obj.get("deviceId"),
            "enable": obj.get("enable") if obj.get("enable") is not None else True,
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype"),
            "attribute": obj.get("attribute"),
            "field": obj.get("field"),
            "scale": obj.get("scale"),
            "zero": obj.get("zero")
        })
        return _obj


