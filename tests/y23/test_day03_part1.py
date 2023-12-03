import re

from aoc.y23.day03 import part1


def test_find_numbers_middle():
    input = "...454$...655..."
    numbers = part1.find_numbers(input)
    assert len(numbers) == 2
    assert numbers[0].group(0) == "454"
    assert numbers[1].group(0) == "655"


def test_find_numbers_start():
    input = "876$...678..."
    numbers = part1.find_numbers(input)
    assert len(numbers) == 2
    assert numbers[0].group(0) == "876"
    assert numbers[1].group(0) == "678"


def test_find_numbers_end():
    input = "...123$...321"
    numbers = part1.find_numbers(input)
    assert len(numbers) == 2
    assert numbers[0].group(0) == "123"
    assert numbers[1].group(0) == "321"


def test_find_all_numbers():
    input = ["...454$...655...", "876$...678...", "...123$...321"]
    numbers = part1.find_all_numbers(input)
    assert len(numbers) == 3
    assert len(numbers[0]) == 2
    assert len(numbers[1]) == 2
    assert len(numbers[2]) == 2
    assert numbers[0][0].group(0) == "454"
    assert numbers[0][1].group(0) == "655"
    assert numbers[1][0].group(0) == "876"
    assert numbers[1][1].group(0) == "678"
    assert numbers[2][0].group(0) == "123"
    assert numbers[2][1].group(0) == "321"


def test_has_symbol():
    input = ".7..$..45."
    assert part1.has_symbol(input, 0, 4) == False
    assert part1.has_symbol(input, 4, 5) == True
    assert part1.has_symbol(input, 5, 9) == False


def test_is_part_number_shouldReturnFalse_whenNoSymbolInAnyLine():
    line = "....456.....123...."
    previous_line = "......."
    next_line = "......."
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, previous_line, next_line, match) == False


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInSameLineAfterNumber():
    line = "....456$.....123...."
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, None, None, match) == True


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInSameLineBeforeNumber():
    line = "....*456.....123...."
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, None, None, match) == True


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInPreviousLineBeforeNumber():
    line = "....456.....123...."
    previous_line = "....*"
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, previous_line, None, match) == True


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInNextLineAfterNumber():
    line = "....456.....123...."
    next_line = ".......*"
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, None, next_line, match) == True


def test_is_part_number_shouldReturnFalse_whenAdjacentSymbolInPreviousLineAfterNumber():
    line = "....456.....123...."
    previous_line = ".......*"
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, previous_line, None, match) == True


def test_is_part_number_shouldReturnFalse_whenAdjacentSymbolInNextLineBeforeNumber():
    line = "....456.....123...."
    next_line = "...*"
    match = re.search(r"\d+", line)
    assert part1.is_part_number(line, None, next_line, match) == True


def test_main():
    assert part1.main("tests/y23/input_day03") == 527369
