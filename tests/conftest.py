import shutil
from pathlib import Path

import copier
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


@pytest.fixture
def copier_copy(pycliche_root_dir: Path, pycliche_test_project_dir: Path):
    """Fixture to run `copier copy`, cleaning up destination directory beforehand."""

    def _run(copier_data: dict):
        if pycliche_test_project_dir.exists():
            shutil.rmtree(pycliche_test_project_dir)

        copier.run_copy(
            vcs_ref="HEAD",
            src_path=str(pycliche_root_dir),
            dst_path=str(pycliche_test_project_dir),
            defaults=True,
            data=copier_data,
        )

    return _run


def pytest_sessionstart(session):
    """Hook to perform initial setup before all tests."""
    if not PYCLICHE_TEST_TEMP_DIR.exists():
        PYCLICHE_TEST_TEMP_DIR.mkdir()
