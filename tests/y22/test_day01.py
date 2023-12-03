from aoc.y22.day01 import part1 as puzzle


def test_parse_next_elf():
    lines = ["1", "2", "3", "4", "5", ""]
    elf, pos = puzzle.parse_next_elf(lines, 0)
    assert elf.total == 15
    assert pos == 6


def test_parse_elves():
    lines = ["1", "2", "3", "4", "5", "", "6", "7", "8", "9", ""]
    elves = puzzle.parse_elves(lines)
    assert len(elves) == 2
    assert elves[0].total == 15
    assert elves[1].total == 30


def test_main():
    assert puzzle.main("tests/y22/input_day01").total == 73211
