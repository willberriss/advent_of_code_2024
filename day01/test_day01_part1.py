# import pytest

from day01_part1 import day01_part1


def test_when_using_sample_input_data_result_is_11():
    filename = "sample_input_data.txt"
    result = day01_part1(filename)
    assert result == 11

def test_when_using_input_data_result_is_1666427():
    filename = "input_data.txt"
    result = day01_part1(filename)
    assert result == 1666427

