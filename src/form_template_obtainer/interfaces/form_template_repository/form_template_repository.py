import abc

from form_template_obtainer.domain import entities


class FormTemplateRepository(abc.ABC):
    @abc.abstractmethod
    async def get_form_template_name(self, fields: list[entities.FormField]) -> str | None:
        pass
