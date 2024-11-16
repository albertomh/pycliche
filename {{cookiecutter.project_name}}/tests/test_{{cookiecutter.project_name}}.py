import pytest

from {{cookiecutter.project_name}} import main as entrypoint


def test_main_runs_without_error():
    """Test that the entrypoint executes without raising any exceptions."""
    try:
        entrypoint.main()
    except Exception as e:
        pytest.fail(f"main() raised an exception: {e}")
