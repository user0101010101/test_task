from fastapi import FastAPI
from form_template_obtainer.domain import usecases
from .routes import form_router
from . import dependency, error_handling


def create_app(
        get_form_template_name_usecase: usecases.get_form_template_name_usecase,
        specify_from_fields_usecase: usecases.SpecifyFormFieldsUsecase
) -> FastAPI:
    dependency.get_form_template_name_usecase = get_form_template_name_usecase
    dependency.specify_from_fields_usecase = specify_from_fields_usecase
    app = FastAPI()
    app.include_router(form_router)

    for exception, handler in error_handling.EXCEPTION_HANDLERS.items():
        app.add_exception_handler(exception, handler)

    return app
