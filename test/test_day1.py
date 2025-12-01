from day1 import part1, part2

example1: str = """L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 3


def test_part1_real_input():
    f = open("input/day1.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 1195


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 6


def test_part2_real_input():
    f = open("input/day1.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 6770
