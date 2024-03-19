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
import json
from enum import Enum
from typing_extensions import Self


class AlarmPriority(int, Enum):
    """
    The priority of the alarm. The higher this value the higher the priority.
    """

    """
    allowed enum values
    """
    NUMBER_1 = 1
    NUMBER_2 = 2
    NUMBER_3 = 3
    NUMBER_10 = 10

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AlarmPriority from a JSON string"""
        return cls(json.loads(json_str))


