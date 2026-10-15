# OpenTrack

OpenTrack is a small command-line issue tracker written in Python (standard
library only). It is partially implemented: creating, fetching, and listing
issues works in common cases. Other behaviors are incomplete or buggy — see
the GitHub issues in your repository for what to investigate.

## Requirements

- Python 3.10 or newer. No third-party packages.

## Run from a fresh clone

```bash
# create an issue
python -m src.main create --title "Fix login flow" --priority high

# show it
python -m src.main get 1

# list all issues
python -m src.main list

# partially update
python -m src.main update 1 --status in_progress

# delete
python -m src.main delete 1

# rank open issues for triage (high first, then medium, then low)
python -m src.main triage --limit 5

# show an issue's reference hint (index of first unique character in its title)
python -m src.main ref 1

# consolidate maintenance windows (inclusive start:end intervals)
python -m src.main windows 1:3 2:5 8:9
```

Data is stored in `opentrack.json` in the working directory (override with
`--db path`).

## Run the starter tests

```bash
python -m unittest discover -s tests -v
```

All starter tests pass on a fresh clone. They cover only baseline behavior —
you are expected to add your own tests as you fix issues.

## Project layout

| Path | Purpose |
| --- | --- |
| `src/main.py` | CLI entry point |
| `src/issue_service.py` | Core issue operations |
| `src/storage.py` | JSON persistence |
| `src/validators.py` | Input validation rules |
| `src/algorithms.py` | Utility algorithms backing the `ref` and `windows` commands |
| `src/ranking.py` | Open-issue ranking backing the `triage` command |
| `tests/` | Public starter tests |

## Assessment workflow

You have **read-only** access to this repository. All work happens in your own
private fork:

1. Read the issues in this repository.
2. **Fork** this repository using the Fork button (your fork stays private).
3. Clone **your fork** and create a branch named `assessment/<your-student-id>`.
4. Commit in small, well-described steps and push to your fork.
5. Open **one cumulative Pull Request inside your fork**: base = your fork's
   `main`, compare = your `assessment/<your-student-id>` branch. Do **not**
   open a PR against this upstream repository.
6. Add **`hshar-intellipaat`** as a collaborator on your fork
   (your fork → Settings → Collaborators → Add people), so instructors can
   review your work.
7. Submit your fork URL and PR URL in this form **by 9:30 AM**:
   <https://forms.gle/c3xazJkKpRqu9Hwt8>
   (Open the PR early — keep pushing commits to it as you progress.)

Your PR description must include: linked issues, root causes found,
components changed, commands/tests run with results, and assumptions.
The last commit on your PR branch **before 12:00 PM IST** is what gets graded.
Do not delete or force-push your fork after the cutoff.

AI-generated solutions and collaboration are prohibited for this assessment.
Shortlisted students will be asked to explain and modify their own code in a
short supervised follow-up session.
