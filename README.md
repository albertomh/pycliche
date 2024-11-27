# pycliché

![pycliche logo](docs/media/pycliche-logo-sm.webp "pycliche logo - a printing plate embossed with the Python logo")

A Python project template with opinionated tooling.

[![python: 3.10](https://img.shields.io/badge/>=3.10-4584b6?logo=python&logoColor=ffde57)](https://docs.python.org/3.10/whatsnew/3.10.html)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/albertomh/pycliche/main/docs/copier-badge.json)](https://github.com/copier-org/copier)
[![justfile](https://img.shields.io/badge/🤖_justfile-EFF1F3)](https://github.com/casey/just)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&labelColor=261230&color=de60e9)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?logo=pre-commit&logoColor=1f2d23)](https://github.com/pre-commit/pre-commit)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&labelColor=261230&color=d8ff64)](https://github.com/astral-sh/ruff)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)](https://github.com/pytest-dev/pytest)
[![coverage](https://img.shields.io/badge/😴_coverage-59aabd)](https://coverage.readthedocs.io/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Release Please](https://img.shields.io/badge/📦_Release_Please-6C97BB)](https://github.com/googleapis/release-please)
[![CI](https://github.com/albertomh/pycliche/actions/workflows/ci.yaml/badge.svg)](https://github.com/albertomh/pycliche/actions/workflows/ci.yaml)

Projects created using `pycliche` include:

- A basic Python package and entrypoint, configured via a `pyproject.toml`.
- A package intended to be managed via `uv`, but flexible enough to use alternatives such as Poetry.
- Scaffolding for unit tests run via `pytest`.
- Out-of-the-box code coverage reporting with `coverage.py`.
- Batteries-included `pre-commit` hook configuration to format, lint and run SAST.
- A `justfile` to enable using `just` as a task runner.

Optionally, for projects intended to be hosted on GitHub, also include:  

- GitHub Actions to:
  - Automate cutting releases via `Release Please`.
  - Run `pre-commit` hooks and `pytest` as part of a Continuous Integration pipeline.
- A `dependabot` configuration to keep Python packages & GitHub Actions up to date.

![Creating a new Python project using pycliche 2.3.0](docs/media/pycliche-demo-2.3.0-sm.gif)

## Prerequisites

To use `pycliche` the following must be available locally:

- [Python 3.10](https://docs.python.org/3.10/) or above
- [uv](https://docs.astral.sh/uv/)

## Bootstrap a new Python project

Bootstrap a new Python project using `pycliche`:

1. Navigate to the directory under which you wish to create a new project.
1. Run `uvx copier copy gh:albertomh/pycliche <project_name>` and follow the wizard.

This creates a directory under your current location. Follow the README in
the new directory to get started with your project.

NB. It is not necessary to clone `pycliche` to your local environment in order to use it
as a template. The `gh:albertomh/pycliche` argument will pull the latest tag from GitHub.

## Update existing projects

To update a project created using an older version of `pycliche` to a newer version of the
template:

```sh
cd ~/Projects/existing_project/
uvx copier update --skip-answered
```

---

## Develop

The developer README ([docs/README-dev.md](docs/README-dev.md)) covers how to work on
`pycliche` itself. It covers:

- [Develop](docs/README-dev.md#develop)
  - [Development prerequisites](docs/README-dev.md#development-prerequisites)
  - [Git principles](docs/README-dev.md#git-principles)
  - [Dependency management](docs/README-dev.md#dependency-management)
  - [Generate project using development version](docs/README-dev.md#generate-project-using-development-version)
  - [Style](docs/README-dev.md#style)

- [Test](docs/README-dev.md#test)

- [Release](docs/README-dev.md#release)
  - [GitHub Personal Access Token](docs/README-dev.md#github-personal-access-token)

- [Record demo](docs/README-dev.md#record-demo)
