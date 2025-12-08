import functools


def find_start(lines: list[str]) -> (int, int):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "S":
                return (x, y)


def find_splitters(lines: list[str]) -> frozenset[(int, int)]:
    splitters = set()
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "^":
                splitters.add((x, y))

    return frozenset(splitters)


@functools.cache
def find_beam_spliters(
    start: (int, int), splitters: frozenset[(int, int)], max_y: int
) -> frozenset[(int, int)]:
    x, y = start
    while True:
        if (x, y) in splitters:
            # splitter found, split beam
            return frozenset(
                set([(x, y)])
                | find_beam_spliters((x - 1, y), splitters, max_y)
                | find_beam_spliters((x + 1, y), splitters, max_y)
            )
        elif y >= max_y:
            return frozenset()
        else:
            y = y + 1


def part1(lines: list[str]) -> int:
    start = find_start(lines)
    return len(
        find_beam_spliters(
            start=start, splitters=find_splitters(lines), max_y=(len(lines) - 1)
        )
    )


@functools.cache
def count_timelines(
    start: (int, int), splitters: frozenset[(int, int)], max_y: int
) -> int:
    x, y = start
    while True:
        if (x, y) in splitters:
            # splitter found, split beam
            return count_timelines((x - 1, y), splitters, max_y) + count_timelines(
                (x + 1, y), splitters, max_y
            )
        elif y >= max_y:
            return 1
        else:
            y = y + 1


def part2(lines: list[str]) -> int:
    start = find_start(lines)
    return count_timelines(
        start=start, splitters=find_splitters(lines), max_y=(len(lines) - 1)
    )
