from aoc.y22.day03 import Rucksack, part1


def test_rucksack1():
    line = "vJrwpWtwJgWrhcsFMMfFFhFp"
    rucksack = Rucksack(line)
    assert rucksack.first_compartment == "vJrwpWtwJgWr"
    assert rucksack.second_compartment == "hcsFMMfFFhFp"


def test_common_chars():
    assert part1.main("tests/y22/input_day03") == 7811
