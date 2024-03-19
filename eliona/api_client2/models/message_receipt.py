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

from datetime import datetime
from pydantic import BaseModel, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class MessageReceipt(BaseModel):
    """
    A receipt for a message or notification
    """ # noqa: E501
    id: StrictStr = Field(description="Identifies the message or notification")
    scheduled_at: Optional[datetime] = Field(default=None, description="When the message or notification is scheduled", alias="scheduledAt")
    status: Optional[StrictStr] = Field(default=None, description="Status of communication processing")
    __properties: ClassVar[List[str]] = ["id", "scheduledAt", "status"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['scheduled', 'sent', 'seen', 'read', 'deleted', 'failed']):
            raise ValueError("must be one of enum values ('scheduled', 'sent', 'seen', 'read', 'deleted', 'failed')")
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
        """Create an instance of MessageReceipt from a JSON string"""
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
        # set to None if scheduled_at (nullable) is None
        # and model_fields_set contains the field
        if self.scheduled_at is None and "scheduled_at" in self.model_fields_set:
            _dict['scheduledAt'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MessageReceipt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "scheduledAt": obj.get("scheduledAt"),
            "status": obj.get("status")
        })
        return _obj


