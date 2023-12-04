from aoc.y22.day01 import parse_elves, sorted_elves_by_calories


def main(lines: list[str]):
    elves = parse_elves(lines)
    sorted_elves = sorted_elves_by_calories(elves)

    max_calories_elf = sorted_elves[0]
    print(f"Elf carrying the most calories : {max_calories_elf}")
    return max_calories_elf
