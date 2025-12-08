from day7 import part1, part2

example1: str = """.......S.......
.......|.......
......|^|......
......|.|......
.....|^|^|.....
.....|.|.|.....
....|^|^|^|....
....|.|.|.|....
...|^|^|||^|...
...|.|.|||.|...
..|^|^|||^|^|..
..|.|.|||.|.|..
.|^|||^||.||^|.
.|.|||.||.||.|.
|^|^|^|^|^|||^|
|.|.|.|.|.|||.|"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 21


def test_part1_real_input():
    f = open("input/day7.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 1615


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 40


def test_part2_real_input():
    f = open("input/day7.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 43560947406326
