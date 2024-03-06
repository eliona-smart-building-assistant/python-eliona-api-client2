# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.6.7
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from eliona.api_client2.models.attachment import Attachment
from typing import Optional, Set
from typing_extensions import Self

class Asset(BaseModel):
    """
    An asset
    """ # noqa: E501
    resource_id: Optional[StrictStr] = Field(default=None, description="A custom identifier for the resource, which can be utilized to identify it for various operations such as updates, deletions, and other related tasks. If this identifier is not provided, the application will generate a new value for it automatically", alias="resourceId")
    id: Optional[StrictInt] = Field(default=None, description="The internal Id of asset")
    device_ids: Optional[List[StrictStr]] = Field(default=None, description="A list of unique device ids", alias="deviceIds")
    project_id: StrictStr = Field(description="ID of the project to which the asset belongs", alias="projectId")
    global_asset_identifier: StrictStr = Field(description="Unique identifier for the asset", alias="globalAssetIdentifier")
    name: Optional[StrictStr] = Field(default=None, description="Alternate text for the asset to display in frontend")
    asset_type: StrictStr = Field(description="Reference to asset type by name", alias="assetType")
    latitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latitude coordinate (GPS) of the asset")
    longitude: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Longitude coordinate (GPS) of the asset")
    is_tracker: Optional[StrictBool] = Field(default=False, description="Does the asset function as a tracker and capture its position by itself", alias="isTracker")
    description: Optional[StrictStr] = Field(default=None, description="Textual description for this asset")
    parent_functional_asset_id: Optional[StrictInt] = Field(default=None, description="The id of an asset which groups this asset as a functional child", alias="parentFunctionalAssetId")
    functional_asset_id_path: Optional[List[StrictInt]] = Field(default=None, description="The hierarchical path of functional ids of the asset", alias="functionalAssetIdPath")
    parent_locational_asset_id: Optional[StrictInt] = Field(default=None, description="The id of an asset which groups this asset as a locational child", alias="parentLocationalAssetId")
    locational_asset_id_path: Optional[List[StrictInt]] = Field(default=None, description="The hierarchical path of locational ids of the asset", alias="locationalAssetIdPath")
    tags: Optional[List[StrictStr]] = Field(default=None, description="List of associated tags")
    children_info: Optional[List[Optional[Asset]]] = Field(default=None, description="List of children for this asset.", alias="childrenInfo")
    attachments: Optional[List[Attachment]] = Field(default=None, description="A list of files attached to the asset")
    __properties: ClassVar[List[str]] = ["resourceId", "id", "deviceIds", "projectId", "globalAssetIdentifier", "name", "assetType", "latitude", "longitude", "isTracker", "description", "parentFunctionalAssetId", "functionalAssetIdPath", "parentLocationalAssetId", "locationalAssetIdPath", "tags", "childrenInfo", "attachments"]

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
        """Create an instance of Asset from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "id",
            "functional_asset_id_path",
            "locational_asset_id_path",
            "children_info",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in children_info (list)
        _items = []
        if self.children_info:
            for _item in self.children_info:
                if _item:
                    _items.append(_item.to_dict())
            _dict['childrenInfo'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # set to None if resource_id (nullable) is None
        # and model_fields_set contains the field
        if self.resource_id is None and "resource_id" in self.model_fields_set:
            _dict['resourceId'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if device_ids (nullable) is None
        # and model_fields_set contains the field
        if self.device_ids is None and "device_ids" in self.model_fields_set:
            _dict['deviceIds'] = None

        # set to None if name (nullable) is None
        # and model_fields_set contains the field
        if self.name is None and "name" in self.model_fields_set:
            _dict['name'] = None

        # set to None if latitude (nullable) is None
        # and model_fields_set contains the field
        if self.latitude is None and "latitude" in self.model_fields_set:
            _dict['latitude'] = None

        # set to None if longitude (nullable) is None
        # and model_fields_set contains the field
        if self.longitude is None and "longitude" in self.model_fields_set:
            _dict['longitude'] = None

        # set to None if is_tracker (nullable) is None
        # and model_fields_set contains the field
        if self.is_tracker is None and "is_tracker" in self.model_fields_set:
            _dict['isTracker'] = None

        # set to None if description (nullable) is None
        # and model_fields_set contains the field
        if self.description is None and "description" in self.model_fields_set:
            _dict['description'] = None

        # set to None if parent_functional_asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_functional_asset_id is None and "parent_functional_asset_id" in self.model_fields_set:
            _dict['parentFunctionalAssetId'] = None

        # set to None if functional_asset_id_path (nullable) is None
        # and model_fields_set contains the field
        if self.functional_asset_id_path is None and "functional_asset_id_path" in self.model_fields_set:
            _dict['functionalAssetIdPath'] = None

        # set to None if parent_locational_asset_id (nullable) is None
        # and model_fields_set contains the field
        if self.parent_locational_asset_id is None and "parent_locational_asset_id" in self.model_fields_set:
            _dict['parentLocationalAssetId'] = None

        # set to None if locational_asset_id_path (nullable) is None
        # and model_fields_set contains the field
        if self.locational_asset_id_path is None and "locational_asset_id_path" in self.model_fields_set:
            _dict['locationalAssetIdPath'] = None

        # set to None if tags (nullable) is None
        # and model_fields_set contains the field
        if self.tags is None and "tags" in self.model_fields_set:
            _dict['tags'] = None

        # set to None if children_info (nullable) is None
        # and model_fields_set contains the field
        if self.children_info is None and "children_info" in self.model_fields_set:
            _dict['childrenInfo'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Asset from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "resourceId": obj.get("resourceId"),
            "id": obj.get("id"),
            "deviceIds": obj.get("deviceIds"),
            "projectId": obj.get("projectId"),
            "globalAssetIdentifier": obj.get("globalAssetIdentifier"),
            "name": obj.get("name"),
            "assetType": obj.get("assetType"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude"),
            "isTracker": obj.get("isTracker") if obj.get("isTracker") is not None else False,
            "description": obj.get("description"),
            "parentFunctionalAssetId": obj.get("parentFunctionalAssetId"),
            "functionalAssetIdPath": obj.get("functionalAssetIdPath"),
            "parentLocationalAssetId": obj.get("parentLocationalAssetId"),
            "locationalAssetIdPath": obj.get("locationalAssetIdPath"),
            "tags": obj.get("tags"),
            "childrenInfo": [Asset.from_dict(_item) for _item in obj["childrenInfo"]] if obj.get("childrenInfo") is not None else None,
            "attachments": [Attachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj

# TODO: Rewrite to not use raise_errors
Asset.model_rebuild(raise_errors=False)

