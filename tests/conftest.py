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
