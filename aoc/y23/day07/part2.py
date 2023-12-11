from aoc.y23.day07 import CARD_NUMERIC_VALUES, parse_hand


def main(lines: list[str]):
    # Set J the weakest card
    CARD_NUMERIC_VALUES["J"] = 1
    hands = [parse_hand(line, True) for line in lines]
    sorted_hands = sorted(hands)
    winnings = [sorted_hands[i].winnings(i + 1) for i in range(len(sorted_hands))]
    print(sum(winnings))
