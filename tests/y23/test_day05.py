from aoc import utils
from aoc.y23.day05 import parse_context, part1


from test_utils import run_main


def test_parse_context():
    utils.state["verbose"] = True
    lines = [
        "seeds: 28965817 302170009 1752849261",
        "",
        "seed-to-soil map:",
        "3680121696 1920754815 614845600",
    ]
    ctx = parse_context(lines)
    assert len(ctx.seeds) == 3
    assert 28965817 in ctx.seeds
    assert 302170009 in ctx.seeds
    assert 1752849261 in ctx.seeds
    assert ctx.map_value("seed", 1) == 1
    assert ctx.map_value("seed", 1920754815) == 3680121696
    assert ctx.map_value("seed", 1920754915) == 3680121796


def test_parse_context_ranges():
    utils.state["verbose"] = True
    lines = [
        "seeds: 28965817 302170009 1752849261 48290258",
        "",
        "seed-to-soil map:",
        "3680121696 1920754815 614845600",
    ]
    ctx = parse_context(lines, ranges=True)
    assert ctx.seeds is None
    assert len(ctx.seed_ranges) == 2
    assert (28965817, 302170009) in ctx.seed_ranges
    assert (1752849261, 48290258) in ctx.seed_ranges


def test_main():
    utils.state["verbose"] = True
    result = run_main(part1.main, "tests/y23/input_day05")
    assert min(result["location"]) == 525792406
