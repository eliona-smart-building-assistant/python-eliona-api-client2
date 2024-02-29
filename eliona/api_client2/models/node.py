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
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Node(BaseModel):
    """
    An edge node
    """ # noqa: E501
    id: Optional[StrictStr] = Field(default=None, description="Unique id for the edge node")
    ident: Optional[StrictStr] = Field(default=None, description="UUID to identify the edge node")
    password: Optional[StrictStr] = Field(default=None, description="Password with which the node identifies itself")
    asset_id: Optional[StrictInt] = Field(default=None, description="ID of the corresponding asset", alias="assetId")
    vendor: Optional[StrictStr] = Field(default=None, description="Vendor name")
    model: Optional[StrictStr] = Field(default=None, description="Model name")
    description: Optional[StrictStr] = Field(default=None, description="Descriptive text for the edge node")
    enable: Optional[StrictBool] = Field(default=False, description="Is the node enabled or not")
    __properties: ClassVar[List[str]] = ["id", "ident", "password", "assetId", "vendor", "model", "description", "enable"]

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
        """Create an instance of Node from a JSON string"""
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
                "ident",
            },
            exclude_none=True,
        )
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if ident (nullable) is None
        # and model_fields_set contains the field
        if self.ident is None and "ident" in self.model_fields_set:
            _dict['ident'] = None

        # set to None if password (nullable) is None
        # and model_fields_set contains the field
        if self.password is None and "password" in self.model_fields_set:
            _dict['password'] = None

        # set to None if asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.asset_id is None and "asset_id" in self.model_fields_set:
            _dict['assetId'] = None

        # set to None if vendor (nullable) is None
        # and model_fields_set contains the field
        if self.vendor is None and "vendor" in self.model_fields_set:
            _dict['vendor'] = None

        # set to None if model (nullable) is None
        # and model_fields_set contains the field
        if self.model is None and "model" in self.model_fields_set:
            _dict['model'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Node from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "ident": obj.get("ident"),
            "password": obj.get("password"),
            "assetId": obj.get("assetId"),
            "vendor": obj.get("vendor"),
            "model": obj.get("model"),
            "description": obj.get("description"),
            "enable": obj.get("enable") if obj.get("enable") is not None else False
        })
        return _obj


