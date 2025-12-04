from day4 import part1, part2

example1: str = """..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 13


def test_part1_real_input():
    f = open("input/day4.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 1602


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 43


def test_part2_real_input():
    f = open("input/day4.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 9518
