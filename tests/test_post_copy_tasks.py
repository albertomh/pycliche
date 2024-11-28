# Test the effects of the tasks that run after generating or updating a project.

from pathlib import Path

from tests.conftest import is_git_repo


def test_is_git_repo(test_project_dir: Path, copier_copy, copier_input_data):
    copier_copy(copier_input_data)

    assert is_git_repo(test_project_dir), "The test project is not a Git repository."
