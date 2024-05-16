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

from datetime import datetime
from pydantic import BaseModel, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from eliona.api_client2.models.data_subtype import DataSubtype
from typing import Optional, Set
from typing_extensions import Self

class Data(BaseModel):
    """
    Data for assets
    """ # noqa: E501
    asset_id: StrictInt = Field(description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    timestamp: Optional[datetime] = Field(default=None, description="Timestamp of the latest data change")
    data: Dict[str, Any] = Field(description="Asset payload")
    asset_type_name: Optional[StrictStr] = Field(default=None, description="The name of the corresponding asset type", alias="assetTypeName")
    client_reference: Optional[StrictStr] = Field(default=None, description="freely assignable by the client to identify self-created data", alias="clientReference")
    __properties: ClassVar[List[str]] = ["assetId", "subtype", "timestamp", "data", "assetTypeName", "clientReference"]

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
        """Create an instance of Data from a JSON string"""
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
            "asset_type_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.timestamp is None and "timestamp" in self.model_fields_set:
            _dict['timestamp'] = None

        # set to None if asset_type_name (nullable) is None
        # and model_fields_set contains the field
        if self.asset_type_name is None and "asset_type_name" in self.model_fields_set:
            _dict['assetTypeName'] = None

        # set to None if client_reference (nullable) is None
        # and model_fields_set contains the field
        if self.client_reference is None and "client_reference" in self.model_fields_set:
            _dict['clientReference'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Data from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype"),
            "timestamp": obj.get("timestamp"),
            "data": obj.get("data"),
            "assetTypeName": obj.get("assetTypeName"),
            "clientReference": obj.get("clientReference")
        })
        return _obj


