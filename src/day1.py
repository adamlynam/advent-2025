import sys


def part1(lines: list[str]) -> int:
    dial_position = 50
    zero_count = 0
    for line in lines:
        move = int(line[1:])
        if "L" in line:
            dial_position = dial_position - move
        else:
            dial_position = dial_position + move
        
        if dial_position % 100 == 0:
            zero_count = zero_count + 1

    return zero_count


def part2(lines: list[str]) -> int:
    dial_position = 50
    zero_count = 0
    for line in lines:
        print (line)
        move = int(line[1:])
        if "L" in line:
            if dial_position == 0:
                print ("add buffer")
                dial_position = 100 # add buffer to prevent double counting zeros
            dial_position = dial_position - move
        else:
            dial_position = dial_position + move
        
        while dial_position < 0:
            print(dial_position)
            dial_position = dial_position + 100
            zero_count = zero_count + 1
        
        while dial_position > 100:
            print(dial_position)
            dial_position = dial_position - 100
            zero_count = zero_count + 1

        if dial_position == 0 or dial_position == 100:
            print(dial_position)
            dial_position = 0
            zero_count = zero_count + 1
        
        print (f"zero count is {zero_count}")

    return zero_count
