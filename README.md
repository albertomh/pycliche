# pycliché

![pycliche logo](docs/pycliche-logo-sm.webp "pycliche logo - a printing plate embossed with the Python logo")

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

Projects created using `pycliche` include:

- A basic Python package and entrypoint, configured via a `pyproject.toml`.
- A package intended to be managed via `uv`, but flexible enough to use alternatives such as Poetry.
- Scaffolding for unit tests run via `pytest`.
- Out-of-the-box code coverage reporting with `coverage.py`.
- Batteries-included `pre-commit` hook configuration to format, lint and run SAST.
- A `justfile` to enable using `just` as a task runner.
- Simple `Release Please` config to automate cutting releases via GitHub Actions.
- A `dependabot` configuration to keep Python packages & GitHub Actions up to date.

## Prerequisites

To use `pycliche` the following must be available locally:

- [Python 3.10](https://docs.python.org/3.10/) or above
- [uv](https://docs.astral.sh/uv/)

## Start a new project

Start a new project based on `pycliche`:

1. Navigate to the directory under which you wish to create a new project.
1. Run `uvx copier copy gh:albertomh/pycliche <project_name>` and follow the wizard.

This creates a directory under your current location. Follow the README in
the new directory to get started with your project.

NB. It is not necessary to clone `pycliche` itself to your local environment
in order to use it as a template. The `gh:albertomh/pycliche` argument
will use the latest version hosted on GitHub.

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

## Test

`pytest` is defined as a test dependency. Run unit tests with:

```sh
uv run -m pytest tests/ [-s] [-vvv] [-W always] [--pdb]
```

## Release

[Release Please](https://github.com/googleapis/release-please) is used to automate:

- Updating the [changelog](CHANGELOG.md).
- Calculating the new SemVer tag based on conventional commit types.
- Creating a new GitHub release.

Release Please is configured as a GitHub action ([release-please.yaml](.github/workflows/release-please.yaml)).
It keeps a release pull request open that is refreshed as changes are merged into `main`.
To cut a release, simply merge the release pull request.

### GitHub Personal Access Token

In order for Release Please to automate the above process, a GitHub Actions secret called
`PYCLICHE_RELEASE_PLEASE_TOKEN` must exist in GitHub ([albertomh/pycliche/settings/secrets/actions](albertomh/pycliche/settings/secrets/actions)).
The contents of this secret must be a Personal Access Token (PAT) with the following permissions:

```text
contents: write
pull-requests: write
```

For more information, consult the [release-please-action project](https://github.com/googleapis/release-please-action).
