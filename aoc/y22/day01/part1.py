from aoc import utils
from aoc.y22.day01 import ElfCalories


def parse_next_elf(lines, pos):
    elf = ElfCalories()
    for line in lines[pos:]:
        pos += 1
        if line == "":
            break
        utils.verbose("Adding line: {}".format(line))
        elf.add(int(line))
    return elf, pos


def parse_elves(lines):
    elves = []
    pos = 0
    while pos < len(lines):
        utils.verbose("Parsing next elf")
        elf, pos = parse_next_elf(lines, pos)
        elves.append(elf)
    return elves


def sorted_elves_by_calories(elves, reverse=True):
    return sorted(elves, key=lambda elf: elf.total, reverse=reverse)


def main(input_file="input"):
    lines = utils.read_file(input_file)

    elves = parse_elves(lines)
    sorted_elves = sorted_elves_by_calories(elves)

    max_calories_elf = sorted_elves[0]
    print(f"Elf carrying the most calories : {max_calories_elf}")
    return max_calories_elf


if __name__ == "__main__":
    import sys

    print(main(sys.argv[1] if len(sys.argv) > 1 else None))
