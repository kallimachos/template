#!/bin/python3
# coding: utf-8
"""template test file."""

from template import template


def test_square():
    """Test square."""
    assert template.square(1) == 1
    assert template.square(2) == 4
    assert template.square(3) == 9
    assert template.square(4) == 16
    assert template.square(5) == 25


if __name__ == "__main__":
    pass
