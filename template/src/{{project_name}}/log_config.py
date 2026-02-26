import json
import logging
import os
import sys

import structlog


def configure_logging():
    log_format = os.getenv("LOG_FORMAT", "").lower()

    if log_format == "json":
        use_json = True
    elif log_format == "console":
        use_json = False
    else:
        use_json = not sys.stderr.isatty()

    renderer = (
        structlog.processors.JSONRenderer(
            serializer=lambda obj, **kwargs: json.dumps(obj, ensure_ascii=False)
        )
        if use_json
        else structlog.dev.ConsoleRenderer()
    )

    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.processors.TimeStamper(fmt="iso"),
            renderer,
        ],
        wrapper_class=structlog.make_filtering_bound_logger(logging.INFO),
        cache_logger_on_first_use=True,
    )
