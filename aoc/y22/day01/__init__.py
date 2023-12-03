from aoc import utils


class ElfCalories:
    def __init__(self):
        self._calories = []
        self._total = 0

    @property
    def total(self):
        return self._total

    @property
    def calories(self):
        return self._calories

    def add(self, value):
        self._calories.append(value)
        self._total += value

    def __repr__(self):
        return f"ElfCalories({self._total})"


def parse_next_elf(lines, pos):
    elf = ElfCalories()
    for line in lines[pos:]:
        pos += 1
        if line == "":
            break
        utils.verbose("Adding line: {}".format(line))
        elf.add(int(line))
    return elf, pos


def parse_elves(lines):
    elves = []
    pos = 0
    while pos < len(lines):
        utils.verbose("Parsing next elf")
        elf, pos = parse_next_elf(lines, pos)
        elves.append(elf)
    return elves


def sorted_elves_by_calories(elves, reverse=True):
    return sorted(elves, key=lambda elf: elf.total, reverse=reverse)
