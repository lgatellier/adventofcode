import re

from aoc23.utils import read_file
from aoc23.day03 import (
    filter_part_numbers,
    find_all_numbers,
    find_numbers,
    has_symbol,
    is_part_number,
    SYMBOL_PATTERN,
)


def find_all_symbol(line):
    return [match for match in re.finditer(SYMBOL_PATTERN, line)]


def is_adjacent(symbol_pos, match) -> bool:
    return symbol_pos >= (match.start() - 1) and symbol_pos <= match.end()


def find_all_adjacent_part_numbers(line, previous_line, next_line, symbol_match):
    adjacent_part_numbers = []
    for match in previous_line + line + next_line:
        if is_adjacent(symbol_match.start(), match):
            adjacent_part_numbers.append(match)
    return adjacent_part_numbers


def is_gear_symbol(line, previous_line, next_line, symbol_match) -> bool:
    adjacent_part_numbers = find_all_adjacent_part_numbers(
        line, previous_line, next_line, symbol_match
    )
    if len(adjacent_part_numbers) == 2:
        first_number = int(adjacent_part_numbers[0].group(0))
        second_number = int(adjacent_part_numbers[1].group(0))
        return True, first_number, second_number
    return False, None, None


def compute_symbol_ratio(line, previous_line, next_line, symbol_match):
    is_gear, first_number, second_number = is_gear_symbol(
        line, previous_line, next_line, symbol_match
    )
    if is_gear:
        return first_number * second_number
    return None


def main(input="input"):
    lines = read_file(input)
    part_numbers = filter_part_numbers(lines, find_all_numbers(lines))
    symbols = [find_all_symbol(line) for line in lines]

    gear_ratios = []
    for i in range(len(lines)):
        previous_line = part_numbers[i - 1] if i > 0 else None
        line = part_numbers[i]
        next_line = part_numbers[i + 1] if i < len(part_numbers) - 1 else None
        gear_ratios.insert(i, [])
        for match in symbols[i]:
            symbol_ratio = compute_symbol_ratio(line, previous_line, next_line, match)
            if symbol_ratio:
                gear_ratios[i].append(symbol_ratio)

    print(gear_ratios)
    sum_gear_ratios = sum([sum(ratios) for ratios in gear_ratios])
    return sum_gear_ratios


if __name__ == "__main__":
    import sys

    sum_gear_ratios = main(sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"sum is {sum_gear_ratios}")
