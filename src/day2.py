from math import floor

def valid_id(id: int, max_repeats: int) -> bool:
    id_as_string = str(id)
    middle_index = int(len(id_as_string) / 2)

    for i in range(1, middle_index + 1):
        # skip lengths that require more repeats than allowed
        if len(id_as_string) / i > max_repeats:
            # print (f"length {i} is too short for a limit of {max_repeats}")
            continue

        # skip lengths that don't split evenly into the string
        if len(id_as_string) % i != 0:
            continue

        compare_part = id_as_string[:i]
        # print (f"compare {compare_part}")
        invalid_id = True
        for j in range(0, floor(len(id_as_string) / i)):
            # print (f"compare to {id_as_string[j*i:(j*i)+i]}")
            if compare_part != id_as_string[j*i:(j*i)+i]:
                invalid_id = False
                break

        if invalid_id:
            # print (f"{id_as_string} is invalid")
            return False

    return True

def invalid_ids(id_range: str, max_repeats: int = 2) -> list[int]:
    # print (id_range)
    start, end = id_range.split("-")
    return [x for x in range(int(start), int(end) + 1) if not valid_id(x, max_repeats)]


def part1(lines: list[str]) -> int:
    id_ranges = lines[0].split(",")
    return sum([sum(invalid_ids(x)) for x in id_ranges])


def part2(lines: list[str]) -> int:
    id_ranges = lines[0].split(",")
    return sum([sum(invalid_ids(x, max_repeats=99)) for x in id_ranges])
