from aoc.y23.day03 import (
    filter_part_numbers,
    find_all_numbers,
)


def main(lines: list[str]):
    numbers = find_all_numbers(lines)
    numbers_count = sum([len(numbers) for numbers in numbers])
    print(f"{numbers_count} numbers found in {len(lines)} lines")
    part_numbers = filter_part_numbers(lines, numbers)
    int_part_numbers = [
        [int(match.group(0)) for match in line] for line in part_numbers
    ]
    part_numbers_sum = sum([sum(numbers) for numbers in int_part_numbers])
    return part_numbers_sum
