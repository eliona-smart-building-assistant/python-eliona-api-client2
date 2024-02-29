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
from pydantic import BaseModel, StrictInt, StrictStr
from pydantic import Field
from eliona.api_client2.models.widget import Widget
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class Dashboard(BaseModel):
    """
    A frontend dashboard
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="The internal Id of dashboard")
    name: StrictStr = Field(description="The name for this dashboard")
    project_id: StrictStr = Field(description="ID of the project to which the dashboard belongs", alias="projectId")
    user_id: StrictStr = Field(description="ID of the user who owns the dashboard", alias="userId")
    sequence: Optional[StrictInt] = Field(default=0, description="The sequence of the dashboard")
    widgets: Optional[List[Widget]] = Field(default=None, description="List of widgets on this dashboard (order matches the order of widgets on the dashboard)")
    __properties: ClassVar[List[str]] = ["id", "name", "projectId", "userId", "sequence", "widgets"]

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
        """Create an instance of Dashboard from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in widgets (list)
        _items = []
        if self.widgets:
            for _item in self.widgets:
                if _item:
                    _items.append(_item.to_dict())
            _dict['widgets'] = _items
        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if sequence (nullable) is None
        # and model_fields_set contains the field
        if self.sequence is None and "sequence" in self.model_fields_set:
            _dict['sequence'] = None

        # set to None if widgets (nullable) is None
        # and model_fields_set contains the field
        if self.widgets is None and "widgets" in self.model_fields_set:
            _dict['widgets'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of Dashboard from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "projectId": obj.get("projectId"),
            "userId": obj.get("userId"),
            "sequence": obj.get("sequence") if obj.get("sequence") is not None else 0,
            "widgets": [Widget.from_dict(_item) for _item in obj.get("widgets")] if obj.get("widgets") is not None else None
        })
        return _obj


