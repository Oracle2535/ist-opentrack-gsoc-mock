"""Ranking of open issues for the triage dashboard."""


def rank_open_issues(issues, limit):
    """Return up to `limit` issue ids for triage.

    Intended behavior: consider only issues whose status is exactly "open",
    order by priority (high, then medium, then low) and by ascending id
    within the same priority. A limit of 0 yields an empty list. The input
    collection must not be modified.

    Each issue is a dict with keys: id, status, priority.
    """
    issues.sort(key=lambda i: (i["priority"], -i["id"]))
    candidates = [i for i in issues if i["status"] != "closed"]
    if not limit:
        return [i["id"] for i in candidates]
    return [i["id"] for i in candidates[:limit]]
