"""Tests for statistics functions within the Model layer."""

import numpy as np
import numpy.testing as npt
import pytest

@pytest.mark.parametrize(
    "test, expected",
    [
        ([ [0, 0], [0, 0], [0, 0] ], [0, 0]),
        ([ [1, 2], [3, 4], [5, 6] ], [3, 4]),
    ])
def test_daily_mean(test, expected):
    """Test mean function works for array of zeroes and positive integers."""
    from inflammation.models import daily_mean
    npt.assert_array_equal(daily_mean(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
            ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [4, 6, 9]),
            ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [4, -1, 9]),
        ])
def test_daily_max(test, expected):
    """Test that max function works for zeros and positive or negative integers."""
    from inflammation.models import daily_max
    npt.assert_array_equal(daily_max(np.array(test)), np.array(expected))

@pytest.mark.parametrize(
        "test, expected",
        [
            ([ [0, 0, 0], [0, 0, 0], [0, 0, 0] ], [0, 0, 0]),
            ([ [4, 2, 5], [1, 6, 2], [4, 1, 9] ], [1, 1, 2]),
            ([ [4, -2, 5], [1, -6, 2], [-4, -1, 9] ], [-4, -6, 2]),
        ])
def test_daily_min(test, expected):
    """Test that min function works for an array of zeros and positive or negative integers."""
    from inflammation.models import daily_min
    npt.assert_array_equal(daily_min(np.array(test)), expected)

...
def test_daily_min_string():
    """Test for TypeError when passing strings"""
    from inflammation.models import daily_min

    with pytest.raises(TypeError):
        error_expected = daily_min([['Hello', 'there'], ['General', 'Kenobi']])

@pytest.mark.parametrize(
    "test, expected, expect_raises",
    [
        # previous test cases here, with None for expect_raises, except for the next one - add ValueError
        # as an expected exception (since it has a negative input value)
        (
            [[-1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            ValueError,
        ),
        (
            [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[0.33, 0.67, 1], [0.67, 0.83, 1], [0.78, 0.89, 1]],
            None,
        ),
    ])
def test_patient_normalise(test, expected, expect_raises):
    """Test normalisation works for arrays of one and positive integers."""
    from inflammation.models import patient_normalise
    if expect_raises is not None:
        with pytest.raises(expect_raises):
            npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
    else:
        npt.assert_almost_equal(patient_normalise(np.array(test)), np.array(expected), decimal=2)
