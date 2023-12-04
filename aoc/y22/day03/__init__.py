class Rucksack:
    def __init__(self, line: str):
        middle = len(line) // 2
        self.first_compartment = line[0:middle]
        self.second_compartment = line[middle : len(line)]
        self.unique_items: set[str] = set(line)

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


# a=97 in ASCII but 1 in this puzzle
LOWER_SUB = 96
# A=65 in ASCII but 27 in this puzzle
UPPER_SUB = 38


def get_priority(char: str):
    if len(char) != 1:
        raise ValueError("get_priority takes a single char as argument")
    elif char.isupper():
        return ord(char) - UPPER_SUB
    else:
        return ord(char) - LOWER_SUB
