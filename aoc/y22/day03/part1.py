from aoc import utils
from aoc.y22.day03 import parse_rucksacks

LOWER_SUB = -96
UPPER_SUB = -38


def main(input_file="input"):
    lines = utils.read_file(input_file)
    rucksacks = parse_rucksacks(lines)
    priorities = []
    for r in rucksacks:
        if r.common_char:
            if r.common_char.isupper():
                priorities.append(ord(r.common_char) + UPPER_SUB)
            else:
                priorities.append(ord(r.common_char) + LOWER_SUB)
    print(priorities)
    print(f"Sum of priorities : {sum(priorities)}")
    return sum(priorities)
