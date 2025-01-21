# coding: utf-8

"""
    Eliona REST API

    The Eliona REST API enables unified access to the resources and data of an Eliona environment.

    The version of the OpenAPI document: 2.8.1
    Contact: hello@eliona.io
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from eliona.api_client2.models.attachment import Attachment
from typing import Optional, Set
from typing_extensions import Self

class Message(BaseModel):
    """
    A message
    """ # noqa: E501
    sender: Optional[StrictStr] = Field(default=None, description="Address of the sender, e.g. an e-mail address")
    recipients: Annotated[List[StrictStr], Field(min_length=1)] = Field(description="A list of recipient addresses to receive this message")
    copy_recipients: Optional[List[StrictStr]] = Field(default=None, description="A list of recipient addresses to receive this message as copy", alias="copyRecipients")
    blind_copy_recipients: Optional[List[StrictStr]] = Field(default=None, description="A list of recipient addresses to receive this message as blind copy without any other recipient information", alias="blindCopyRecipients")
    subject: Optional[StrictStr] = Field(default=None, description="The subject for this message")
    content: StrictStr = Field(description="The content of the message. If template is used, the content is embedded in the template.")
    attachments: Optional[List[Attachment]] = Field(default=None, description="A list of files attached to the message")
    __properties: ClassVar[List[str]] = ["sender", "recipients", "copyRecipients", "blindCopyRecipients", "subject", "content", "attachments"]

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
        """Create an instance of Message from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in attachments (list)
        _items = []
        if self.attachments:
            for _item in self.attachments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['attachments'] = _items
        # set to None if sender (nullable) is None
        # and model_fields_set contains the field
        if self.sender is None and "sender" in self.model_fields_set:
            _dict['sender'] = None

        # set to None if copy_recipients (nullable) is None
        # and model_fields_set contains the field
        if self.copy_recipients is None and "copy_recipients" in self.model_fields_set:
            _dict['copyRecipients'] = None

        # set to None if blind_copy_recipients (nullable) is None
        # and model_fields_set contains the field
        if self.blind_copy_recipients is None and "blind_copy_recipients" in self.model_fields_set:
            _dict['blindCopyRecipients'] = None

        # set to None if attachments (nullable) is None
        # and model_fields_set contains the field
        if self.attachments is None and "attachments" in self.model_fields_set:
            _dict['attachments'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Message from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sender": obj.get("sender"),
            "recipients": obj.get("recipients"),
            "copyRecipients": obj.get("copyRecipients"),
            "blindCopyRecipients": obj.get("blindCopyRecipients"),
            "subject": obj.get("subject"),
            "content": obj.get("content"),
            "attachments": [Attachment.from_dict(_item) for _item in obj["attachments"]] if obj.get("attachments") is not None else None
        })
        return _obj


