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

from pydantic import BaseModel, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from eliona.api_client2.models.data_subtype import DataSubtype
from typing import Optional, Set
from typing_extensions import Self

class Aggregation(BaseModel):
    """
    Defines the aggregation of data points
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="ID of the aggregation")
    asset_id: StrictInt = Field(description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: Optional[StrictStr] = Field(default=None, description="Name of the attribute which holds the data points")
    mode: StrictStr = Field(description="Calculation mode")
    raster: Optional[StrictStr] = Field(default=None, description="calculation interval")
    __properties: ClassVar[List[str]] = ["id", "assetId", "subtype", "attribute", "mode", "raster"]

    @field_validator('mode')
    def mode_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['avg', 'sum', 'cusum', 'avg-on-change']):
            raise ValueError("must be one of enum values ('avg', 'sum', 'cusum', 'avg-on-change')")
        return value

    @field_validator('raster')
    def raster_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10', 'S12', 'S15', 'S20', 'S30', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M10', 'M12', 'M15', 'M20', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12', 'DAY', 'WEEK', 'MONTH', 'QUARTER', 'YEAR', 'DECADE', 'CENTURY']):
            raise ValueError("must be one of enum values ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10', 'S12', 'S15', 'S20', 'S30', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M10', 'M12', 'M15', 'M20', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12', 'DAY', 'WEEK', 'MONTH', 'QUARTER', 'YEAR', 'DECADE', 'CENTURY')")
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
        """Create an instance of Aggregation from a JSON string"""
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
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if raster (nullable) is None
        # and model_fields_set contains the field
        if self.raster is None and "raster" in self.model_fields_set:
            _dict['raster'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Aggregation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype"),
            "attribute": obj.get("attribute"),
            "mode": obj.get("mode"),
            "raster": obj.get("raster")
        })
        return _obj


