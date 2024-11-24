# Changelog

Notable changes to this project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [2.1.0](https://github.com/albertomh/pycliche/compare/v2.0.0...v2.1.0) (2024-11-24)


### Features

* Add Release Please config & GitHub Action to the project template ([#12](https://github.com/albertomh/pycliche/issues/12)) ([2247823](https://github.com/albertomh/pycliche/commit/224782304359d35a1e995f43d3c748460249478f))


### Bug Fixes

* Add 'deps' as a valid commit type in the project template ([#10](https://github.com/albertomh/pycliche/issues/10)) ([59e29f1](https://github.com/albertomh/pycliche/commit/59e29f1fcf1d1b1cdc9d56b6f4e5e3d80985a034))

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
