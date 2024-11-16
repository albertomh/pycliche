# {{cookiecutter.project_name}}

## Prerequisites

To use `{{cookiecutter.project_name}}` the following must be available locally:

- [Python {{cookiecutter.python_version}}](https://docs.python.org/{{cookiecutter.python_version}}/) or above
- [uv](https://docs.astral.sh/uv/)


## Develop

This repo follows trunk-based development. This means:

- the `main` branch should always be in a releasable state
- use short-lived feature branches

### Development prerequisites

In addition to the [Prerequisites](#prerequisites) above, you will need the following to
develop `{{cookiecutter.project_name}}`:

- [pre-commit](https://pre-commit.com/)

### Dependency management

Dependencies are defined in the `pyproject.toml` file. `uv` is used to manage dependencies:

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
```

Docstrings should follow the conventions set out in the [Google styleguide](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings).

Please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/)
guidelines when writing commit messages. `commitlint` is enabled as a pre-commit hook.
Valid commit types are defined in `.commitlintrc.yaml`.
