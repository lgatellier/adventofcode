import re

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