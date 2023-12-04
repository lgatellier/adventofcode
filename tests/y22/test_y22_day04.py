from aoc.y22.day04 import PairOfElves, part1, part2


from test_utils import run_main


def test_pairofelves_1():
    pair: PairOfElves = PairOfElves.parse("1-2,3-4")
    assert pair.first[0] == 1
    assert pair.first[1] == 2
    assert pair.second[0] == 3
    assert pair.second[1] == 4
    assert not pair.fully_overlap
    assert not pair.partially_overlap


def test_pairofelves_2():
    pair: PairOfElves = PairOfElves.parse("5-8,2-7")
    assert pair.first[0] == 5
    assert pair.first[1] == 8
    assert pair.second[0] == 2
    assert pair.second[1] == 7
    assert not pair.fully_overlap
    assert pair.partially_overlap


def test_pairofelves_full_overlap_forward():
    pair: PairOfElves = PairOfElves.parse("2-9,3-8")
    assert pair.first[0] == 2
    assert pair.first[1] == 9
    assert pair.second[0] == 3
    assert pair.second[1] == 8
    assert pair.fully_overlap
    assert pair.partially_overlap


def test_pairofelves_full_overlap_reverse():
    pair: PairOfElves = PairOfElves.parse("3-8,2-9")
    assert pair.first[0] == 3
    assert pair.first[1] == 8
    assert pair.second[0] == 2
    assert pair.second[1] == 9
    assert pair.fully_overlap
    assert pair.partially_overlap


def test_partial_overlap():
    pair: PairOfElves = PairOfElves.parse("2-7,5-8")
    assert pair.first[0] == 2
    assert pair.first[1] == 7
    assert pair.second[0] == 5
    assert pair.second[1] == 8
    assert not pair.fully_overlap
    assert pair.partially_overlap


def test_partial_overlap_one_forward():
    pair: PairOfElves = PairOfElves.parse("2-5,5-8")
    assert pair.first[0] == 2
    assert pair.first[1] == 5
    assert pair.second[0] == 5
    assert pair.second[1] == 8
    assert not pair.fully_overlap
    assert pair.partially_overlap


def test_partial_overlap_one_reverse():
    pair: PairOfElves = PairOfElves.parse("5-8,2-5")
    assert pair.first[0] == 5
    assert pair.first[1] == 8
    assert pair.second[0] == 2
    assert pair.second[1] == 5
    assert not pair.fully_overlap
    assert pair.partially_overlap


def test_part1_main():
    assert run_main(part1.main, "tests/y22/input_day04") == 518


def test_part2_main():
    assert run_main(part2.main, "tests/y22/input_day04") == 909
