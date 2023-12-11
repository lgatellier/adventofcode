from aoc.y23.day07 import parse_hand


def main(lines: list[str]):
    hands = [parse_hand(line) for line in lines]
    sorted_hands = sorted(hands)
    winnings = [sorted_hands[i].winnings(i + 1) for i in range(len(sorted_hands))]
    print(sum(winnings))
