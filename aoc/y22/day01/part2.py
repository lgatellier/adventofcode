from aoc import utils
from aoc.y22.day01 import parse_elves, sorted_elves_by_calories


def main(lines: list[str]):
    elves = parse_elves(lines)
    sorted_elves = sorted_elves_by_calories(elves)

    top_three_elves = sorted_elves[:3]
    print(f"Top three elves : {top_three_elves}")
    sum_top_three_calories = sum(e.total for e in top_three_elves)
    print(f"Sum of calories of top three elves : {sum_top_three_calories}")
    return sum_top_three_calories


if __name__ == "__main__":
    utils.main(main)
