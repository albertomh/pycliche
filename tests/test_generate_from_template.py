from pathlib import Path


def test_pycliche_jinja_templates_converted(
    copier_copy,
    pycliche_root_dir: Path,
    test_project_dir: Path,
    copier_input_data,
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
