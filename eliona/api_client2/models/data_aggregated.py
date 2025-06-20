# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.9.4
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from eliona.api_client2.models.data_subtype import DataSubtype
from typing import Optional, Set
from typing_extensions import Self

class DataAggregated(BaseModel):
    """
    Aggregated data combines multiple data points for a periodical raster
    """ # noqa: E501
    aggregation_id: Optional[StrictInt] = Field(default=None, description="ID of the aggregation", alias="aggregationId")
    asset_id: StrictInt = Field(description="ID of the corresponding asset", alias="assetId")
    subtype: DataSubtype
    attribute: Optional[StrictStr] = Field(default=None, description="Name of the attribute which holds the data points")
    raster: StrictStr = Field(description="Calculation intervals.")
    timestamp: Optional[datetime] = Field(default=None, description="Timestamp of this aggregated data set. The timestamp when the timeslot based on raster starts.")
    count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Count of data points in this aggregated data set")
    average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Average of all data points for this aggregated data set")
    sum: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Sum of all data points for this aggregated data set")
    first: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="First data point in this aggregated data set")
    min: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Data point with the most minimal value in this aggregated data set")
    max: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Data point with the most maximal value in this aggregated data set")
    last: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Latest data point in this aggregated data set")
    last_timestamp: Optional[datetime] = Field(default=None, description="Timestamp of the latest data point", alias="lastTimestamp")
    asset_type_name: Optional[StrictStr] = Field(default=None, description="The name of the corresponding asset type", alias="assetTypeName")
    __properties: ClassVar[List[str]] = ["aggregationId", "assetId", "subtype", "attribute", "raster", "timestamp", "count", "average", "sum", "first", "min", "max", "last", "lastTimestamp", "assetTypeName"]

    @field_validator('raster')
    def raster_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10', 'S12', 'S15', 'S20', 'S30', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M10', 'M12', 'M15', 'M20', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12', 'DAY', 'WEEK', 'MONTH', 'QUARTER', 'YEAR', 'DECADE', 'CENTURY']):
            raise ValueError("must be one of enum values ('S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S10', 'S12', 'S15', 'S20', 'S30', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'M10', 'M12', 'M15', 'M20', 'M30', 'H1', 'H2', 'H3', 'H4', 'H6', 'H8', 'H12', 'DAY', 'WEEK', 'MONTH', 'QUARTER', 'YEAR', 'DECADE', 'CENTURY')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of DataAggregated from a JSON string"""
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

        # set to None if count (nullable) is None
        # and model_fields_set contains the field
        if self.count is None and "count" in self.model_fields_set:
            _dict['count'] = None

        # set to None if average (nullable) is None
        # and model_fields_set contains the field
        if self.average is None and "average" in self.model_fields_set:
            _dict['average'] = None

        # set to None if sum (nullable) is None
        # and model_fields_set contains the field
        if self.sum is None and "sum" in self.model_fields_set:
            _dict['sum'] = None

        # set to None if first (nullable) is None
        # and model_fields_set contains the field
        if self.first is None and "first" in self.model_fields_set:
            _dict['first'] = None

        # set to None if min (nullable) is None
        # and model_fields_set contains the field
        if self.min is None and "min" in self.model_fields_set:
            _dict['min'] = None

        # set to None if max (nullable) is None
        # and model_fields_set contains the field
        if self.max is None and "max" in self.model_fields_set:
            _dict['max'] = None

        # set to None if last (nullable) is None
        # and model_fields_set contains the field
        if self.last is None and "last" in self.model_fields_set:
            _dict['last'] = None

        # set to None if last_timestamp (nullable) is None
        # and model_fields_set contains the field
        if self.last_timestamp is None and "last_timestamp" in self.model_fields_set:
            _dict['lastTimestamp'] = None

        # set to None if asset_type_name (nullable) is None
        # and model_fields_set contains the field
        if self.asset_type_name is None and "asset_type_name" in self.model_fields_set:
            _dict['assetTypeName'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DataAggregated from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "aggregationId": obj.get("aggregationId"),
            "assetId": obj.get("assetId"),
            "subtype": obj.get("subtype") if obj.get("subtype") is not None else DataSubtype.NUMBER_SUBTYPE_INPUT,
            "attribute": obj.get("attribute"),
            "raster": obj.get("raster"),
            "timestamp": obj.get("timestamp"),
            "count": obj.get("count"),
            "average": obj.get("average"),
            "sum": obj.get("sum"),
            "first": obj.get("first"),
            "min": obj.get("min"),
            "max": obj.get("max"),
            "last": obj.get("last"),
            "lastTimestamp": obj.get("lastTimestamp"),
            "assetTypeName": obj.get("assetTypeName")
        })
        return _obj


