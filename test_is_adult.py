"""Tests for the is_adult function (Task 3)."""

import pytest

from is_adult import is_adult


def test_age_17_is_not_adult():
    assert is_adult(17) is False


def test_age_18_is_adult():
    assert is_adult(18) is True


def test_negative_age_raises_value_error():
    with pytest.raises(ValueError):
        is_adult(-1)
