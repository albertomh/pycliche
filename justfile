# pycliche - local development tooling

set positional-arguments

default:
  @just --list

test +args='':
  @uv venv
  @uv sync --group test
  @uv pip install -e .
  @uv run -m pytest tests/ -s -vvv -W always --pdb "$@"
