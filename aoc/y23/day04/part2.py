from aoc import utils
from aoc.y23.day04 import Card, parse_cards


def win_additional_cards(cards: list[Card], index: int):
    card = cards[index]
    print(f"process card {card.card_number}")
    if len(card.my_winning_numbers) > 0:
        for i in range(1, len(card.my_winning_numbers) + 1):
            if index + i < len(cards):
                cards[index + i].increment_count(card.count)


def main(input_file: str):
    cards = parse_cards(utils.read_file(input_file))
    total_cards = 0
    for i in range(len(cards)):
        win_additional_cards(cards, i)
        total_cards += cards[i].count
    print(f"You end with {total_cards} cards")
    return total_cards
