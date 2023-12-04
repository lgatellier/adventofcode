from aoc import utils
from aoc.y22.day03 import parse_rucksacks


def main(lines: list[str]):
    rucksacks = parse_rucksacks(lines)
    utils.verbose("Found {n} rucksacks", n=len(rucksacks))
    priorities = [r.priority for r in rucksacks if r.priority]
    utils.verbose("Priorities are {p}", p=priorities)
    print(f"Sum of priorities : {sum(priorities)}")
    return sum(priorities)
