from aoc.y22.day03 import Rucksack, part1, part2


from test_utils import run_main


def test_rucksack1():
    line = "vJrwpWtwJgWrhcsFMMfFFhFp"
    rucksack = Rucksack(line)
    assert rucksack.first_compartment == "vJrwpWtwJgWr"
    assert rucksack.second_compartment == "hcsFMMfFFhFp"
    for c in line:
        assert c in rucksack.unique_items


def test_common_chars():
    assert run_main(part1.main, "tests/y22/input_day03") == 7811


def test_part2_main():
    assert run_main(part2.main, "tests/y22/input_day03") == 2639
