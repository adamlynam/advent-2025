from day11 import part1, part2

example1: str = """aaa: you hhh
you: bbb ccc
bbb: ddd eee
ccc: ddd eee fff
ddd: ggg
eee: out
fff: out
ggg: out
hhh: ccc fff iii
iii: out"""

example2: str = """svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 5


def test_part1_real_input():
    f = open("input/day11.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 508


def test_part2_example():
    lines = example2.split("\n")
    assert part2(lines) == 2


def test_part2_real_input():
    f = open("input/day11.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 315116216513280
