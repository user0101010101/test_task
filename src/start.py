import os
import logging
import api_server

from utils import EnvConfigurationObtainer, UsecasesBuilder


def main() -> int:
    try:
        config_obtainer = EnvConfigurationObtainer()
    except Exception:
        msg_crit = "Error during configuration obtainment."
        logging.critical(msg_crit, exc_info=True)
        return 1

    try:
        usecases_builder = UsecasesBuilder(config_obtainer)
        web_app = api_server.create_app(
            usecases_builder.build_get_form_template_name(),
            usecases_builder.build_specify_form_fields()
        )
    except Exception:
        msg_crit = "Error during service's initialization."
        logging.critical(msg_crit, exc_info=True)
        return 1

    try:
        api_server.start_api_server(
            web_app,
            host="0.0.0.0",
            port=10000,
        )
    except Exception:
        msg_crit = "Critical error during service's work."
        logging.critical(msg_crit, exc_info=True)
        return 1

    return 0


if __name__ == "__main__":
    exit_code = main()

    os._exit(exit_code)
