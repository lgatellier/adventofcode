import typer

app = typer.Typer(name="aoc", rich_markup_mode="rich")


@app.command()
def run(year: int, day: int, part: int):
    pass
