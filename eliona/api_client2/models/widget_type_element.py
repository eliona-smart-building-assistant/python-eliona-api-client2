# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.6
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictInt, StrictStr, field_validator
from pydantic import Field
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WidgetTypeElement(BaseModel):
    """
    An element for widget types
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The internal Id of widget element")
    category: StrictStr = Field(description="The category for this element")
    sequence: Optional[StrictInt] = Field(default=None, description="sequence of element in widget; if not defined the index in array is taken")
    config: Optional[Dict[str, Any]] = Field(default=None, description="individual config parameters depending on category")
    __properties: ClassVar[List[str]] = ["id", "category", "sequence", "config"]

    @field_validator('category')
    def category_validate_enum(cls, value):
        """Validates the enum"""
        if value not in ('input', 'table', 'image', 'tickets', 'map', 'icon', 'range', 'donut', 'comfort', 'sankey', 'progress', 'tracking', 'heatmap', 'radar', 'value', 'calendar', 'trend', 'alarms', 'weather', 'storey'):
            raise ValueError("must be one of enum values ('input', 'table', 'image', 'tickets', 'map', 'icon', 'range', 'donut', 'comfort', 'sankey', 'progress', 'tracking', 'heatmap', 'radar', 'value', 'calendar', 'trend', 'alarms', 'weather', 'storey')")
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
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of WidgetTypeElement from a JSON string"""
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
        _dict = self.model_dump(
            by_alias=True,
            exclude={
                "id",
            },
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if sequence (nullable) is None
        # and model_fields_set contains the field
        if self.sequence is None and "sequence" in self.model_fields_set:
            _dict['sequence'] = None

        # set to None if config (nullable) is None
        # and model_fields_set contains the field
        if self.config is None and "config" in self.model_fields_set:
            _dict['config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WidgetTypeElement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "category": obj.get("category"),
            "sequence": obj.get("sequence"),
            "config": obj.get("config")
        })
        return _obj


