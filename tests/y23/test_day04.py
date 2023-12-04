from aoc.y23.day04 import parse_cards, part1, part2


from test_utils import run_main


def test_parse_cards_card1():
    line = "Card  1: 1 2 3 4 5 | 6 7 8 9 10"
    cards = parse_cards([line])
    assert len(cards) == 1
    assert cards[0].card_number == 1
    assert cards[0].winning_numbers == [1, 2, 3, 4, 5]
    assert cards[0].my_numbers == [6, 7, 8, 9, 10]


def test_parse_cards_card37():
    line = "Card  37: 49 37 88 55 20 95 11 86 53 18 | 53 95 18 80 25  2 88 17 11 20 22 63 45 70 55 37 86 81 28 61 47 74 49 79 48"
    cards = parse_cards([line])
    assert len(cards) == 1
    assert cards[0].card_number == 37
    assert cards[0].winning_numbers == [
        49,
        37,
        88,
        55,
        20,
        95,
        11,
        86,
        53,
        18,
    ]
    assert cards[0].my_numbers == [
        53,
        95,
        18,
        80,
        25,
        2,
        88,
        17,
        11,
        20,
        22,
        63,
        45,
        70,
        55,
        37,
        86,
        81,
        28,
        61,
        47,
        74,
        49,
        79,
        48,
    ]


def test_parse_cards_card106():
    lines = "Card 106: 71 48  3 34 73 72 85 76 69 66 | 66  7 22 76 65 25 46 69 96 34  3 35 14 45 21 23 36  5 17 60 98 71 33 93 59"
    cards = parse_cards([lines])
    assert len(cards) == 1
    assert cards[0].card_number == 106
    assert cards[0].winning_numbers == [
        71,
        48,
        3,
        34,
        73,
        72,
        85,
        76,
        69,
        66,
    ]
    assert cards[0].my_numbers == [
        66,
        7,
        22,
        76,
        65,
        25,
        46,
        69,
        96,
        34,
        3,
        35,
        14,
        45,
        21,
        23,
        36,
        5,
        17,
        60,
        98,
        71,
        33,
        93,
        59,
    ]


def test_my_winning_numbers():
    line = "Card  37: 49 37 88 55 20 95 11 86 53 18 | 53 95 18 80 25  2 88 17 11 20 22 63 45 70 55 37 86 81 28 61 47 74 49 79 48"
    cards = parse_cards([line])
    assert len(cards) == 1
    my_winning_numbers = cards[0].my_winning_numbers
    expected_winning_numbers = [95, 18, 88, 11, 20, 55, 37, 86, 49, 53]
    assert len(my_winning_numbers) == len(expected_winning_numbers)
    for i in expected_winning_numbers:
        assert i in my_winning_numbers


def test_card_points():
    line = "Card  37: 49 37 88 55 20 95 11 86 53 18 | 53 95 18 80 25  2 88 17 11 20 22 63 45 70 55 37 86 81 28 61 47 74 49 79 48"
    cards = parse_cards([line])
    assert len(cards) == 1
    assert part1.cards_points(cards[0]) == 512


def test_part1_main():
    assert run_main(part1.main, "tests/y23/input_day04") == 21558


def test_part2_main():
    assert run_main(part2.main, "tests/y23/input_day04_partial") == 15
