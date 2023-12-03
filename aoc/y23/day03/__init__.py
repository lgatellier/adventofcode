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


class Context:
    def __init__(self, lines, line_index):
        self._lines = lines
        self._line_index = line_index
        self._previous_line = self.get_previous_line()
        self._current_line = lines[line_index]
        self._next_line = self.get_next_line()

    def get_previous_line(self):
        return self._lines[self._line_index - 1] if self._line_index > 0 else None

    def get_next_line(self):
        return (
            self._lines[self._line_index + 1]
            if self._line_index < len(self._lines) - 1
            else None
        )

    @property
    def line_index(self):
        return self._line_index

    @property
    def previous_line(self):
        return self._previous_line

    @property
    def current_line(self):
        return self._current_line

    @property
    def next_line(self):
        return self._next_line
