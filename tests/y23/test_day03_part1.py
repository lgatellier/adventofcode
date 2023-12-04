from aoc.y23.day03 import part1 as puzzle


from test_utils import run_main


def test_main():
    assert run_main(puzzle.main, "tests/y23/input_day03") == 527369
