import subprocess
import sys
from pathlib import Path
from typing import Callable

import pytest

from tests._utils import count_dirs_and_files


def test_pycliche_jinja_templates_converted(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    pycliche_root_dir: Path,
    test_project_dir: Path,
):
    """
    Smoke test to validate the generation process converted Jinja templates to files.
    """
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

        assert (
            expected_file_path.exists()
        ), f"Expected file {expected_file_path} not found."


@pytest.mark.parametrize(
    "is_github_project, expected_directory_count, expected_file_count",
    [(True, 4, 14), (False, 3, 12)],
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


def test_version_is_importable(
    copier_copy: Callable[[dict], None],
    copier_input_data: dict,
    test_project_dir: Path,
    test_project_name: str,
):
    copier_copy(copier_input_data)
    subprocess.run(
        [sys.executable, "-m", "pip", "install", str(test_project_dir)],
        check=True,
    )

    from importlib.metadata import version

    assert version(test_project_name) == "0.1.0"

    subprocess.run(
        [sys.executable, "-m", "pip", "uninstall", "-y", test_project_name],
        check=True,
    )
