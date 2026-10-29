# aa-job-application

An Agile Alps job application studio for Claude. It tailors a CV and cover letter to a job description with truthful, ATS-aware wording, keeps the candidate's original design, researches the company problem, and prepares interview practice.

## What it does

- Tailors a CV and cover letter to a job description, without adding claims the source CV does not support.
- Keeps the candidate's original design (fonts, sizes, colours, page size).
- Researches the company and the problem the role solves.
- Prepares interview practice and suggests similar roles.

## Contents

- `SKILL.md`: the skill instructions that Claude follows.
- `scripts/extract_design.py`: prints a style sheet (fonts, sizes, colours, page size) from a source PDF or DOCX. Python 3 standard library only.

## Usage

Use the skill when you share a CV and a job description, or ask for an application, cover letter, CV tailoring or interview preparation.

Read the style sheet of a source CV:

```sh
python3 scripts/extract_design.py path/to/cv.pdf
python3 scripts/extract_design.py path/to/cv.docx
```

## Privacy

Candidate data stays out of this repository. Keep CVs, generated documents and profiles in `cvs/` and `output/` on your own machine. Both folders are listed in `.gitignore`.

## Licence

MIT. See [LICENSE](LICENSE).
