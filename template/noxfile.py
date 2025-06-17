# ruff: noqa: INP001

import nox

# https://endoflife.date/python
py_versions = ["3.13", "3.12"]
OLDEST_PY, *MIDDLE_PY, LATEST_PY = py_versions

nox.options.default_venv_backend = "uv"

run_tests_args = ["pytest", "tests/", "-s", "-vvv", "-W", "always", "--pdb"]


def _install_deps(session: nox.Session) -> None:
    session.run_install(
        "uv",
        "sync",
        "--group=test",
        f"--python={session.virtualenv.location}",
        env={"UV_PROJECT_ENVIRONMENT": session.virtualenv.location},
    )
    # Needed for assertions against `importlib.metadata.version`.
    session.install("-e", ".")


@nox.session(python=MIDDLE_PY)
def tests(session: nox.Session) -> None:
    _install_deps(session)

    session.run(*run_tests_args)


@nox.session(python=[OLDEST_PY, LATEST_PY])
def tests_with_coverage(session: nox.Session) -> None:
    _install_deps(session)

    session.run("coverage", "erase")
    session.run(
        "coverage",
        "run",
        # "--source", ".",
        "-m",
        *run_tests_args,
        *session.posargs,
    )
    session.run("coverage", "report")
    session.run("coverage", "html")
