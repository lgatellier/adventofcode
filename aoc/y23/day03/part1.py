from aoc.utils import read_file
from aoc.y23.day03 import (
    filter_part_numbers,
    find_all_numbers,
)


def main(input_file="input", lines_count=None):
    lines = read_file(input_file)

    sub_lines = lines[0 : int(lines_count)] if lines_count else lines
    numbers = find_all_numbers(sub_lines)
    numbers_count = sum([len(numbers) for numbers in numbers])
    print(f"{numbers_count} numbers found in {len(sub_lines)} lines")
    part_numbers = filter_part_numbers(lines, numbers)
    int_part_numbers = [
        [int(match.group(0)) for match in line] for line in part_numbers
    ]
    part_numbers_sum = sum([sum(numbers) for numbers in int_part_numbers])
    return part_numbers_sum


if __name__ == "__main__":
    import sys

    sum_part_numbers = main(
        sys.argv[1] if len(sys.argv) > 1 else None,
        sys.argv[2] if len(sys.argv) > 2 else None,
    )
    print(f"Sum is {sum_part_numbers}")
