# ruff: noqa: INP001

import nox

# https://endoflife.date/python
py_versions = ["3.13", "3.12"]
OLDEST_PY, *MIDDLE_PY, LATEST_PY = py_versions

nox.options.default_venv_backend = "uv"


def _run_tests(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--group=test",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )

    # Needed for assertions against `importlib.metadata.version`.
    session.install("-e", ".")

    session.run(
        "pytest", "tests/", "-s", "-vvv", "-W", "always", "--pdb", *session.posargs
    )


def _cov(session: nox.Session) -> None:
    session.run(
        "coverage",
        "run",
        "-m",
        "pytest",
        "tests/",
        "-s",
        "-vvv",
        "-W",
        "always",
        "--pdb",
        *session.posargs,
    )
    session.run("coverage", "report")
    session.run("coverage", "html")


@nox.session(python=[OLDEST_PY, LATEST_PY])
def tests_with_coverage(session):
    _run_tests(session)

    _cov(session)


@nox.session(python=MIDDLE_PY)
def tests(session):
    _run_tests(session)
