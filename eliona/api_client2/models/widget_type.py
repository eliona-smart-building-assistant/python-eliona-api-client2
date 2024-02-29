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


from typing import Any, ClassVar, Dict, List, Optional
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from pydantic import Field
from eliona.api_client2.models.translation import Translation
from eliona.api_client2.models.widget_type_element import WidgetTypeElement
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class WidgetType(BaseModel):
    """
    A frontend widget
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The internal Id of widget type")
    name: StrictStr = Field(description="The unique name for this widget type")
    custom: Optional[StrictBool] = Field(default=True, description="Is this a customer created type or not")
    translation: Optional[Translation]
    icon: Optional[StrictStr] = Field(default=None, description="Icon name corresponding to assets used in this widget")
    with_alarm: Optional[StrictBool] = Field(default=False, description="Show alarms in widget", alias="withAlarm")
    with_timespan: Optional[StrictBool] = Field(default=False, description="Show selection for timespan in widget", alias="withTimespan")
    elements: List[WidgetTypeElement] = Field(description="A list of elements for this widget (order matches the order of elements for this type)")
    __properties: ClassVar[List[str]] = ["id", "name", "custom", "translation", "icon", "withAlarm", "withTimespan", "elements"]

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
        """Create an instance of WidgetType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of translation
        if self.translation:
            _dict['translation'] = self.translation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in elements (list)
        _items = []
        if self.elements:
            for _item in self.elements:
                if _item:
                    _items.append(_item.to_dict())
            _dict['elements'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if translation (nullable) is None
        # and model_fields_set contains the field
        if self.translation is None and "translation" in self.model_fields_set:
            _dict['translation'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if with_alarm (nullable) is None
        # and model_fields_set contains the field
        if self.with_alarm is None and "with_alarm" in self.model_fields_set:
            _dict['withAlarm'] = None

        # set to None if with_timespan (nullable) is None
        # and model_fields_set contains the field
        if self.with_timespan is None and "with_timespan" in self.model_fields_set:
            _dict['withTimespan'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of WidgetType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "custom": obj.get("custom") if obj.get("custom") is not None else True,
            "translation": Translation.from_dict(obj.get("translation")) if obj.get("translation") is not None else None,
            "icon": obj.get("icon"),
            "withAlarm": obj.get("withAlarm") if obj.get("withAlarm") is not None else False,
            "withTimespan": obj.get("withTimespan") if obj.get("withTimespan") is not None else False,
            "elements": [WidgetTypeElement.from_dict(_item) for _item in obj.get("elements")] if obj.get("elements") is not None else None
        })
        return _obj


