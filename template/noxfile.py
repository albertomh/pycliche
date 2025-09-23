# ruff: noqa: INP001

import nox

# https://endoflife.date/python
py_versions = ["3.12", "3.13"]
OLDEST_PY, *MIDDLE_PY, LATEST_PY = py_versions

nox.options.default_venv_backend = "uv"
nox.options.sessions = [f"tests_with_coverage-{LATEST_PY}"]


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


def make_pytest_args(posargs: list) -> list[str]:
    pytest_args = [
        "--capture=no",
        "--verbosity=3",
        "--pythonwarnings=always",
    ]

    use_pdb = "--pdb" in posargs
    if not use_pdb:
        pytest_args.append("--numprocesses=auto")

    return pytest_args


@nox.session(python=MIDDLE_PY)
def tests(session: nox.Session) -> None:
    _install_deps(session)

    pytest_args = make_pytest_args(list(session.posargs))
    session.run("pytest", "tests/", *pytest_args, *session.posargs)


@nox.session(python=[OLDEST_PY, LATEST_PY])
def tests_with_coverage(session: nox.Session) -> None:
    _install_deps(session)

    session.run("coverage", "erase")
    pytest_args = make_pytest_args(list(session.posargs))
    session.run(
        "coverage",
        "run",
        # "--source", ".",
        "-m",
        "pytest",
        "tests/",
        *pytest_args,
        *session.posargs,
    )
    session.run("coverage", "report")
    session.run("coverage", "html")
