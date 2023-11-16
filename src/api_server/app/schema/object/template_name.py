from pydantic import BaseModel, Field
from typing import Self


class TemplateName(BaseModel):
    name: str = Field(
        description="Template form name",
        examples=["Order Form"]
    )

    @classmethod
    def from_str(cls, template_name: str) -> Self:
        return cls(name=template_name)
