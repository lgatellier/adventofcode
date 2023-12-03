import re

from aoc.y23 import day03 as puzzle


def test_find_numbers_middle():
    input = "...454$...655..."
    numbers = puzzle.find_numbers(input)
    assert len(numbers) == 2
    assert numbers[0].group(0) == "454"
    assert numbers[1].group(0) == "655"


def test_find_numbers_start():
    input = "876$...678..."
    numbers = puzzle.find_numbers(input)
    assert len(numbers) == 2
    assert numbers[0].group(0) == "876"
    assert numbers[1].group(0) == "678"


def test_find_numbers_end():
    input = "...123$...321"
    numbers = puzzle.find_numbers(input)
    assert len(numbers) == 2
    assert numbers[0].group(0) == "123"
    assert numbers[1].group(0) == "321"


def test_find_all_numbers():
    input = ["...454$...655...", "876$...678...", "...123$...321"]
    numbers = puzzle.find_all_numbers(input)
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
    assert not puzzle.has_symbol(input, 0, 4)
    assert puzzle.has_symbol(input, 4, 5)
    assert not puzzle.has_symbol(input, 5, 9)


def test_is_part_number_shouldReturnFalse_whenNoSymbolInAnyLine():
    lines = [".......", "....456.....123....", "......."]
    ctx = puzzle.Context(lines, 1)
    match = re.search(r"\d+", lines[1])
    assert not puzzle.is_part_number(ctx, match)


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInSameLineAfterNumber():
    lines = ["....456$.....123...."]
    ctx = puzzle.Context(lines, 0)
    match = re.search(r"\d+", lines[0])
    assert puzzle.is_part_number(ctx, match)


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInSameLineBeforeNumber():
    lines = ["....*456.....123...."]
    ctx = puzzle.Context(lines, 0)
    match = re.search(r"\d+", lines[0])
    assert puzzle.is_part_number(ctx, match)


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInPreviousLineBeforeNumber():
    lines = [
        "....*",  # previous line
        "....456.....123....",  # current line
    ]
    ctx = puzzle.Context(lines, 1)
    match = re.search(r"\d+", lines[1])
    assert puzzle.is_part_number(ctx, match)


def test_is_part_number_shouldReturnTrue_whenAdjacentSymbolInNextLineAfterNumber():
    lines = ["....456.....123....", ".......*"]  # current line  # next line
    ctx = puzzle.Context(lines, 0)
    match = re.search(r"\d+", lines[0])
    assert puzzle.is_part_number(ctx, match)


def test_is_part_number_shouldReturnFalse_whenAdjacentSymbolInPreviousLineAfterNumber():
    lines = [".......*", "....456.....123...."]  # previous line  # current line
    ctx = puzzle.Context(lines, 1)
    match = re.search(r"\d+", lines[1])
    assert puzzle.is_part_number(ctx, match)


def test_is_part_number_shouldReturnFalse_whenAdjacentSymbolInNextLineBeforeNumber():
    lines = [
        "....456.....123....",  # current line
        "...*",  # next line
    ]
    ctx = puzzle.Context(lines, 0)
    match = re.search(r"\d+", lines[0])
    assert puzzle.is_part_number(ctx, match)
