# Test the custom validators defined for certain questions in `copier.yaml`.


from typing import Callable

import pytest


@pytest.mark.parametrize(
    "question, answer, error_msg",
    [
        ("author_name", "Francisco de Quevedo", None),
        ("author_name", "", "author_name cannot be empty"),
        ("initial_version", "0.0.0", None),
        ("initial_version", "", "Invalid choice"),
    ],
)
def test_validator_is_empty(
    question: str,
    answer: str,
    error_msg: str | None,
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
):
    def _copier_copy_with_project_name():
        copier_copy(
            {
                **copier_input_data,
                question: answer,
            }
        )

    if error_msg is None:
        try:
            _copier_copy_with_project_name()
        except Exception as e:
            pytest.fail(f"Unexpected exception raised: {str(e)}")

    else:
        with pytest.raises(ValueError) as exc_info:
            _copier_copy_with_project_name()
        assert str(exc_info.value).endswith(error_msg)


@pytest.mark.parametrize(
    "project_name, should_raise",
    [
        ("ok_project", False),
        ("MyProjectName", True),
        ("dash-it", True),
        ("2whynumber", True),
    ],
)
def test_validator_project_name(
    project_name: str,
    should_raise: bool,
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
):
    def _copier_copy_with_project_name():
        copier_copy(
            {
                **copier_input_data,
                "project_name": project_name,
            }
        )

    expected_error_msg = (
        "Validation error for question 'project_name': project_name must "
        "start with a letter, be lowercase and may contain underscores"
    )

    if should_raise:
        with pytest.raises(ValueError) as exc_info:
            _copier_copy_with_project_name()
        assert str(exc_info.value) == expected_error_msg

    else:
        try:
            _copier_copy_with_project_name()
        except Exception as e:
            pytest.fail(f"Unexpected exception raised: {str(e)}")
