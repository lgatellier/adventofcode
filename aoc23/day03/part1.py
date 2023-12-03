import re

from aoc23.utils import read_file

LINE_LENGTH = 140
NUMBERS_PATTERN = r"(\d+)"
SYMBOL_PATTERN = r"[^\d\.]"


def find_numbers(line):
    return [match for match in re.finditer(NUMBERS_PATTERN, line)]


def find_all_numbers(lines):
    numbers = []
    for i in range(len(lines)):
        numbers.insert(i, find_numbers(lines[i]))
    return numbers


def has_symbol(line, start, end) -> bool:
    if re.search(SYMBOL_PATTERN, line[start:end]):
        return True
    return False


def is_part_number(line, previous_line, next_line, match) -> bool:
    safe_start = max(0, match.start() - 1)
    safe_end = min(match.end() + 1, len(line))
    if previous_line and has_symbol(previous_line, safe_start, safe_end):
        return True
    elif has_symbol(line, safe_start, safe_end):
        return True
    elif next_line and has_symbol(next_line, safe_start, safe_end):
        return True
    return False


def filter_part_numbers(lines, numbers) -> list[int]:
    part_numbers = []
    for i in range(len(numbers)):
        line = lines[i]
        part_numbers.insert(i, [])
        for match in numbers[i]:
            previous_line = lines[i - 1] if i > 0 else None
            next_line = lines[i + 1] if i < len(lines) - 1 else None
            if is_part_number(line, previous_line, next_line, match):
                part_numbers[i].append(match)
    return part_numbers


def main(input="input", lines_count=None):
    lines = read_file(input)

    sub_lines = lines[0 : int(lines_count)] if lines_count else lines
    numbers = find_all_numbers(sub_lines)
    numbers_count = sum([len(numbers) for numbers in numbers])
    print(f"{numbers_count} numbers found in {len(sub_lines)} lines")
    part_numbers = filter_part_numbers(lines, numbers)
    int_part_numbers = [[int(match.group(0)) for match in line] for line in part_numbers]
    part_numbers_sum = sum([sum(numbers) for numbers in int_part_numbers])
    return part_numbers_sum


if __name__ == "__main__":
    import sys

    sum_part_numbers = main(
        sys.argv[1] if len(sys.argv) > 1 else None,
        sys.argv[2] if len(sys.argv) > 2 else None,
    )
    print(f"Sum is {sum_part_numbers}")
