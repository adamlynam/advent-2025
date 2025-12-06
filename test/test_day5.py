from day5 import part1, part2

example1: str = """3-5
10-14
16-20
12-18

1
5
8
11
17
32"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 3


def test_part1_real_input():
    f = open("input/day5.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 874


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 14


def test_part2_real_input():
    f = open("input/day5.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 348548952146313
