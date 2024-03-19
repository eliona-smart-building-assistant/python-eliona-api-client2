# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.8
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
from eliona.api_client2.models.agent_class import AgentClass
from eliona.api_client2.models.data_subtype import DataSubtype
from typing import Optional, Set
from typing_extensions import Self

class IosysAgentDeviceMapping(BaseModel):
    """
    IosysAgentDeviceMapping
    """ # noqa: E501
    var_class: Optional[AgentClass] = Field(default=None, alias="class")
    id: Optional[StrictInt] = Field(default=None, description="Unique id for the mapping")
    device_id: Optional[StrictInt] = Field(default=None, description="The id of the device the mapping belongs to", alias="deviceId")
    enable: Optional[StrictBool] = Field(default=True, description="Is the mapping enabled or not")
    asset_id: Optional[StrictInt] = Field(default=None, description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: StrictStr = Field(description="Name of the attribute to map")
    ios_var: Optional[StrictStr] = Field(default=None, alias="iosVar")
    ios_type: Optional[StrictStr] = Field(default=None, alias="iosType")
    down: Optional[StrictBool] = False
    scale: Optional[Union[StrictFloat, StrictInt]] = None
    zero: Optional[Union[StrictFloat, StrictInt]] = None
    mask: Optional[List[StrictInt]] = None
    mask_attributes: Optional[List[StrictStr]] = Field(default=None, alias="maskAttributes")
    dead_time: Optional[StrictInt] = Field(default=None, alias="deadTime")
    dead_band: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="deadBand")
    filter: Optional[StrictStr] = None
    tau: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["class", "id", "deviceId", "enable", "assetId", "subtype", "attribute", "iosVar", "iosType", "down", "scale", "zero", "mask", "maskAttributes", "deadTime", "deadBand", "filter", "tau"]

    @field_validator('ios_type')
    def ios_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['INT', 'REAL', 'STRING']):
            raise ValueError("must be one of enum values ('INT', 'REAL', 'STRING')")
        return value

    @field_validator('filter')
    def filter_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['LPF1', 'LPF2', 'MOVA']):
            raise ValueError("must be one of enum values ('LPF1', 'LPF2', 'MOVA')")
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
        """Create an instance of IosysAgentDeviceMapping from a JSON string"""
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
            "device_id",
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

        # set to None if device_id (nullable) is None
        # and model_fields_set contains the field
        if self.device_id is None and "device_id" in self.model_fields_set:
            _dict['deviceId'] = None

        # set to None if asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.asset_id is None and "asset_id" in self.model_fields_set:
            _dict['assetId'] = None

        # set to None if ios_var (nullable) is None
        # and model_fields_set contains the field
        if self.ios_var is None and "ios_var" in self.model_fields_set:
            _dict['iosVar'] = None

        # set to None if ios_type (nullable) is None
        # and model_fields_set contains the field
        if self.ios_type is None and "ios_type" in self.model_fields_set:
            _dict['iosType'] = None

        # set to None if down (nullable) is None
        # and model_fields_set contains the field
        if self.down is None and "down" in self.model_fields_set:
            _dict['down'] = None

        # set to None if scale (nullable) is None
        # and model_fields_set contains the field
        if self.scale is None and "scale" in self.model_fields_set:
            _dict['scale'] = None

        # set to None if zero (nullable) is None
        # and model_fields_set contains the field
        if self.zero is None and "zero" in self.model_fields_set:
            _dict['zero'] = None

        # set to None if mask (nullable) is None
        # and model_fields_set contains the field
        if self.mask is None and "mask" in self.model_fields_set:
            _dict['mask'] = None

        # set to None if mask_attributes (nullable) is None
        # and model_fields_set contains the field
        if self.mask_attributes is None and "mask_attributes" in self.model_fields_set:
            _dict['maskAttributes'] = None

        # set to None if dead_time (nullable) is None
        # and model_fields_set contains the field
        if self.dead_time is None and "dead_time" in self.model_fields_set:
            _dict['deadTime'] = None

        # set to None if dead_band (nullable) is None
        # and model_fields_set contains the field
        if self.dead_band is None and "dead_band" in self.model_fields_set:
            _dict['deadBand'] = None

        # set to None if filter (nullable) is None
        # and model_fields_set contains the field
        if self.filter is None and "filter" in self.model_fields_set:
            _dict['filter'] = None

        # set to None if tau (nullable) is None
        # and model_fields_set contains the field
        if self.tau is None and "tau" in self.model_fields_set:
            _dict['tau'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IosysAgentDeviceMapping from a dict"""
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
            "iosVar": obj.get("iosVar"),
            "iosType": obj.get("iosType"),
            "down": obj.get("down") if obj.get("down") is not None else False,
            "scale": obj.get("scale"),
            "zero": obj.get("zero"),
            "mask": obj.get("mask"),
            "maskAttributes": obj.get("maskAttributes"),
            "deadTime": obj.get("deadTime"),
            "deadBand": obj.get("deadBand"),
            "filter": obj.get("filter"),
            "tau": obj.get("tau")
        })
        return _obj


