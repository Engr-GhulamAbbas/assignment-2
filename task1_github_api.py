"""Task 1 - GitHub API

Fetch details of 3 GitHub users using the GitHub REST API, and display
each user's username and public repository count. The HTTP response
status code is verified before the data is processed.
"""

import requests

# The three GitHub users to look up.
USERS = ["torvalds", "gvanrossum", "octocat"]

API_URL = "https://api.github.com/users/{username}"


def fetch_user(username):
    """Return the GitHub API JSON for one user, or None if the request failed."""
    response = requests.get(API_URL.format(username=username), timeout=10)

    # Verify the status code before processing the data.
    if response.status_code != 200:
        print(f"[ERROR] {username}: request failed with status {response.status_code}")
        return None

    return response.json()


def main():
    print("GitHub user details")
    print("-" * 40)
    for username in USERS:
        data = fetch_user(username)
        if data is None:
            continue
        print(f"Username : {data['login']}")
        print(f"Public repositories : {data['public_repos']}")
        print("-" * 40)


if __name__ == "__main__":
    main()
