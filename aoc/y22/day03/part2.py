from aoc import utils
from aoc.y22.day03 import get_priority, parse_rucksacks, Rucksack


class Group:
    def __init__(self):
        self.rucksacks: list[Rucksack] = []

    def append_rucksack(self, rucksack: Rucksack):
        if len(self.rucksacks) == 3:
            raise RuntimeError("An elves group cannot contain more than 3 elves")

        self.rucksacks.append(rucksack)
        if len(self.rucksacks) == 3:
            common_items = self.rucksacks[0].unique_items.intersection(
                self.rucksacks[1].unique_items, self.rucksacks[2].unique_items
            )
            if len(common_items) > 1:
                raise RuntimeError("An elves group must have a single badge !")
            self.badge = common_items.pop()
            utils.verbose("Group's badge is '{badge}'", badge=self.badge)


def main(input_file="input"):
    lines = utils.read_file(input_file)
    groups: list[Group] = []
    current_group: Group = None
    rucksacks = parse_rucksacks(lines)
    priorities_sum = 0
    for i in range(len(rucksacks)):
        if i % 3 == 0:
            if i > 0:
                priorities_sum += get_priority(current_group.badge)
            utils.verbose("i={i}, starting new group", i=i)
            current_group = Group()
            groups.append(current_group)
        utils.verbose("Adding elf {i} to group {group}", i=i, group=len(groups) - 1)
        current_group.append_rucksack(rucksacks[i])
    priorities_sum += get_priority(current_group.badge)
    print(f"Found {len(groups)} groups of elves")
    print(f"Sum of all groups badges priorities is {priorities_sum}")
    return priorities_sum
