from typing import Self
from enum import StrEnum
from pydantic import BaseModel, StrictStr


class FieldType(StrEnum):
    Email = "email"
    Phone = "phone"
    Date = "date"
    Text = "text"


class FormField(BaseModel):
    name: StrictStr
    type_: FieldType

    @classmethod
    def new(cls, name: str, type_: FieldType) -> Self:
        return cls(name=name, type_=type_)
