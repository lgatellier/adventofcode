from __future__ import annotations


class PairOfElves:
    def __init__(self, first: tuple[int], second: tuple[int]):
        self.first = first
        self.second = second
        self.fully_overlap = (first[0] <= second[0] and first[1] >= second[1]) or (
            second[0] <= first[0] and second[1] >= first[1]
        )

    @staticmethod
    def parse(line: str) -> PairOfElves:
        split = line.split(",")
        first_elf = split[0].split("-")
        second_elf = split[1].split("-")
        return PairOfElves(
            (int(first_elf[0]), int(first_elf[1])),
            (int(second_elf[0]), int(second_elf[1])),
        )
