import abc

from form_template_obtainer.domain import entities


class FormFieldTypeSpecifier(abc.ABC):
    @abc.abstractmethod
    def get_specified_form_fields(self, data: dict[str, str]) -> list[entities.FormField]:
        pass
