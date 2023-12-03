import importlib
import os
import typer

app = typer.Typer(
    name="aoc", rich_markup_mode="rich", help="Advent of Code CLI", no_args_is_help=True
)


@app.command()
def run(
    year: int,
    day: int,
    part: int,
    input_file: str = typer.Argument(
        "input",
        help="Your AoC puzzle input file. Defaults to 'input' in the current directory.",
    ),
):
    module_name = f"aoc.y{year}.day{day:02d}.part{part}"

    if not os.path.exists(input_file):
        print("test")
        typer.echo(f"ERROR : Input file {input_file} does not exist", err=True)
        raise typer.Exit(code=1)

    try:
        module = importlib.import_module(module_name)
        typer.echo(f"Starting AdventOfCode 20{year:02d} Day {day} Part {part}")
        module.main(input=input_file)
    except ModuleNotFoundError as err:
        typer.echo(
            f"ERROR : AdventOfCode 20{year:02d} Day {day} Part {part} does not exist or is not implemented yet",
            err=True,
        )
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
