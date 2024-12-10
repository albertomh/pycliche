# pycliche - local development tooling

default:
  @just --list

test:
  @uv sync --group test
  @uv run -m pytest tests/ -s -vvv -W always --pdb
