from aoc.y22.day02 import part1, part2


from test_utils import run_main


def test_part1_main():
    assert run_main(part1.main, "tests/y22/input_day02") == 9651


def test_part2_main():
    assert run_main(part2.main, "tests/y22/input_day02") == 10560
