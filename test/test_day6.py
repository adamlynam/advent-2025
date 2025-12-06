from day6 import part1, part2

example1: str = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 4277556


def test_part1_real_input():
    f = open("input/day6.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 6605396225322


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 3263827


def test_part2_real_input():
    f = open("input/day6.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 11052310600986
