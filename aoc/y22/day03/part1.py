from aoc import utils
from aoc.y22.day03 import parse_rucksacks


def main(input_file="input"):
    lines = utils.read_file(input_file)
    rucksacks = parse_rucksacks(lines)
    utils.verbose("Found {n} rucksacks", n=len(rucksacks))
    priorities = [r.priority for r in rucksacks if r.priority]
    utils.verbose("Priorities are {p}", p=priorities)
    print(f"Sum of priorities : {sum(priorities)}")
    return sum(priorities)
