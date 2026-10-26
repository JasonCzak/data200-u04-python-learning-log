"""The fictional sample programs run, match the reference output, and support the sample's run results."""
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from PIL import Image

REPO = Path(__file__).resolve().parents[1]
SAMPLES = REPO / "src" / "sample_entries"
REFERENCE = REPO / "figures" / "reference"

# Each program and the values typed at its prompts for the reference output.
ENTRIES = {
    "week01_entry01_temperature_converter": "0\n",
    "week01_entry02_grade_classifier": "90\n",
    "week01_entry03_average_calculator": "10\n20\n30\n40\n50\n",
    "week01_entry04_data_summary": "",
}


def run(script, typed="", cwd=None):
    return subprocess.run([sys.executable, "-W", "error", str(script)], input=typed, cwd=cwd,
                          capture_output=True, text=True, check=False)


def lines(text):
    return [line.rstrip() for line in text.splitlines()]


def test_expected_programs_present():
    assert sorted(p.stem for p in SAMPLES.glob("*.py")) == sorted(ENTRIES)


@pytest.mark.parametrize("entry", ENTRIES)
def test_matches_reference(entry):
    result = run(SAMPLES / f"{entry}.py", ENTRIES[entry])
    assert result.returncode == 0, result.stderr
    expected = (REFERENCE / f"{entry}_output.txt").read_text(encoding="utf-8")
    assert lines(result.stdout) == lines(expected)


@pytest.mark.parametrize("entry", ENTRIES)
def test_runs_from_another_folder_and_flat(entry, tmp_path):
    shutil.copy(SAMPLES / f"{entry}.py", tmp_path)
    for cwd in (tmp_path, REPO):
        result = run(tmp_path / f"{entry}.py", ENTRIES[entry], cwd=cwd)
        assert result.returncode == 0, result.stderr
    assert [p.name for p in tmp_path.iterdir()] == [f"{entry}.py"], "the programs write no files"


@pytest.mark.parametrize("entry", ENTRIES)
def test_labeled_fictional(entry):
    assert "Fictional sample log entry" in (SAMPLES / f"{entry}.py").read_text(encoding="utf-8")


@pytest.mark.parametrize("celsius, expected", [("0", "32.00"), ("100", "212.00")])
def test_entry1_run_result(celsius, expected):
    assert f"Temperature in Fahrenheit: {expected}" in run(SAMPLES / f"{list(ENTRIES)[0]}.py", celsius + "\n").stdout


@pytest.mark.parametrize("score, grade", [("95", "A"), ("87", "B"), ("72", "C"), ("55", "F"),
                                          ("90", "A"), ("80", "B"), ("70", "C"), ("60", "D")])
def test_entry2_run_result(score, grade):
    assert run(SAMPLES / f"{list(ENTRIES)[1]}.py", score + "\n").stdout.endswith(f"Grade: {grade}\n")


def test_entry3_accepts_decimals():
    result = run(SAMPLES / f"{list(ENTRIES)[2]}.py", "1.5\n2.5\n3.5\n4.5\n5.5\n")
    assert "Average = 3.50" in result.stdout


def test_placeholder_image_reproduced(tmp_path):
    shutil.copy(REPO / "src" / "make_screenshot_placeholder.py", tmp_path)
    result = run(tmp_path / "make_screenshot_placeholder.py", cwd=tmp_path)
    assert result.returncode == 0, result.stderr
    assert str(tmp_path) not in result.stdout
    with Image.open(tmp_path / "screenshot-placeholder.png") as made, \
            Image.open(REPO / "report" / "screenshot-placeholder.png") as committed:
        assert made.size == committed.size
