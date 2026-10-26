"""The notebook runs from top to bottom and is stored with outputs cleared."""
import shutil
from pathlib import Path

import nbformat
import pytest
from nbclient import NotebookClient

REPO = Path(__file__).resolve().parents[1]
NOTEBOOKS = sorted((REPO / "notebooks").glob("*.ipynb"))


def test_expected_notebooks_present():
    assert [nb.name for nb in NOTEBOOKS] == ["01-worked-example.ipynb"]


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_outputs_cleared(path):
    nb = nbformat.read(path, as_version=4)
    for cell in nb.cells:
        if cell.cell_type == "code":
            assert cell.outputs == [] and cell.execution_count is None


@pytest.mark.parametrize("path", NOTEBOOKS, ids=lambda p: p.name)
def test_notebook_runs(path, tmp_path):
    shutil.copytree(REPO / "src", tmp_path / "src", ignore=shutil.ignore_patterns("__pycache__"))
    (tmp_path / "notebooks").mkdir()
    nb = nbformat.read(path, as_version=4)
    NotebookClient(nb, timeout=180, kernel_name="python3",
                   resources={"metadata": {"path": str(tmp_path / "notebooks")}}).execute()
    printed = "".join(output.get("text", "") for cell in nb.cells if cell.cell_type == "code"
                      for output in cell.outputs)
    assert "Temperature in Fahrenheit: 212.00" in printed
    assert "90 -> A" in printed and "89.9 -> B" in printed
    assert "Average: 20.29" in printed
