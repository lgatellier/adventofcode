import re

from aoc import utils

LINE_LENGTH = 140
NUMBERS_PATTERN = r"(\d+)"
SYMBOL_PATTERN = r"[^\d\.]"


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


def is_part_number(ctx: Context, match) -> bool:
    safe_start = max(0, match.start() - 1)
    safe_end = min(match.end() + 1, len(ctx.current_line))
    if ctx.previous_line and has_symbol(ctx.previous_line, safe_start, safe_end):
        return True
    elif has_symbol(ctx.current_line, safe_start, safe_end):
        return True
    elif ctx.next_line and has_symbol(ctx.next_line, safe_start, safe_end):
        return True
    return False


def filter_part_numbers(lines, numbers) -> list[int]:
    part_numbers = []
    for i in range(len(numbers)):
        ctx = Context(lines, i)
        part_numbers.insert(i, [])
        for match in numbers[i]:
            if is_part_number(ctx, match):
                utils.verbose(
                    " Line {line_number} - Part number found : {num}",
                    line_number=i,
                    num=match.group(0),
                )
                part_numbers[i].append(match)
    return part_numbers
