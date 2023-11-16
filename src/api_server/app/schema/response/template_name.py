from typing import Self

from .base import ResponseBody
from ..object import TemplateName


class TemplateNameResponse(ResponseBody):
    result: TemplateName

    @classmethod
    def create(cls, template_name: str) -> Self:
        return cls(result=TemplateName.from_str(template_name))
