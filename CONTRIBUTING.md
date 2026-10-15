# Contributing

## Fork, branch, and PR rules

- You have read-only access here. **Fork this repository** and do all work in
  your fork.
- In your fork, branch from `main` as `assessment/<your-student-id>`.
- Never commit directly to `main`, even in your fork. All work goes through
  a Pull Request.
- Open **one cumulative PR inside your fork** (base: your fork's `main`,
  compare: your assessment branch) — not against the upstream repository.
  Keep pushing commits to it as you progress. The commit SHA on your PR
  branch at the cutoff time is what gets graded.
- Add `hshar-intellipaat` as a collaborator on your fork, and submit your
  fork URL + PR URL via the submission form by 9:30 AM:
  <https://forms.gle/c3xazJkKpRqu9Hwt8>

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
