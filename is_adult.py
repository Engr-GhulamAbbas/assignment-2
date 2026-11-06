"""Task 3 - Pytest

The is_adult(age) function returns True when the age is 18 or above,
and False otherwise. A negative age is invalid and raises a ValueError.
"""


def is_adult(age):
    """Return True if age >= 18. Raise ValueError for a negative age."""
    if age < 0:
        raise ValueError("age cannot be negative")
    return age >= 18
