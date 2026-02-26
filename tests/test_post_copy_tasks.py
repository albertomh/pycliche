# Test the effects of the tasks that run after generating or updating a project.

from collections.abc import Callable
from pathlib import Path

import pytest

from tests.conftest import is_git_repo


@pytest.mark.integration
@pytest.mark.smoke
def test_is_git_repo(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
):
    copier_copy(copier_input_data)

    assert is_git_repo(test_project_dir), "The test project is not a Git repository."


@pytest.mark.integration
@pytest.mark.smoke
def test_uv_lockfile_exists(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
):
    copier_copy(copier_input_data)

    uv_lock_file = test_project_dir / "uv.lock"
    assert uv_lock_file.exists(), f"Expected lock file {uv_lock_file} not found."


@pytest.mark.integration
@pytest.mark.smoke
def test_generated_project_message_after_copy(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    capsys: pytest.CaptureFixture[str],
):
    copier_copy(copier_input_data)
    captured = capsys.readouterr()

    assert "Your project is ready!" in captured.err
    assert "Please update the LICENSE file" in captured.err
