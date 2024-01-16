# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.5.9
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
import re  # noqa: F401
from enum import Enum



try:
    from typing import Self
except ImportError:
    from typing_extensions import Self


class AgentClass(str, Enum):
    """
    The class of an agent
    """

    """
    allowed enum values
    """
    IOSYS = 'iosys'
    MBUS = 'mbus'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of AgentClass from a JSON string"""
        return cls(json.loads(json_str))


