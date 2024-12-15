# pycliche - local development tooling

set positional-arguments

default:
  @just --list

test +args='':
  @uv sync --group test
  @uv run -m pytest tests/ -s -vvv -W always --pdb "$@"
