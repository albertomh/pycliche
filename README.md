<!-- markdownlint-disable MD041 first-line-heading/first-line-h1 -->

<!-- markdownlint-disable MD033 no-inline-html -->
<p align="center">
  <!-- markdownlint-disable MD013 line-length -->
  <img src="docs/media/pycliche_wordmark-logo.webp" alt="pycliché logo - a printing plate embossed with the Python logo and the word 'pycliché'"/>
  <!-- markdownlint-enable MD013 line-length -->
</p>

`pycliche` - a Python project template with opinionated tooling.

[![python: 3.10](https://img.shields.io/badge/>=3.10-4584b6?logo=python&logoColor=ffde57)](https://docs.python.org/3.10/whatsnew/3.10.html)
[![Copier](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/albertomh/pycliche/main/docs/media/copier-badge.json)](https://github.com/copier-org/copier)
[![justfile](https://img.shields.io/badge/🤖_justfile-EFF1F3)](https://github.com/casey/just)
[![uv](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/uv/main/assets/badge/v0.json&labelColor=261230&color=de60e9)](https://github.com/astral-sh/uv)
[![pre-commit](https://img.shields.io/badge/pre--commit-FAB040?logo=pre-commit&logoColor=1f2d23)](https://github.com/pre-commit/pre-commit)
[![ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json&labelColor=261230&color=d8ff64)](https://github.com/astral-sh/ruff)
[![IPython](https://img.shields.io/badge/IP[y]:-3465a4)](https://ipython.readthedocs.io/en/stable/)
[![structlog](https://img.shields.io/badge/🪵_structlog-000)](https://github.com/hynek/structlog)
[![pytest](https://img.shields.io/badge/pytest-0A9EDC?logo=pytest&logoColor=white)](https://github.com/pytest-dev/pytest)
[![coverage](https://img.shields.io/badge/😴_coverage-59aabd)](https://coverage.readthedocs.io/)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)
[![Release Please](https://img.shields.io/badge/📦_Release_Please-6C97BB)](https://github.com/googleapis/release-please)
[![CI](https://github.com/albertomh/pycliche/actions/workflows/ci.yaml/badge.svg)](https://github.com/albertomh/pycliche/actions/workflows/ci.yaml)

Projects created using `pycliche` include:

- A basic Python package and entrypoint, configured via a `pyproject.toml`.
- Dependencies managed via `uv`, using a `uv.lock` file for consistent and reproducible builds.
- IPython as the default shell.
- Simple configuration to enhance your logs with `structlog`.
- Scaffolding for unit tests run via `pytest`.
- Out-of-the-box code coverage reporting with `coverage.py`.
- Batteries-included `pre-commit` hook configuration to lint & format code, and run SAST.
- A `justfile` to enable using `just` as a task runner.

Optionally, for projects intended to be hosted on GitHub, also include:

- GitHub Actions to:
  - Automate cutting releases via `Release Please`.
  - Run `pre-commit` hooks and `pytest` as part of a Continuous Integration pipeline.
- A `dependabot` configuration to keep Python packages & GitHub Actions up to date.

<p align="center">
  <!-- markdownlint-disable MD013 line-length -->
  <img src="docs/media/pycliche-demo-2.9.1.gif" alt="Creating a Python project using pycliche 2.9.1"/>
  <!-- markdownlint-enable MD013 line-length -->
</p>

## Prerequisites

To use `pycliche` the following must be available locally:

- [Python 3.10](https://docs.python.org/3.10/) or above
- [uv](https://docs.astral.sh/uv/)

## Bootstrap a new Python project

Bootstrap a new Python project using `pycliche`:

1. Navigate to the directory under which you wish to create a new project.
1. Run `uvx copier copy --trust gh:albertomh/pycliche <project_name>` and follow the wizard.

This creates a directory under your current location. Follow the README in the new directory
to get started with your project.

Please note:

- it is not necessary to clone `pycliche`. The `gh:albertomh/pycliche` argument will pull
  the latest tag from GitHub.
- the `--trust` flag is necessary since a post-creation task initialises the new directory
  as a git repository and generates a `uv` lockfile.

## Update existing projects

To update a project created using an older version of `pycliche` to a newer version of the
template:

```sh
cd ~/Projects/existing_project/
uvx copier update --skip-answered --trust [--vcs-ref=<TAG>]
```

If the `--vcs-ref` flag is not specified `copier` will use the latest `pycliche` tag.

---

## Develop

The developer README ([docs/README-dev.md](docs/README-dev.md)) covers how to work on
`pycliche` itself. It covers:

- [Develop](docs/README-dev.md#develop)
  - [Development prerequisites](docs/README-dev.md#development-prerequisites)
  - [Recursive pycliche](docs/README-dev.md#recursive-pycliche)
  - [Git principles](docs/README-dev.md#git-principles)
  - [Dependency management](docs/README-dev.md#dependency-management)
    - [Updating dependencies in the template](docs/README-dev.md#updating-dependencies-in-the-template)
  - [Generate project using development version](docs/README-dev.md#generate-project-using-development-version)
  - [Style](docs/README-dev.md#style)

- [Test](docs/README-dev.md#test)

- [Release](docs/README-dev.md#release)
  - [GitHub Personal Access Token](docs/README-dev.md#github-personal-access-token)

- [Record demo](docs/README-dev.md#record-demo)

---

## Acknowledgements

Several tooling choices have been guided by the work of [Adam Johnson](https://adamj.eu/tech/).

The `pycliche` logo is typeset in [Allerta Stencil](https://fonts.google.com/specimen/Allerta+Stencil).
