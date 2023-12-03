import re

from aoc.y23.day03 import part2 as puzzle


def test_find_all_symbol():
    input = "#...5..*...$../"
    matches = puzzle.find_all_symbol(input)
    assert len(matches) == 4
    assert matches[0].group(0) == "#"
    assert matches[1].group(0) == "*"
    assert matches[2].group(0) == "$"
    assert matches[3].group(0) == "/"


def test_is_adjacent():
    assert not puzzle.is_adjacent(0, re.search(r"\d+", "..123"))
    assert puzzle.is_adjacent(1, re.search(r"\d+", "..123"))
    assert puzzle.is_adjacent(2, re.search(r"\d+", "..123"))
    assert puzzle.is_adjacent(3, re.search(r"\d+", "..123"))
    assert puzzle.is_adjacent(4, re.search(r"\d+", "..123"))
    assert puzzle.is_adjacent(5, re.search(r"\d+", "..123"))
    assert not puzzle.is_adjacent(6, re.search(r"\d+", "..123"))
    assert not puzzle.is_adjacent(7, re.search(r"\d+", "..123"))
    assert not puzzle.is_adjacent(8, re.search(r"\d+", "..123"))


def test_main():
    assert puzzle.main("tests/y23/input_day03") == 73074886
