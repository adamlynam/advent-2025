def parse_fresh_ranges(lines: list[str]) -> list[str]:
    return [line for line in lines if "-" in line]


def parse_ingredients(lines: list[str]) -> list[int]:
    return [int(line) for line in lines if line != "" and "-" not in line]


def ingredient_is_fresh(ingredient: int, fresh_ranges: list[str]):
    for fresh_range in fresh_ranges:
        start, finish = map(int, fresh_range.split("-"))
        if ingredient >= start and ingredient <= finish:
            return True
    return False


def find_fresh_ingredients(
    fresh_ranges: list[str], ingredients: list[int]
) -> list[int]:
    return [
        ingredient
        for ingredient in ingredients
        if ingredient_is_fresh(ingredient, fresh_ranges)
    ]


def part1(lines: list[str]) -> int:
    fresh_ranges = parse_fresh_ranges(lines)
    ingredients = parse_ingredients(lines)
    return len(find_fresh_ingredients(fresh_ranges, ingredients))


def fix_overlapping_range(fresh_range: str, fresh_ranges: list[str]):
    other_fresh_ranges = fresh_ranges[:]
    other_fresh_ranges.remove(fresh_range)
    start, finish = map(int, fresh_range.split("-"))
    for other_range in other_fresh_ranges:
        other_start, other_finish = map(int, other_range.split("-"))
        if start >= other_start and start <= other_finish:
            # the range starts inside another range
            if finish <= other_finish:
                # the entire range is inside the other range
                return None
            else:
                print(
                    f"{fresh_range} overlaps with {other_range}, changing to {other_finish + 1}-{finish}"
                )
                return f"{other_finish + 1}-{finish}"
        elif finish >= other_start and finish <= other_finish:
            #  the range ends inside another range
            if start >= other_start:
                # the entire range is inside the other range
                return None
            else:
                print(
                    f"{fresh_range} overlaps with {other_range}, changing to {start}-{other_start - 1}"
                )
                return f"{start}-{other_start - 1}"

    return fresh_range


def remove_overlapping_ranges(fresh_ranges: list[str]) -> list[str]:
    overlap_seen = True
    potentially_overlapping_ranges = fresh_ranges
    while overlap_seen:
        overlap_seen = False
        new_ranges = potentially_overlapping_ranges[:]
        for fresh_range in potentially_overlapping_ranges:
            fixed_fresh_range = fix_overlapping_range(
                fresh_range, potentially_overlapping_ranges
            )
            if fresh_range != fixed_fresh_range:
                overlap_seen = True
                new_ranges.remove(fresh_range)
                if fixed_fresh_range is not None:
                    new_ranges.append(fixed_fresh_range)
                break
        potentially_overlapping_ranges = new_ranges

    return potentially_overlapping_ranges


def count_fresh_ids(fresh_ranges: list[str]) -> int:
    fresh_ids = 0
    for fresh_range in fresh_ranges:
        start, finish = map(int, fresh_range.split("-"))
        fresh_ids = fresh_ids + finish - start + 1

    return fresh_ids


def part2(lines: list[str]) -> int:
    return count_fresh_ids(remove_overlapping_ranges(parse_fresh_ranges(lines)))
