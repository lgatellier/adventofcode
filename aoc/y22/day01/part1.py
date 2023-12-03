from aoc import utils
from aoc.y22.day01 import parse_elves, sorted_elves_by_calories


def main(input_file="input"):
    lines = utils.read_file(input_file)

    elves = parse_elves(lines)
    sorted_elves = sorted_elves_by_calories(elves)

    max_calories_elf = sorted_elves[0]
    print(f"Elf carrying the most calories : {max_calories_elf}")
    return max_calories_elf


if __name__ == "__main__":
    utils.main(main)
