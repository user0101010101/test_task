from fastapi import APIRouter, status, Request
from .. import dependency, schema, error_handling

form_router = APIRouter(prefix="/api/v1", tags=["Form"], responses=error_handling.ERROR_RESPONSES)


@form_router.post(
    "/get_form",
    responses={
        status.HTTP_200_OK: {
            "model": schema.response.template_name.TemplateNameResponse
            | schema.response.specified_form_fields.SpecifiedFormFieldsResponse
        }
    },
)
async def get_form(
    request: Request
):
    form_fields = dependency.specify_from_fields_usecase.execute(dict(request.query_params))

    if template_name := await dependency.get_form_template_name_usecase.execute(form_fields):
        return schema.response.TemplateNameResponse.create(template_name)
    return schema.response.SpecifiedFormFieldsResponse.create(form_fields)
