import re

LINE_LENGTH = 140
NUMBERS_PATTERN = r'(\d+)'
SYMBOL_PATTERN = r'[^\d\.]'

def read_file(input):
    with open(input, 'r') as f:
        return [line.strip() for line in f.readlines()]

def find_all_numbers(lines):
    numbers = []
    for i in range(len(lines)):
        numbers.insert(i, [])
        for match in re.finditer(NUMBERS_PATTERN, lines[i]):
            numbers[i].append(match)
    return numbers

def has_symbol(line, start, end) -> bool:
    if re.search(SYMBOL_PATTERN, line[start:end]) is not None:
        #print(f"Found symbol in {line[start:end]}")
        return True
    #print(f"No symbol in    {line[start:end]}")
    return False

def is_part_number(line, previous_line, next_line, match) -> bool:
    safe_start = max(0, match.start() - 1)
    safe_end = min(match.end() + 1, len(line))
    #print(match)
    if previous_line and has_symbol(previous_line, safe_start, safe_end):
        return True
    elif has_symbol(line, safe_start, safe_end):
        return True
    elif next_line and has_symbol(next_line, safe_start, safe_end):
        return True
    return False

def filter_part_numbers(lines, numbers) -> list[int]:
    part_numbers = []
    for i in  range(len(numbers)):
        line = lines[i]
        part_numbers.insert(i, [])
        for match in numbers[i]:
            previous_line = lines[i - 1] if i > 0 else None
            next_line = lines[i + 1] if i < len(lines) - 1 else None
            if is_part_number(line, previous_line, next_line, match):
                part_numbers[i].append(int(match.group(0)))
    return part_numbers

def main(lines_count=None):
    input = "input"
    lines = read_file(input)

    if lines_count:
        sub_lines = lines[0:int(lines_count)]
    else:
        sub_lines = lines
    numbers = find_all_numbers(sub_lines)
    numbers_count = sum([ len(numbers) for numbers in numbers ])
    print(f"{numbers_count} numbers found in {len(sub_lines)} lines")
    part_numbers = filter_part_numbers(lines, numbers)
    print(part_numbers)
    print(sum([ sum(numbers) for numbers in part_numbers ]))

import sys
main(sys.argv[1] if len(sys.argv) > 1 else None)