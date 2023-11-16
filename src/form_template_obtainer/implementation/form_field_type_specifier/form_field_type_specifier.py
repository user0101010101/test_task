import re
from form_template_obtainer.domain import entities
from form_template_obtainer.interfaces import FormFieldTypeSpecifier


class FormFieldTypeSpecifierImpl(FormFieldTypeSpecifier):
    _DATE_PATTERNS: list[str] = [r"^\d{2}\.\d{2}.\d{4}$", r"^\d{4}-\d{2}-\d{2}$"]
    _DATA_REGEX = re.compile("|".join(_DATE_PATTERNS))
    _PHONE_REGEX = re.compile(r"^\+7 \d{3} \d{3} \d{2} \d{2}$")
    _EMAIL_REGEX = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4}$")

    def get_specified_form_fields(self, data: dict[str, str]) -> list[entities.FormField]:
        form_fields: list[entities.FormField] = list()
        for key, value in data.items():
            if self._DATA_REGEX.match(value) is not None:
                form_fields.append(
                    entities.FormField.new(
                        name=key,
                        type_=entities.FieldType.Date
                    )
                )
            elif self._PHONE_REGEX.match(value) is not None:
                form_fields.append(
                    entities.FormField.new(
                        name=key,
                        type_=entities.FieldType.Phone
                    )
                )
            elif self._EMAIL_REGEX.match(value) is not None:
                form_fields.append(
                    entities.FormField.new(
                        name=key,
                        type_=entities.FieldType.Email
                    )
                )
            else:
                form_fields.append(
                    entities.FormField.new(
                        name=key,
                        type_=entities.FieldType.Text
                    )
                )
        return form_fields
