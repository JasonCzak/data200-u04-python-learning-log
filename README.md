# Unit 4: Python Learning Log

Part of DATA 200: Introduction to Data Science, James Madison University · Jason E. Czak

← [Unit 3](https://github.com/JasonCzak/data200-u03-python-camp) · [Course home](https://github.com/JasonCzak/data200) · Unit 5 (coming soon) →

## What you'll learn
- Practice Python regularly and document what you tried, what went wrong, and how you fixed it.
- Write each program as its own uniquely named, commented Python file.
- Test programs with values you can check by hand, including exact boundary values.
- Show evidence that your code runs on your own computer.
- Keep a LaTeX report whose code listings match the files you submit.
- Explain your growth with specific evidence from your own entries.

## Before you start
You need the course Python environment (see Setup below; this unit adds nothing to it) and a working LaTeX installation from the course setup. If you cannot install software on your computer, contact the instructor for the course's approved alternative.

## The task
You keep a log of your Python practice for the rest of the semester, with at least four substantive entries per week. Each entry gives the date, time spent, learning focus, and resources; a paragraph on what you attempted, where you had difficulty, what you changed, and how you checked the result; one uniquely named Python file; an explanation of what the program does; its complete code in your LaTeX report; and a screenshot showing that it ran on your own computer. Entries can come from homework, guided class examples, tutorials, or independent practice, as long as the narrative, code, debugging, and screenshots are your own.

You start from `report/template.tex`. Four fictional sample entries in [`report/fictional-sample-entries.pdf`](report/fictional-sample-entries.pdf) model the expected level of detail; they are not real student work and are not text to reuse. The full instructions are in [`handout/python-learning-log.pdf`](handout/python-learning-log.pdf).

The log continues across the semester and supports several later projects and assignments: some entries are turned in under one of them and some under another.

## Why this assignment
The Python Learning Log turns the skills from the course's first weeks into a habit that lasts the semester. Starting here, students complete at least four entries a week. Each entry has its own uniquely named Python file, the complete code in a LaTeX report, a screenshot showing the program ran on the student's own computer, and a paragraph on what they tried, what went wrong, and how they checked the result. The same log carries across several later projects and assignments, with entries gathered under whichever one they support. It serves the professional workflow from the first week: separate source files, a write-up that matches the code, and a reproducibility statement are the habits later projects depend on, whatever the dataset. It also serves a common starting point: entries can come from homework, guided class examples, tutorials, or independent practice, and periodic checks catch missing entries before the end of the term.

Because the practice is spread across the semester instead of concentrated at one deadline, it supports every later unit, and growth shows in commenting, testing, and independence rather than in code length. By the end, each student has a documented record of their development as a programmer that they can show employers.

## Files
| Path | Contents |
|---|---|
| `handout/` | `python-learning-log`, the assignment instructions (LaTeX source and PDF) |
| `report/template.tex` | Starting point for your log: every section it needs and a Week 1 with four entries to fill in |
| `report/fictional-sample-entries` | Four fictional completed Week 1 entries (LaTeX source and PDF), with a placeholder where each screenshot goes |
| `report/screenshot-placeholder.png` | The "YOUR screenshot here" image the sample uses |
| `src/sample_entries/` | One program for each fictional entry: temperature converter, grade classifier, average calculator, data summary |
| `src/make_screenshot_placeholder.py` | Draws the placeholder image |
| `notebooks/01-worked-example.ipynb` | Tests the four sample programs with hand-checkable and boundary values |
| `figures/` | For any figures you create; `figures/reference/` holds the expected console output of the sample programs |
| `tests/` | Checks that the sample programs reproduce the reference output, the notebook runs, and every document builds |

## Setup
With conda (recommended), in Anaconda Prompt on Windows or a terminal on Linux:
```
conda env create -f environment.yml
conda activate data200
```
If you already created the `data200` environment in an earlier unit, you can keep using it; this unit uses the same packages.

Or with pip:
```
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Check that everything works:
```
pytest
```
The LaTeX tests need `pdflatex` on your PATH and are skipped without it.

## Reproducibility
From the repository root, run the sample programs:
```
python src/sample_entries/week01_entry01_temperature_converter.py
python src/sample_entries/week01_entry02_grade_classifier.py
python src/sample_entries/week01_entry03_average_calculator.py
python src/sample_entries/week01_entry04_data_summary.py
```
With the inputs 0, 90, and 10, 20, 30, 40, 50, the output matches the `*_output.txt` files in `figures/reference/` (the values you type do not appear in those files). The programs read no files and write none, so they run from any folder.

To work through the tests cell by cell, run `jupyter lab` and open `notebooks/01-worked-example.ipynb`. To rebuild the documents, run `pdflatex` twice on each `.tex` file from inside its own folder (`handout/` or `report/`). The sample entries read their code from `src/sample_entries/`, so they always show the current programs; copied into one folder with the programs and the placeholder image, they compile there too.

## For instructors
Everything students need is open, including the four fictional sample entries, because they model the expected level of detail. The sample programs and entries are fictional, not student work. If you adapt the log, keep public examples fictional: do not publish real student names, grades, screenshots, usernames, directory paths, or submissions without permission. Grading notes are available to instructors on request. Nothing in the repository needs a network connection once the environment is installed.

## License
Code (`src/`, `notebooks/`, `tests/`): [MIT](LICENSE). Handout, report template, sample entries, placeholder image, and reference output: [CC BY-NC 4.0](LICENSE-CONTENT.md).
