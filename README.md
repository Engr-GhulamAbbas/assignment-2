# Assignment 2

Three independent tasks.

## Task 1 — GitHub API (`task1_github_api.py`)
Fetches 3 GitHub users via the GitHub REST API and prints each user's
username and public repository count. The response status code is
verified (must be 200) before the data is processed.

```bash
pip install requests
python task1_github_api.py
```

## Task 2 — SQL / Library Database (`library.sql`)
Creates a `books` table, inserts 8 records, then filters books priced
above 500, sorts by price, counts the records, and updates a book's
price using `WHERE`.

```bash
sqlite3 library.db < library.sql
```

## Task 3 — Pytest (`is_adult.py`, `test_is_adult.py`)
`is_adult(age)` returns `True` for age ≥ 18, `False` otherwise, and
raises `ValueError` for a negative age. Tests cover ages 17, 18 and -1.

```bash
pip install pytest
pytest -v
```
