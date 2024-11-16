# pycliché

![pycliche logo](docs/pycliche-logo-sm.webp "pycliche logo - a printing plate embossed with the Python logo")

A simple template for starting Python projects.

[![python: 3.12](https://img.shields.io/badge/3.12-4584b6?logo=python&logoColor=ffde57)](https://docs.python.org/3.12/whatsnew/3.12.html)
[![justfile](https://img.shields.io/badge/🤖_justfile-EFF1F3)](https://github.com/casey/just)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&labelColor=261230&color=de60e9)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?logo=pre-commit&logoColor=1f2d23)](https://github.com/pre-commit/pre-commit)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&labelColor=261230&color=d8ff64)](https://github.com/astral-sh/ruff)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)](https://github.com/pytest-dev/pytest)
[![coverage](https://img.shields.io/badge/😴_coverage-59aabd)](https://coverage.readthedocs.io/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

## Prerequisites

To use `pycliche` the following must be available locally:

- [Python 3.10](https://docs.python.org/3.10/) or above
- [uv](https://docs.astral.sh/uv/)

## Generate a new project

Create a new project based on `pycliche`:

1. Navigate to the directory under which you wish to create a new project.
1. Run `uvx cookiecutter gh:albertomh/pycliche` and follow the wizard.

Note that it is not necessary to clone `pycliche` itself to your local
environment in order to use it as a template. The `gh:albertomh/pycliche`
argument will use the latest version hosted on GitHub.

## Develop

This repo follows trunk-based development. This means:

- the `main` branch should always be in a releasable state
- use short-lived feature branches

### Development prerequisites

In addition to the [Prerequisites](#prerequisites) above, you will need the
following to develop `pycliche`:

- [pre-commit](https://pre-commit.com/)

### Dependency management

Dependencies are defined in the `pyproject.toml` file. `uv` is used to manage
dependencies:

```sh
# add a dependency to the project
uv add some-package
```

### Style

Code style is enforced by pre-commit hooks. Linter rules are configured in the `ruff`
tables in `pyproject.toml`.

```sh
# before you start developing, install pre-commit hooks
pre-commit install

# update pre-commit hooks
pre-commit autoupdate
```

Docstrings should follow the conventions set out in the [Google styleguide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

Please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
guidelines when writing commit messages. `commitlint` is enabled as
pre-commit hook. Valid commit types are defined in `.commitlintrc.yaml`.
