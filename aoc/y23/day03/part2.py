import re

from aoc import utils
from aoc.y23.day03 import (
    Context,
    filter_part_numbers,
    find_all_numbers,
    SYMBOL_PATTERN,
)


def find_all_symbol(line):
    return [match for match in re.finditer(SYMBOL_PATTERN, line)]


def is_adjacent(symbol_pos, match) -> bool:
    return symbol_pos >= (match.start() - 1) and symbol_pos <= match.end()


def find_all_adjacent_part_numbers(ctx: Context, symbol_match):
    adjacent_lines = ctx.previous_line + ctx.current_line + ctx.next_line
    return [
        match for match in adjacent_lines if is_adjacent(symbol_match.start(), match)
    ]


def is_gear_symbol(ctx: Context, symbol_match) -> bool:
    adjacent_part_numbers = find_all_adjacent_part_numbers(ctx, symbol_match)
    if len(adjacent_part_numbers) == 2:
        first_number = int(adjacent_part_numbers[0].group(0))
        second_number = int(adjacent_part_numbers[1].group(0))
        return True, first_number * second_number
    return False, None


def main(input="input"):
    lines = utils.read_file(input)
    part_numbers = filter_part_numbers(lines, find_all_numbers(lines))
    symbols = [find_all_symbol(line) for line in lines]

    gear_ratios = []
    for i in range(len(lines)):
        ctx = Context(part_numbers, i)
        line_gears = [is_gear_symbol(ctx, match) for match in symbols[i]]
        gear_ratios.insert(i, [ratio for is_gear, ratio in line_gears if is_gear])

    sum_gear_ratios = sum([sum(ratios) for ratios in gear_ratios])
    return sum_gear_ratios


if __name__ == "__main__":
    import sys
    import time

    start1 = time.time()
    sum_gear_ratios = main(sys.argv[1] if len(sys.argv) > 1 else None)
    end1 = time.time()
    print(f"sum is {sum_gear_ratios} ({end1 - start1} seconds) ")
