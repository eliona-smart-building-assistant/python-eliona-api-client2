# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.7.2
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class AlarmPriority(int, Enum):
    """
    The priority of the alarm. The lower this value the higher the priority.
    """

    """
    allowed enum values
    """
    ALARM_PRIORITY_HEIGHT = 1
    ALARM_PRIORITY_MEDIUM = 2
    ALARM_PRIORITY_LOW = 3
    ALARM_PRIORITY_INFO = 10

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlarmPriority from a JSON string"""
        return cls(json.loads(json_str))


