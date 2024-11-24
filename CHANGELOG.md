# Changelog

Notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.0.0](https://github.com/albertomh/pycliche/compare/v1.0.0...v2.0.0) (2024-11-23)

### Added

- copier.yaml config file.

### Changed

- Switch from cookiecutter to copier as the project templating tool.

### Removed

- cookiecutter.json config file.

## [1.0.0] (2024-11-17)

### Added

- Project template package structure and entrypoint.
- cookiecutter.json config file.
- Minimal unit test suite structure. Configuration for running tests and reporting on coverage.
- git hooks for both pycliché and the project template, including:
  - commitlint
  - ruff (linter & formatter)
  - bandit (SAST)
