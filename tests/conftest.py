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
def test_project_dir(pycliche_test_temp_dir) -> Path:
    """"""
    return pycliche_test_temp_dir / "test_project"


@pytest.fixture
def copier_input_data() -> dict:
    """Answers to core pycliche template questions."""
    return {
        "project_name": "test_project",
        "author_name": "Miguel de Cervantes",
        "author_email": "mike@alcala.net",
    }


@pytest.fixture
def copier_copy(pycliche_root_dir: Path, test_project_dir: Path):
    """
    Fixture to run `copier copy`, cleaning up destination directory beforehand.
    Uses the `pycliche_root_dir` & `test_project_dir` fixtures as source and
    destination directories respectively, so tests should use these fixtures
    """

    def _run(copier_data: dict):
        if test_project_dir.exists():
            shutil.rmtree(test_project_dir)

        copier.run_copy(
            vcs_ref="HEAD",
            src_path=str(pycliche_root_dir),
            dst_path=str(test_project_dir),
            defaults=True,
            data=copier_data,
        )

    return _run


def pytest_sessionstart(session):
    """Hook to perform initial setup before all tests."""
    if not PYCLICHE_TEST_TEMP_DIR.exists():
        PYCLICHE_TEST_TEMP_DIR.mkdir()
