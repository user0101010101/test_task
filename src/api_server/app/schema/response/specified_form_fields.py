from typing import Self
from pydantic import Field
from form_template_obtainer.domain import entities
from .base import ResponseBody


class SpecifiedFormFieldsResponse(ResponseBody):
    result: dict[str, str] = Field(
        description="Contains field name and type.",
        examples=["{'field': 'text'}", "{'field2': 'phone'}", "{'field3': 'email'}", "{'field4': 'date'}"]
    )

    @classmethod
    def create(cls, fields: list[entities.FormField]) -> Self:
        fields = {field.name: field.type_.value for field in fields}
        return cls(result=fields)
