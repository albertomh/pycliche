# pycliché

A simple template for starting Python projects.

## Prerequisites

To use `pycliche` the following must be available locally:

- [Python 3.10](https://docs.python.org/3.10/) or above
- [uv](https://docs.astral.sh/uv/)

## Develop

This repo follows trunk-based development. This means:

- the `main` branch should always be in a releasable state
- use short-lived feature branches

### Development prerequisites

In addition to the [Prerequisites](#prerequisites) above, you will need the
following to develop `pycliche`:

- [pre-commit](https://pre-commit.com/)

### Style

Code style is enforced by pre-commit hooks. Linter rules are configured in the `ruff`
tables in `pyproject.toml`.

```sh
# before you start developing, install pre-commit hooks
pre-commit install
```

Docstrings should follow the conventions set out in the [Google styleguide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

Please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
guidelines when writing commit messages. `commitlint` is enabled as
pre-commit hook. Valid commit types are defined in `.commitlintrc.yaml`.
