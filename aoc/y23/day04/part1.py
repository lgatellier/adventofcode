from aoc import utils
from aoc.y23.day04 import Card, parse_cards


def cards_points(card: Card):
    my_winning_numbers_number = len(card.my_winning_numbers)
    return pow(2, my_winning_numbers_number - 1) if my_winning_numbers_number > 0 else 0


def main(input_file: str) -> int:
    cards = parse_cards(utils.read_file(input_file))
    return sum([cards_points(card) for card in cards])
