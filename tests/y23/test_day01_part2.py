from aoc.y23.day01 import part2 as puzzle


from test_utils import run_main


def test_main():
    assert run_main(puzzle.main, "tests/y23/input_day01") == 54530
