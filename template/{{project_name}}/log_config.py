import json
import logging
import sys

import structlog


def configure_logging():
    renderer = (
        structlog.processors.JSONRenderer(
            serializer=lambda obj, **kwargs: json.dumps(obj, ensure_ascii=False)
        )
        if not sys.stderr.isatty()
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
