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
from typing_extensions import Annotated
from eliona.api_client2.models.data_subtype import DataSubtype
from eliona.api_client2.models.translation import Translation
from typing import Optional, Set
from typing_extensions import Self

class AssetTypeAttribute(BaseModel):
    """
    Named attribute to store data of assets
    """ # noqa: E501
    asset_type_name: Optional[StrictStr] = Field(default=None, description="The unique name for the asset type", alias="assetTypeName")
    name: StrictStr = Field(description="Unique key of asset data")
    subtype: DataSubtype
    type: Optional[StrictStr] = Field(default=None, description="Name of the type for this attribute: air_quality, battery-voltage, brightness, co2, current, device-info, device-status, energy, flow, frequency, humidity, inputs-and-switches, level, motion, operating-status, people-count, power, presence, pressure, temperature, vehicle-detector, voltage, weather, voc")
    enable: Optional[StrictBool] = Field(default=True, description="Is data active or not")
    translation: Optional[Translation] = None
    unit: Optional[StrictStr] = Field(default=None, description="Physical unit of numeric data")
    precision: Optional[Annotated[int, Field(le=20, strict=True, ge=-20)]] = Field(default=None, description="Number of decimal places")
    min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Lower limit")
    max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Upper limit")
    aggregation_mode: Optional[StrictStr] = Field(default=None, description="Aggregation calculation mode", alias="aggregationMode")
    aggregation_rasters: Optional[List[StrictStr]] = Field(default=None, alias="aggregationRasters")
    viewer: Optional[StrictBool] = Field(default=False, description="Should the attribute be displayed in viewer")
    ar: Optional[StrictBool] = Field(default=False, description="Should the attribute be displayed in AR")
    sequence: Optional[StrictInt] = Field(default=None, description="Sequence in AR display")
    virtual: Optional[StrictBool] = Field(default=None, description="Is the attribute virtual or not")
    formula: Optional[StrictStr] = Field(default=None, description="calculation rule to calculate the value for this attribute")
    scale: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value scale")
    zero: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="value scale")
    map: Optional[List[Dict[str, Any]]] = Field(default=None, description="list of mapping between value and custom text")
    source_path: Optional[List[StrictStr]] = Field(default=None, description="source path for attribute value", alias="sourcePath")
    is_digital: Optional[StrictBool] = Field(default=None, description="is attribute digital", alias="isDigital")
    __properties: ClassVar[List[str]] = ["assetTypeName", "name", "subtype", "type", "enable", "translation", "unit", "precision", "min", "max", "aggregationMode", "aggregationRasters", "viewer", "ar", "sequence", "virtual", "formula", "scale", "zero", "map", "sourcePath", "isDigital"]

    @field_validator('aggregation_mode')
    def aggregation_mode_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['avg', 'sum', 'cusum', 'avg-on-change']):
            raise ValueError("must be one of enum values ('avg', 'sum', 'cusum', 'avg-on-change')")
        return value

    @field_validator('aggregation_rasters')
    def aggregation_rasters_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        for i in value:
            if i not in set(['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10', 'S12', 'S15', 'S20', 'S30', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M10', 'M12', 'M15', 'M20', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12', 'DAY', 'WEEK', 'MONTH', 'QUARTER', 'YEAR', 'DECADE', 'CENTURY']):
                raise ValueError("each list item must be one of ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10', 'S12', 'S15', 'S20', 'S30', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M10', 'M12', 'M15', 'M20', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12', 'DAY', 'WEEK', 'MONTH', 'QUARTER', 'YEAR', 'DECADE', 'CENTURY')")
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
        """Create an instance of AssetTypeAttribute from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of translation
        if self.translation:
            _dict['translation'] = self.translation.to_dict()
        # set to None if asset_type_name (nullable) is None
        # and model_fields_set contains the field
        if self.asset_type_name is None and "asset_type_name" in self.model_fields_set:
            _dict['assetTypeName'] = None

        # set to None if type (nullable) is None
        # and model_fields_set contains the field
        if self.type is None and "type" in self.model_fields_set:
            _dict['type'] = None

        # set to None if translation (nullable) is None
        # and model_fields_set contains the field
        if self.translation is None and "translation" in self.model_fields_set:
            _dict['translation'] = None

        # set to None if unit (nullable) is None
        # and model_fields_set contains the field
        if self.unit is None and "unit" in self.model_fields_set:
            _dict['unit'] = None

        # set to None if precision (nullable) is None
        # and model_fields_set contains the field
        if self.precision is None and "precision" in self.model_fields_set:
            _dict['precision'] = None

        # set to None if min (nullable) is None
        # and model_fields_set contains the field
        if self.min is None and "min" in self.model_fields_set:
            _dict['min'] = None

        # set to None if max (nullable) is None
        # and model_fields_set contains the field
        if self.max is None and "max" in self.model_fields_set:
            _dict['max'] = None

        # set to None if aggregation_mode (nullable) is None
        # and model_fields_set contains the field
        if self.aggregation_mode is None and "aggregation_mode" in self.model_fields_set:
            _dict['aggregationMode'] = None

        # set to None if viewer (nullable) is None
        # and model_fields_set contains the field
        if self.viewer is None and "viewer" in self.model_fields_set:
            _dict['viewer'] = None

        # set to None if ar (nullable) is None
        # and model_fields_set contains the field
        if self.ar is None and "ar" in self.model_fields_set:
            _dict['ar'] = None

        # set to None if sequence (nullable) is None
        # and model_fields_set contains the field
        if self.sequence is None and "sequence" in self.model_fields_set:
            _dict['sequence'] = None

        # set to None if virtual (nullable) is None
        # and model_fields_set contains the field
        if self.virtual is None and "virtual" in self.model_fields_set:
            _dict['virtual'] = None

        # set to None if formula (nullable) is None
        # and model_fields_set contains the field
        if self.formula is None and "formula" in self.model_fields_set:
            _dict['formula'] = None

        # set to None if scale (nullable) is None
        # and model_fields_set contains the field
        if self.scale is None and "scale" in self.model_fields_set:
            _dict['scale'] = None

        # set to None if zero (nullable) is None
        # and model_fields_set contains the field
        if self.zero is None and "zero" in self.model_fields_set:
            _dict['zero'] = None

        # set to None if map (nullable) is None
        # and model_fields_set contains the field
        if self.map is None and "map" in self.model_fields_set:
            _dict['map'] = None

        # set to None if source_path (nullable) is None
        # and model_fields_set contains the field
        if self.source_path is None and "source_path" in self.model_fields_set:
            _dict['sourcePath'] = None

        # set to None if is_digital (nullable) is None
        # and model_fields_set contains the field
        if self.is_digital is None and "is_digital" in self.model_fields_set:
            _dict['isDigital'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AssetTypeAttribute from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetTypeName": obj.get("assetTypeName"),
            "name": obj.get("name"),
            "subtype": obj.get("subtype"),
            "type": obj.get("type"),
            "enable": obj.get("enable") if obj.get("enable") is not None else True,
            "translation": Translation.from_dict(obj["translation"]) if obj.get("translation") is not None else None,
            "unit": obj.get("unit"),
            "precision": obj.get("precision"),
            "min": obj.get("min"),
            "max": obj.get("max"),
            "aggregationMode": obj.get("aggregationMode"),
            "aggregationRasters": obj.get("aggregationRasters"),
            "viewer": obj.get("viewer") if obj.get("viewer") is not None else False,
            "ar": obj.get("ar") if obj.get("ar") is not None else False,
            "sequence": obj.get("sequence"),
            "virtual": obj.get("virtual"),
            "formula": obj.get("formula"),
            "scale": obj.get("scale"),
            "zero": obj.get("zero"),
            "map": obj.get("map"),
            "sourcePath": obj.get("sourcePath"),
            "isDigital": obj.get("isDigital")
        })
        return _obj


