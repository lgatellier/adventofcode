from aoc import utils
from aoc.y23.day06 import (
    Race,
    parse_races,
    parse_records,
    parse_times,
    part1,
    part2,
)

from test_utils import run_main


def test_ways_to_win1():
    utils.state["verbose"] = True
    assert Race(7, 9).number_of_ways_to_win() == 4


def test_ways_to_win2():
    utils.state["verbose"] = True
    assert Race(15, 40).number_of_ways_to_win() == 8


def test_ways_to_win3():
    utils.state["verbose"] = True
    assert Race(30, 200).number_of_ways_to_win() == 9


def test_parse_records():
    records = parse_records("Distance:   213   1168   1086   1248")
    assert len(records) == 4
    assert records[0] == 213
    assert records[1] == 1168
    assert records[2] == 1086
    assert records[3] == 1248


def test_parse_records_joint():
    records = parse_records("Distance:   213   1168   1086   1248", joint=True)
    assert len(records) == 1
    assert records[0] == 213116810861248


def test_parse_times():
    times = parse_times("Time:        35     69     68     87")
    assert len(times) == 4
    assert times[0] == 35
    assert times[1] == 69
    assert times[2] == 68
    assert times[3] == 87


def test_parse_times_joint():
    times = parse_times("Time:        35     69     68     87", joint=True)
    assert len(times) == 1
    assert times[0] == 35696887


def test_parse_races():
    times = [7, 15, 30]
    records = [9, 40, 200]
    races = parse_races(times, records)
    assert len(races) == 3
    assert races[0].duration == 7
    assert races[0].record == 9
    assert races[1].duration == 15
    assert races[1].record == 40
    assert races[2].duration == 30
    assert races[2].record == 200


def test_part1_main():
    assert run_main(part1.main, "tests/y23/input_day06") == 170000


def test_part2_main():
    assert run_main(part2.main, "tests/y23/input_day06") == 20537782
