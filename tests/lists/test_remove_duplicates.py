import pytest
from lists.remove_duplicates import remove_duplicates


def test_remove_duplicates():
    input_nums = [0, 0, 1, 1, 1, 1, 2, 3, 3, ]
    output_nums = [0, 0, 1, 1, 2, 3, 3, ]

    k, result_nums = remove_duplicates(input_nums)
    assert k, 7
    assert result_nums, output_nums


def test_remove_duplicates_for_small_list():
    input_nums = [0, 0, 0, ]
    output_nums = [0, 0, ]

    k, result_nums = remove_duplicates(input_nums)
    assert k, 2
    assert result_nums, output_nums
