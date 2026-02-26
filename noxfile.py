# Usage:
# > nox [-- --pdb | -m "mark"]

import os
import shutil
from pathlib import Path

import nox

# https://endoflife.date/python
py_versions = ["3.13", "3.14"]
OLDEST_PY, *MIDDLE_PY, LATEST_PY = py_versions
PYCLICHE_TEST_TEMP_DIR = Path("/", "tmp", "pycliche_test")

nox.options.default_venv_backend = "uv|virtualenv"
nox.options.sessions = [f"tests-{LATEST_PY}"]


def clean_up():
    if PYCLICHE_TEST_TEMP_DIR.exists():
        shutil.rmtree(PYCLICHE_TEST_TEMP_DIR, ignore_errors=True)


@nox.session(python=py_versions)
def tests(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--group=test",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )

    # Needed for assertions against `importlib.metadata.version`.
    session.install("-e", ".")

    posargs = list(session.posargs)
    use_pdb = "--pdb" in posargs

    pytest_args = [
        "--capture=no",
        "--verbosity=3",
        "--showlocals",
    ]

    if not use_pdb:
        pytest_args.append("--numprocesses=auto")

    try:
        session.run("pytest", "tests/", *pytest_args, *posargs)
    finally:
        if os.getenv("CI") != "true":
            clean_up()
