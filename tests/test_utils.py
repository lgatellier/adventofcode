from pathlib import Path


from aoc import utils


def run_main(main: callable, input_file: Path):
    """
    Run a puzzle `main()` method against `input_file`
    """
    return main(utils.read_file(input_file))
