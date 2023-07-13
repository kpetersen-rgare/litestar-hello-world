"""Minimal Starlite application."""
from typing import Any

import logging
import structlog
from starlite import Starlite, get, StructLoggingConfig

main_logger = structlog.getLogger("main")


@get("/")
def hello_world() -> dict[str, Any]:
    """Route Handler that outputs hello world."""
    main_logger.info("hello world endpoint called INFO")
    main_logger.debug("hello world endpoint called DEBUG")
    return {"hello": "world"}


logging_config = StructLoggingConfig(
    wrapper_class=structlog.make_filtering_bound_logger(logging.DEBUG)
)


app = Starlite(route_handlers=[hello_world], logging_config=logging_config)
