from form_template_obtainer.domain import usecases
from form_template_obtainer.implementation import FormFieldTypeSpecifierImpl, MongoDBFormTemplateRepository

from .configuration_obtainer import EnvConfigurationObtainer


class UsecasesBuilder:
    def __init__(self, config_obtainer: EnvConfigurationObtainer) -> None:
        self._config_obtainer = config_obtainer
        self._form_template_repo = MongoDBFormTemplateRepository(
            self._config_obtainer.get_repo_host(),
            self._config_obtainer.get_repo_port(),
            self._config_obtainer.get_repo_user(),
            self._config_obtainer.get_repo_password(),
            self._config_obtainer.get_repo_database(),
            self._config_obtainer.get_repo_collection(),
        )
        self._form_field_specifier = FormFieldTypeSpecifierImpl()

    def build_get_form_template_name(self) -> usecases.GetFormTemplateNameUsecase:
        return usecases.GetFormTemplateNameUsecase(self._form_template_repo)

    def build_specify_form_fields(self) -> usecases.SpecifyFormFieldsUsecase:
        return usecases.SpecifyFormFieldsUsecase(self._form_field_specifier)
