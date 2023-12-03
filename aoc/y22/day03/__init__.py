class Rucksack:
    def __init__(self, line: str):
        middle = len(line) // 2
        self.first_compartment = line[0:middle]
        self.second_compartment = line[middle : len(line)]

    @property
    def common_char(self) -> str:
        for c in self.first_compartment:
            if c in self.second_compartment:
                return c
        return None

    def __repr__(self) -> str:
        return f"{self.first_compartment} | {self.second_compartment}"


def parse_rucksacks(lines: list[str]) -> list[Rucksack]:
    return [Rucksack(line) for line in lines]
