import importlib
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
    typer.echo(f"Starting AdventOfCode 20{year:02d} Day {day} Part {part}")

    module = importlib.import_module(module_name)
    module.main(input=input_file)


if __name__ == "__main__":
    app()
