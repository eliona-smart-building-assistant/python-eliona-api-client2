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
from pydantic import BaseModel, StrictBool, StrictStr, field_validator
from pydantic import Field
from eliona.api_client2.models.asset_type_attribute import AssetTypeAttribute
from eliona.api_client2.models.translation import Translation
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AssetType(BaseModel):
    """
    A type of assets
    """ # noqa: E501
    name: StrictStr = Field(description="The unique name for this asset type")
    custom: Optional[StrictBool] = Field(default=True, description="Is this a customer created type or not")
    vendor: Optional[StrictStr] = Field(default=None, description="The vendor providing assets of this type")
    model: Optional[StrictStr] = Field(default=None, description="The specific model of assets of this type")
    translation: Optional[Translation] = None
    urldoc: Optional[StrictStr] = Field(default=None, description="The url describing assets of this type")
    icon: Optional[StrictStr] = Field(default=None, description="Icon name corresponding to assets of this type")
    payload_function: Optional[StrictStr] = Field(default=None, description="Asset types payload function", alias="payloadFunction")
    allowed_inactivity: Optional[StrictStr] = Field(default=None, alias="allowedInactivity")
    attributes: Optional[List[AssetTypeAttribute]] = Field(default=None, description="List of named attributes")
    __properties: ClassVar[List[str]] = ["name", "custom", "vendor", "model", "translation", "urldoc", "icon", "payloadFunction", "allowedInactivity", "attributes"]

    @field_validator('icon')
    def icon_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in ('blind', 'building', 'button', 'closable', 'elevator', 'environment', 'fallback', 'filling', 'gateway', 'light', 'mailbox', 'parking', 'people', 'power', 'rack', 'storey', 'trash', 'ventilation', 'vibration', 'water', 'weather'):
            raise ValueError("must be one of enum values ('blind', 'building', 'button', 'closable', 'elevator', 'environment', 'fallback', 'filling', 'gateway', 'light', 'mailbox', 'parking', 'people', 'power', 'rack', 'storey', 'trash', 'ventilation', 'vibration', 'water', 'weather')")
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
        """Create an instance of AssetType from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of translation
        if self.translation:
            _dict['translation'] = self.translation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in attributes (list)
        _items = []
        if self.attributes:
            for _item in self.attributes:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attributes'] = _items
        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if translation (nullable) is None
        # and model_fields_set contains the field
        if self.translation is None and "translation" in self.model_fields_set:
            _dict['translation'] = None

        # set to None if urldoc (nullable) is None
        # and model_fields_set contains the field
        if self.urldoc is None and "urldoc" in self.model_fields_set:
            _dict['urldoc'] = None

        # set to None if icon (nullable) is None
        # and model_fields_set contains the field
        if self.icon is None and "icon" in self.model_fields_set:
            _dict['icon'] = None

        # set to None if payload_function (nullable) is None
        # and model_fields_set contains the field
        if self.payload_function is None and "payload_function" in self.model_fields_set:
            _dict['payloadFunction'] = None

        # set to None if allowed_inactivity (nullable) is None
        # and model_fields_set contains the field
        if self.allowed_inactivity is None and "allowed_inactivity" in self.model_fields_set:
            _dict['allowedInactivity'] = None

        # set to None if attributes (nullable) is None
        # and model_fields_set contains the field
        if self.attributes is None and "attributes" in self.model_fields_set:
            _dict['attributes'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AssetType from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "custom": obj.get("custom") if obj.get("custom") is not None else True,
            "vendor": obj.get("vendor"),
            "model": obj.get("model"),
            "translation": Translation.from_dict(obj.get("translation")) if obj.get("translation") is not None else None,
            "urldoc": obj.get("urldoc"),
            "icon": obj.get("icon"),
            "payloadFunction": obj.get("payloadFunction"),
            "allowedInactivity": obj.get("allowedInactivity"),
            "attributes": [AssetTypeAttribute.from_dict(_item) for _item in obj.get("attributes")] if obj.get("attributes") is not None else None
        })
        return _obj


