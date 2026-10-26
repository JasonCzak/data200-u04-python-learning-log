"""Every .tex file compiles without errors or warnings, and the committed PDFs are present."""
import re
import shutil
import subprocess
from pathlib import Path

import pytest

REPO = Path(__file__).resolve().parents[1]
FOLDERS = [f for f in ("handout", "report", "solutions") if (REPO / f).is_dir()]
DOCUMENTS = sorted(p.relative_to(REPO) for folder in FOLDERS for p in (REPO / folder).glob("*.tex"))
COMMITTED_PDF = [d for d in DOCUMENTS if d.name != "template.tex"]
PROBLEMS = re.compile(r"^!|Warning|Overfull|Underfull", re.MULTILINE)

needs_pdflatex = pytest.mark.skipif(shutil.which("pdflatex") is None, reason="pdflatex is not installed")


def compile_copy(document, tmp_path):
    """Compile in a temporary copy (the sample entries read ../src) until references settle."""
    for folder in FOLDERS + ["src"]:
        shutil.copytree(REPO / folder, tmp_path / folder, ignore=shutil.ignore_patterns("*.pdf", "__pycache__"))
    workdir = tmp_path / document.parent
    for _ in range(3):
        result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", document.name],
                                cwd=workdir, capture_output=True, text=True, errors="replace", check=False)
        assert result.returncode == 0, result.stdout[-2000:]
        log = (workdir / document.with_suffix(".log").name).read_text(errors="replace")
        if "Rerun" not in log:
            break
    return log


@needs_pdflatex
@pytest.mark.parametrize("document", DOCUMENTS, ids=str)
def test_compiles_cleanly(document, tmp_path):
    log = compile_copy(document, tmp_path)
    assert not PROBLEMS.findall(log), [line for line in log.splitlines() if PROBLEMS.search(line)]


@needs_pdflatex
def test_sample_compiles_flat(tmp_path):
    """The sample also compiles with its programs and image copied next to it."""
    for path in [REPO / "report" / "fictional-sample-entries.tex", REPO / "report" / "screenshot-placeholder.png",
                 *(REPO / "src" / "sample_entries").glob("*.py")]:
        shutil.copy(path, tmp_path)
    for _ in range(2):
        result = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "fictional-sample-entries.tex"],
                                cwd=tmp_path, capture_output=True, text=True, errors="replace", check=False)
        assert result.returncode == 0, result.stdout[-2000:]


@pytest.mark.parametrize("document", COMMITTED_PDF, ids=str)
def test_compiled_pdf_is_committed(document):
    committed = REPO / document.with_suffix(".pdf")
    assert committed.is_file() and committed.stat().st_size > 0, f"{committed.name} is missing"
