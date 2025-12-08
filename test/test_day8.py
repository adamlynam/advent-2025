from day8 import part1, part2

example1: str = """162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines, 10) == 40


def test_part1_real_input():
    f = open("input/day8.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines, 1000) == 117000


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 25272


def test_part2_real_input():
    f = open("input/day8.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 8368033065
