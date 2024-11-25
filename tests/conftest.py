import shutil
import subprocess
from pathlib import Path

import pytest

PYCLICHE_TEST_TEMP_DIR = Path("/", "tmp", "pycliche_test")


@pytest.fixture
def pycliche_root_dir() -> Path:
    """Provides the path to the pycliche project root."""
    project_root = Path(__file__).resolve().parent.parent
    if not project_root.exists():
        pytest.fail(f"pycliche project root does not exist at {project_root}")
    return project_root


@pytest.fixture
def pycliche_test_temp_dir() -> Path:
    """"""
    return PYCLICHE_TEST_TEMP_DIR


@pytest.fixture
def pycliche_test_project_dir(pycliche_test_temp_dir) -> Path:
    """"""
    return pycliche_test_temp_dir / "test_project"


def copier_data_args(data: dict) -> list[str]:
    """
    Generates --data arguments for copier.
    Accepts a dictionary and converts it to a list of key-value pairs.
    """

    def quote_if_has_space(value):
        return f"'{value}'" if (isinstance(value, str) and " " in value) else value

    args = []
    for key, value in data.items():
        args.append("--data")
        args.append(f"{key}={quote_if_has_space(value)}")
    return args


@pytest.fixture
def run_copier(pycliche_root_dir: Path, pycliche_test_project_dir: Path):
    """
    Fixture to run `copier copy` (via uvx) and clean up destination_path before each test.
    """

    def _run(copier_input_data: dict):
        # clean up destination directory before running copier
        if pycliche_test_project_dir.exists():
            shutil.rmtree(pycliche_test_project_dir)

        pycliche_test_project_dir.mkdir(parents=True)

        copier_data = copier_data_args(copier_input_data)

        subprocess.run(
            [
                "uvx",
                "copier",
                "copy",
                "--defaults",
                *copier_data,
                str(pycliche_root_dir),
                str(pycliche_test_project_dir),
            ],
            check=True,
        )

    return _run


def pytest_sessionstart(session):
    """Hook to perform initial setup before all tests."""
    if not PYCLICHE_TEST_TEMP_DIR.exists():
        PYCLICHE_TEST_TEMP_DIR.mkdir()
