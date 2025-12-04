def adjacent_rolls(lines: list[str], x, y) -> int:
    adjacent_spaces = [
        (x - 1, y - 1),
        (x, y - 1),
        (x + 1, y - 1),
        (x - 1, y),
        (x + 1, y),
        (x - 1, y + 1),
        (x, y + 1),
        (x + 1, y + 1),
    ]
    return len([(i, j) for (i, j) in adjacent_spaces if i >= 0 and j >= 0 and i < len(lines) and j < len(lines[0]) and lines[i][j] == "@"])

def get_accessible_rolls(lines: list[str]) -> list[(int, int)]:
    accessible_rolls = list()
    
    for x in range(len(lines)):
        for y in range(len(lines[0])):
            if lines[x][y] == "@" and adjacent_rolls(lines, x, y) < 4:
                accessible_rolls.append((x, y))

    return accessible_rolls

def remove_accessible_rolls(lines: list[str], accessible_rolls: list[(int, int)]) -> list[str]:
    for x, y, in accessible_rolls:
        lines[x] = lines[x][:y] + "." + lines[x][y + 1:]
    return lines

def part1(lines: list[str]) -> int:
    return len(get_accessible_rolls(lines))

def part2(lines: list[str]) -> int:
    accessible_rolls = get_accessible_rolls(lines)
    total_removed = 0
    while (len(accessible_rolls) > 0):
        total_removed = total_removed + len(accessible_rolls)
        lines = remove_accessible_rolls(lines, accessible_rolls)

        accessible_rolls = get_accessible_rolls(lines)
    
    return total_removed
