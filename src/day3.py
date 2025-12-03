import functools

@functools.cache
def max_joltage(bank: str, jolt_length: int) -> int:
    if jolt_length == 1:
        # print (f"jolt length 1, returing highest value {max(map(int, bank))}")
        return max(map(int, bank))
        
    best_joltage = 0
    for i in range(len(bank) - jolt_length + 1):
        best_joltage = max(best_joltage, int(bank[i] + "0" * (jolt_length - 1)) + max_joltage(bank[i+1:], jolt_length=jolt_length - 1))
    return best_joltage

def part1(lines: list[str]) -> int:
    return sum([max_joltage(line, jolt_length=2) for line in lines])


def part2(lines: list[str]) -> int:
    return sum([max_joltage(line, jolt_length=12) for line in lines])
