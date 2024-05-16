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

from pydantic import BaseModel, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from eliona.api_client2.models.agent_class import AgentClass
from typing import Optional, Set
from typing_extensions import Self

class Agent(BaseModel):
    """
    An agent installed on an edge node
    """ # noqa: E501
    id: Optional[StrictInt] = Field(default=None, description="Unique id for the agent")
    node_id: Optional[StrictStr] = Field(default=None, description="Id of the node where the agent is installed", alias="nodeId")
    asset_id: Optional[StrictInt] = Field(default=None, description="ID of the corresponding asset", alias="assetId")
    var_class: Optional[AgentClass] = Field(default=None, alias="class")
    description: Optional[StrictStr] = Field(default=None, description="Descriptive text for the agent")
    enable: Optional[StrictBool] = Field(default=False, description="Is the agent enabled or not")
    config: Optional[Dict[str, Any]] = Field(default=None, description="Individual configuration depending on agent class")
    __properties: ClassVar[List[str]] = ["id", "nodeId", "assetId", "class", "description", "enable", "config"]

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
        """Create an instance of Agent from a JSON string"""
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

        # set to None if node_id (nullable) is None
        # and model_fields_set contains the field
        if self.node_id is None and "node_id" in self.model_fields_set:
            _dict['nodeId'] = None

        # set to None if asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.asset_id is None and "asset_id" in self.model_fields_set:
            _dict['assetId'] = None

        # set to None if var_class (nullable) is None
        # and model_fields_set contains the field
        if self.var_class is None and "var_class" in self.model_fields_set:
            _dict['class'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if config (nullable) is None
        # and model_fields_set contains the field
        if self.config is None and "config" in self.model_fields_set:
            _dict['config'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Agent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "nodeId": obj.get("nodeId"),
            "assetId": obj.get("assetId"),
            "class": obj.get("class"),
            "description": obj.get("description"),
            "enable": obj.get("enable") if obj.get("enable") is not None else False,
            "config": obj.get("config")
        })
        return _obj


