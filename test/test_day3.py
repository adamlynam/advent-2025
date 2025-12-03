from day3 import part1, part2

example1: str = """987654321111111
811111111111119
234234234234278
818181911112111"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 357


def test_part1_single_example1():
    assert part1(["987654321111111"]) == 98

def test_part1_single_example2():
    assert part1(["811111111111119"]) == 89

def test_part1_single_example3():
    assert part1(["234234234234278"]) == 78

def test_part1_single_example4():
    assert part1(["818181911112111"]) == 92


def test_part1_real_input():
    f = open("input/day3.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 17244


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 3121910778619

def test_part2_single_example1():
    assert part2(["987654321111111"]) == 987654321111

def test_part2_single_example2():
    assert part2(["811111111111119"]) == 811111111119

def test_part2_single_example3():
    assert part2(["234234234234278"]) == 434234234278

def test_part2_single_example4():
    assert part2(["818181911112111"]) == 888911112111


def test_part2_real_input():
    f = open("input/day3.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 171435596092638
