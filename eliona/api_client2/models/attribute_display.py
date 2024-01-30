# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.1
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
from typing_extensions import Annotated
from eliona.api_client2.models.data_subtype import DataSubtype
from eliona.api_client2.models.value_mapping import ValueMapping
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AttributeDisplay(BaseModel):
    """
    How attributes are displayed for specific assets
    """ # noqa: E501
    asset_id: StrictInt = Field(description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: StrictStr = Field(description="Name of the attribute of the asset type")
    unit: Optional[StrictStr] = Field(default=None, description="Physical unit of numeric data")
    precision: Optional[Annotated[int, Field(le=20, strict=True, ge=-20)]] = Field(default=None, description="Number of decimal places")
    min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Lower limit")
    max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Upper limit")
    viewer: Optional[StrictBool] = Field(default=False, description="Should the attribute be displayed in viewer")
    ar: Optional[StrictBool] = Field(default=False, description="Should the attribute be displayed in AR")
    sequence: Optional[StrictInt] = Field(default=None, description="Sequence in AR display")
    map: Optional[List[ValueMapping]] = Field(default=None, description="list of mapping between value and custom text")
    __properties: ClassVar[List[str]] = ["assetId", "subtype", "attribute", "unit", "precision", "min", "max", "viewer", "ar", "sequence", "map"]

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
        """Create an instance of AttributeDisplay from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in map (list)
        _items = []
        if self.map:
            for _item in self.map:
                if _item:
                    _items.append(_item.to_dict())
            _dict['map'] = _items
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

        # set to None if map (nullable) is None
        # and model_fields_set contains the field
        if self.map is None and "map" in self.model_fields_set:
            _dict['map'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AttributeDisplay from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype"),
            "attribute": obj.get("attribute"),
            "unit": obj.get("unit"),
            "precision": obj.get("precision"),
            "min": obj.get("min"),
            "max": obj.get("max"),
            "viewer": obj.get("viewer") if obj.get("viewer") is not None else False,
            "ar": obj.get("ar") if obj.get("ar") is not None else False,
            "sequence": obj.get("sequence"),
            "map": [ValueMapping.from_dict(_item) for _item in obj.get("map")] if obj.get("map") is not None else None
        })
        return _obj


