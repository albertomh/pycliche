import json
import os
import re
import tomllib
from collections.abc import Callable
from pathlib import Path

import pytest
import yaml
from sh import ErrorReturnCode, git, python, uv
from sh import pytest as sh_pytest

from tests._utils import count_dirs_and_files


@pytest.mark.integration
@pytest.mark.smoke
def test_pycliche_jinja_templates_converted(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    pycliche_root_dir: Path,
    test_project_dir: Path,
):
    """Validate that generating a project converts Jinja templates to files."""
    copier_copy(copier_input_data)

    template_files: list[Path] = [
        f.relative_to(pycliche_root_dir / "template")
        for f in pycliche_root_dir.rglob("*.jinja")
        if not f.name.startswith("{")
    ]

    def _transform_file_name(fname: str):
        fname = fname.replace("{{project_name}}", copier_input_data["project_name"])
        fname = fname.removesuffix(".jinja")
        return fname

    template_file_names: list[str] = [str(f) for f in template_files]
    template_file_names: list[str] = list(map(_transform_file_name, template_file_names))

    for file_name in template_file_names:
        expected_file_path = test_project_dir / file_name

        assert expected_file_path.exists(), (
            f"Expected file {expected_file_path} not found."
        )


@pytest.mark.integration
@pytest.mark.parametrize(
    ("is_github_project", "expected_directory_count", "expected_file_count"),
    [(True, 4, 17), (False, 3, 15)],
)
def test_is_github_project(
    is_github_project: bool,
    expected_directory_count: int,
    expected_file_count: int,
    test_project_dir: Path,
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
):
    copier_copy(
        {
            **copier_input_data,
            "is_github_project": is_github_project,
        }
    )

    num_dirs, num_files = count_dirs_and_files(test_project_dir)

    assert num_dirs == expected_directory_count
    assert num_files == expected_file_count


@pytest.mark.integration
def test_version_is_importable(
    install_test_project,
    test_project_name: str,
):
    from importlib.metadata import version

    assert version(test_project_name) == "0.0.0"


@pytest.mark.integration
@pytest.mark.smoke
def test_entrypoint_logs_info(
    install_test_project,
    test_project_name: str,
):
    result = python("-m", f"{test_project_name}.main")

    json_stdout = json.loads(result)
    assert re.match(rf"{test_project_name}", json_stdout["event"]), (
        f"Unexpected log: {json_stdout['event']}"
    )
    assert re.match(r"v\d+\.\d+\.\d+", json_stdout["version"]), (
        f"Unexpected log: {json_stdout['version']}"
    )
    assert json_stdout["level"] == "info"


@pytest.mark.integration
def test_generated_toml_is_valid(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
):
    copier_copy(copier_input_data)

    toml_files = list(test_project_dir.rglob("*.toml"))
    assert toml_files, "No TOML files found in the generated project."

    for file_path in toml_files:
        try:
            with open(file_path, "rb") as f:  # must be binary for tomllib
                tomllib.load(f)
        except tomllib.TOMLDecodeError as e:
            pytest.fail(f"Invalid TOML file: {file_path}\nError: {e}")


@pytest.mark.integration
def test_generated_yaml_is_valid(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
):
    copier_copy(copier_input_data)

    yaml_files = list(test_project_dir.rglob("*.yaml")) + list(
        test_project_dir.rglob("*.yml")
    )
    assert yaml_files, "No YAML files found in the generated project."

    for file_path in yaml_files:
        with open(file_path) as f:
            try:
                yaml.safe_load(f)
            except yaml.YAMLError as e:
                pytest.fail(f"Invalid YAML file: {file_path}\nError: {e}")


@pytest.mark.integration
@pytest.mark.smoke
def test_generated_project_tests_run_successfully(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
):
    copier_copy(copier_input_data)

    try:
        install_res = uv(
            "pip",
            "install",
            "-e",
            ".",
            _cwd=test_project_dir,
        )
    except ErrorReturnCode:
        pytest.fail(
            f"Dependency installation failed:\n{install_res.stdout}\n{install_res.stderr}"
        )

    try:
        result = sh_pytest(_cwd=test_project_dir)
    except ErrorReturnCode:
        pytest.fail(f"Pytest failed:\n{result.stdout}\n{result.stderr}")


@pytest.mark.integration
@pytest.mark.smoke
def test_generated_project_pre_commit_hooks_run_successfully(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
):
    copier_copy(copier_input_data)

    # prek will only run against files tracked by git
    git("init", _cwd=test_project_dir)
    git("add", ".", _cwd=test_project_dir)

    env = os.environ.copy()
    env["SKIP"] = "no-commit-to-branch"
    prek_res = uv(
        "run",
        "prek",
        "run",
        "--all-files",
        _cwd=test_project_dir,
        _env=env,
        _return_cmd=True,
    )
    assert prek_res.exit_code == 0, (
        f"prek pre-commit hooks failed:\n{prek_res.stdout}\n{prek_res.stderr}"
    )
