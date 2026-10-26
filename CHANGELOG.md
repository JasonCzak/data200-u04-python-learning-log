# Changelog

Each entry records what changed for a semester, newest first.

## Fall 2026: repository conversion

### Structure
- Standard DATA 200 layout: `notebooks/`, `src/`, `report/`, `figures/reference/`, `handout/`, `tests/`, plus `CITATION.cff`, `environment.yml`, and `pytest.ini`.
- No `data/` folder: the only data in this unit is the short list inside the fourth sample program, so there is nothing to keep raw or processed. No `slides/`: the unit has no presentation.
- Renamed for portability and clarity: `assignment/python_learning_progress_log_template.tex` became `report/template.tex`; `example/fictional_sample_log_entries.tex` became `report/fictional-sample-entries.tex`; `example/code/` became `src/sample_entries/`.
- Removed: `CONTRIBUTING.md` (not part of the course's repository layout), a file list, a compiled test cache, and the empty `example/screenshots/` folder.
- Licenses: `LICENSE` (MIT, code) and `LICENSE-CONTENT.md` (CC BY-NC 4.0: handout, report template, sample entries, placeholder image, reference output).

### Handout
- New `handout/python-learning-log.tex` gathers the instructions that were spread across the template, the README, and a submission checklist: what each entry includes, what can count as an entry, screenshots, AI use, setup, the fictional sample, how to check your work, the assessment criteria, and submission.
- Screenshots must show the program running on the student's own computer.
- One paragraph explains that the log continues all semester and that its entries are turned in under several later projects and assignments.
- Setup covers conda and pip on Windows and Linux and points students who cannot install software to the course's approved alternative. One line says students may keep their work in their own Git repository and publish it on GitHub if they choose.

### Report template
- Fixed two compile errors: the accessibility metadata block needs a newer LaTeX than many installations have, and the screenshot placeholder printed file names with unescaped underscores, so the template could not compile until every screenshot existed. It now compiles with `pdflatex` from the first day; the PDF title metadata and image alt text are kept.
- The placeholder box reads "YOUR screenshot here". The semester and submission date are fill-in fields rather than preset values.
- The AI-use section explains that a later part of the course covers generative AI; entries before then are written without AI tools, and any later use is documented.
- The submission checklist adds how each program was tested, file names that match the submitted files, and no private usernames, passwords, or tokens.
- Fixed header-height, list-width, and font warnings.

### Fictional sample entries
- Each entry now shows a "YOUR screenshot here" image where the run screenshot goes, drawn by `src/make_screenshot_placeholder.py`.
- Each sample program says in its docstring that it is a fictional sample, not real student work. The sample's listings read the programs from `src/sample_entries/`, or from the same folder when the files are copied together.
- Titled "DATA 200: Python Learning Log"; fixed a header-height warning.

### Code and tests
- `notebooks/01-worked-example.ipynb`, outputs cleared, tests the four sample programs with hand-checkable and boundary values.
- `figures/reference/` holds each sample program's expected console output.
- `tests/` (pytest, replacing the unittest smoke tests): each sample program matches its reference output, runs from any folder, and confirms the run results its entry reports; the placeholder image is reproduced; the notebook runs; every `.tex` compiles without warnings (skipped if `pdflatex` is missing), and the sample also compiles from a flat folder. All offline.
- Environment: the shared `data200` environment, pinned the same as the previous unit, with no additions: Python 3.12, NumPy 2.5.4, pandas 3.1.0, Matplotlib 3.11.2, JupyterLab 4.6.4, ipykernel 7.4.0, nbclient 0.11.0, nbformat 5.11.1, pytest 9.1.1. `pytest.ini` treats warnings as errors.
