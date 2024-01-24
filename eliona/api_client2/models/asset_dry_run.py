# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.0
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
from eliona.api_client2.models.asset import Asset
from eliona.api_client2.models.asset_identify_by import AssetIdentifyBy
try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

class AssetDryRun(BaseModel):
    """
    AssetDryRun
    """ # noqa: E501
    identifier: Optional[StrictStr] = Field(default=None, description="Unique identifier (textual or numeric) of resources")
    status_code: Optional[StrictInt] = Field(default=None, description="The status code expecting when actually perform the operation. Some values are - 200: updated (ok)  - 201: created - 204: deleted (no content) - 304: unchanged (not modified) - 400: problem (bad request) - 404: not found - 409: duplicated (conflict) - 422: unprocessable ", alias="statusCode")
    error_message: Optional[StrictStr] = Field(default=None, description="The error message expecting when actually perform the operation. ", alias="errorMessage")
    identified_by: Optional[AssetIdentifyBy] = Field(default=None, alias="identifiedBy")
    before: Optional[Asset] = None
    after: Optional[Asset] = None
    __properties: ClassVar[List[str]] = ["identifier", "statusCode", "errorMessage", "identifiedBy", "before", "after"]

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
        """Create an instance of AssetDryRun from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of before
        if self.before:
            _dict['before'] = self.before.to_dict()
        # override the default output from pydantic by calling `to_dict()` of after
        if self.after:
            _dict['after'] = self.after.to_dict()
        # set to None if error_message (nullable) is None
        # and model_fields_set contains the field
        if self.error_message is None and "error_message" in self.model_fields_set:
            _dict['errorMessage'] = None

        # set to None if before (nullable) is None
        # and model_fields_set contains the field
        if self.before is None and "before" in self.model_fields_set:
            _dict['before'] = None

        # set to None if after (nullable) is None
        # and model_fields_set contains the field
        if self.after is None and "after" in self.model_fields_set:
            _dict['after'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Dict) -> Self:
        """Create an instance of AssetDryRun from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "identifier": obj.get("identifier"),
            "statusCode": obj.get("statusCode"),
            "errorMessage": obj.get("errorMessage"),
            "identifiedBy": obj.get("identifiedBy"),
            "before": Asset.from_dict(obj.get("before")) if obj.get("before") is not None else None,
            "after": Asset.from_dict(obj.get("after")) if obj.get("after") is not None else None
        })
        return _obj


