from datetime import date
import importlib
import os
from pathlib import Path
import typer
from typing import Optional


app = typer.Typer(
    name="aoc", rich_markup_mode="rich", help="Advent of Code CLI", no_args_is_help=True
)

today = date.today()


def validate_year(year: int) -> bool:
    if year < 100:
        year += 2000
    if year < 2015:
        raise typer.BadParameter(f"Advent Of Code did not exist before 2015")
    if year > today.year or year == today.year and today.month < 12:
        raise typer.BadParameter(f"Advent Of Code has not started yet for year {year}")
    return year


def validate_day(day: int) -> bool:
    if not 1 <= day <= 25:
        raise typer.BadParameter(f"Day must be between 1 and 25")
    return day


@app.command()
def run(
    year: int = typer.Argument(callback=validate_year, help="The year of the puzzle"),
    day: int = typer.Argument(callback=validate_day, help="The day of the puzzle"),
    part: int = typer.Argument(1, help="The part number of the puzzle (1 or 2)"),
    input_file: Optional[Path] = typer.Argument(
        "./input",
        exists=True,
        file_okay=True,
        dir_okay=False,
        writable=False,
        readable=True,
        resolve_path=True,
        help="Your AoC puzzle input file.",
    ),
):
    module_name = f"aoc.y{year - 2000}.day{day:02d}.part{part}"

    if not os.path.exists(input_file):
        print("test")
        typer.echo(f"ERROR : Input file {input_file} does not exist", err=True)
        raise typer.Exit(code=1)

    try:
        module = importlib.import_module(module_name)
        typer.echo(f"Starting AdventOfCode {year} Day {day} Part {part}")
        module.main(input=input_file)
    except ModuleNotFoundError as err:
        typer.echo(
            f"ERROR : AdventOfCode {year} Day {day} Part {part} does not exist or is not implemented yet",
            err=True,
        )
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
