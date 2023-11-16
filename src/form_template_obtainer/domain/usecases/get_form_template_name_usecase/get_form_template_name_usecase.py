from form_template_obtainer.domain import entities
from form_template_obtainer.interfaces import FormTemplateRepository


class GetFormTemplateNameUsecase:
    def __init__(self, form_repo: FormTemplateRepository):
        self._form_repo = form_repo

    async def execute(self, fields: list[entities.FormField]) -> str | None:
        return await self._form_repo.get_form_template_name(fields)
