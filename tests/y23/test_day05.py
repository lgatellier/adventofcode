from aoc import utils
from aoc.y23.day05 import parse_context, part1, part2, Range


from test_utils import run_main


def test_parse_context():
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
    assert Range(28965817, length=302170009) in ctx.seed_ranges
    assert Range(1752849261, length=48290258) in ctx.seed_ranges
    range1_map = ctx.map_range("seed", Range(28965817, length=302170009))
    assert len(range1_map) == 1
    assert Range(28965817, length=302170009) in range1_map
    range2_map = ctx.map_range("seed", Range(1920754815 + 15, 1920754815 + 30))
    assert len(range2_map) == 1
    assert Range(3680121696 + 15, 3680121696 + 30) in range2_map
    range3_map = ctx.map_range(
        "seed", Range(1920754815 + 614845600 - 11, 1920754815 + 614845600 + 9)
    )
    assert len(range3_map) == 2
    assert (
        Range(3680121696 + 614845600 - 11, 3680121696 + 614845600 - 1) == range3_map[0]
    )
    assert Range(1920754815 + 614845600, 1920754815 + 614845600 + 9) == range3_map[1]


def test_part1_main():
    result = run_main(part1.main, "tests/y23/input_day05")
    assert min(result["location"]) == 525792406


def test_range_overlaps_():
    assert not Range(5, 9).overlaps(Range(1, 3))
    assert Range(5, 9).overlaps(Range(1, 5))
    assert Range(5, 9).overlaps(Range(1, 6))
    assert Range(5, 9).overlaps(Range(1, 9))
    assert Range(5, 9).overlaps(Range(1, 12))
    assert Range(5, 9).overlaps(Range(5, 5))
    assert Range(5, 9).overlaps(Range(5, 8))
    assert Range(5, 9).overlaps(Range(5, 9))
    assert Range(5, 9).overlaps(Range(5, 12))
    assert Range(5, 9).overlaps(Range(7, 8))
    assert Range(5, 9).overlaps(Range(7, 9))
    assert Range(5, 9).overlaps(Range(7, 12))
    assert Range(5, 9).overlaps(Range(9, 9))
    assert Range(5, 9).overlaps(Range(9, 12))
    assert not Range(5, 9).overlaps(Range(10, 12))


def test_range_intersection():
    assert Range(5, 9) & Range(1, 3) is None
    assert Range(5, 9) & Range(1, 5) == Range(5)
    assert Range(5, 9) & Range(1, 6) == Range(5, 6)
    assert Range(5, 9) & Range(1, 9) == Range(5, 9)
    assert Range(5, 9) & Range(1, 12) == Range(5, 9)
    assert Range(5, 9) & Range(5, 5) == Range(5)
    assert Range(5, 9) & Range(5, 8) == Range(5, 8)
    assert Range(5, 9) & Range(5, 9) == Range(5, 9)
    assert Range(5, 9) & Range(5, 12) == Range(5, 9)
    assert Range(5, 9) & Range(7, 8) == Range(7, 8)
    assert Range(5, 9) & Range(7, 9) == Range(7, 9)
    assert Range(5, 9) & Range(7, 12) == Range(7, 9)
    assert Range(5, 9) & Range(9, 9) == Range(9)
    assert Range(5, 9) & Range(9, 12) == Range(9)
    assert Range(5, 9) & Range(10, 12) is None


def test_part2_main():
    result = run_main(part2.main, "tests/y23/input_day05")
    assert min([r.start for r in result["location"]]) == 79004094
