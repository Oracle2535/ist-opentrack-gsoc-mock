# Contributing

## Branch and PR rules

- Branch from `main` as `assessment/<your-student-id>`.
- Do not push directly to `main`. All submissions go through a Pull Request.
- Open one cumulative PR against `main`; keep pushing commits to it as you
  progress. The commit SHA at the cutoff time is what gets graded.

## Commits

- Make small commits with messages that describe *why*, not just *what*.
- Reference issues in commit messages (e.g. `Fix interval touching case (#102)`).

## Tests

- Run `python -m unittest discover -s tests -v` before every push.
- Add regression tests for every bug you fix. Keep tests deterministic: use
  temporary files for storage tests, never the repository's `opentrack.json`.

## PR description checklist

- [ ] Issues addressed, with links
- [ ] Root cause of each defect, in your own words
- [ ] Files/components modified
- [ ] Exact commands run and their results
- [ ] Assumptions and tradeoffs
