from form_template_obtainer.domain import entities
from form_template_obtainer.interfaces import FormFieldTypeSpecifier


class SpecifyFormFieldsUsecase:
    def __init__(self, form_field_type_specifier: FormFieldTypeSpecifier):
        self._form_field_type_specifier = form_field_type_specifier

    def execute(self, data: dict[str, str]) -> list[entities.FormField]:
        return self._form_field_type_specifier.get_specified_form_fields(data)
