from day2 import part1, part2

example1: str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""


def test_part1_example():
    lines = example1.split("\n")
    assert part1(lines) == 1227775554

def test_part1_single_example():
    assert part1(["11-22"]) == 33

def test_part1_single_example2():
    assert part1(["95-115"]) == 99

def test_part1_real_input():
    f = open("input/day2.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part1(lines) == 44487518055


def test_part2_example():
    lines = example1.split("\n")
    assert part2(lines) == 4174379265

def test_part2_single_example():
    assert part2(["11-22"]) == 33

def test_part2_single_example2():
    assert part2(["95-115"]) == (99 + 111)

def test_part2_single_example3():
    assert part2(["998-1012"]) == (999 + 1010)

def test_part2_single_example4():
    assert part2(["1188511880-1188511890"]) == 1188511885

def test_part2_single_example5():
    assert part2(["222220-222224"]) == 222222

def test_part2_single_example6():
    assert part2(["1698522-1698528"]) == 0

def test_part2_single_example7():
    assert part2(["446443-446449"]) == 446446

def test_part2_single_example8():
    assert part2(["38593856-38593862"]) == 38593859

def test_part2_single_example9():
    assert part2(["565653-565659"]) == 565656

def test_part2_single_example10():
    assert part2(["824824821-824824827"]) == 824824824

def test_part2_single_example11():
    assert part2(["2121212118-2121212124"]) == 2121212121

def test_part2_real_input():
    f = open("input/day2.txt", "r")
    lines = list(map(lambda line: line.replace("\n", ""), f.readlines()))
    assert part2(lines) == 53481866137
