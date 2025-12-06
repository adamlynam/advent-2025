from math import prod


def split_rows(lines: list[str]) -> list[list[str]]:
    return [line.split() for line in lines]


def parse_problems(lines: list[str]) -> list[list[int], bool]:
    problems = list()
    rows = split_rows(lines)
    number_rows = rows[:-1]
    operator_row = rows[len(rows) - 1]
    for i in range(len(operator_row)):
        problems.append(
            (
                [int(number_row[i]) for number_row in number_rows],
                operator_row[i] == "+",
            )
        )
    return problems


def solve_problem(numbers: list[int], is_adding: bool):
    if is_adding:
        return sum(numbers)
    else:
        return prod(numbers)


def part1(lines: list[str]) -> int:
    return sum(
        solve_problem(numbers, is_adding)
        for numbers, is_adding in parse_problems(lines)
    )


def parse_cephalopod_digit(cephalopod_digit: str) -> str:
    if cephalopod_digit == " ":
        return ""

    return cephalopod_digit


def parse_cephalopod_numbers(lines: list[str]) -> list[list[int]]:
    cephalopod_numbers = list()
    for i in range(len(lines[0])):
        cephalopod_number = "0"
        for j in range(len(lines)):
            cephalopod_number = cephalopod_number + parse_cephalopod_digit(lines[j][i])
        cephalopod_numbers.append(int(cephalopod_number))
    return cephalopod_numbers


def group_cephalopod_numbers(cephalopod_numbers: list[int]):
    grouped_cephalopod_numbers = list()
    current_group = list()
    for number in cephalopod_numbers:
        if number == 0:
            grouped_cephalopod_numbers.append(current_group)
            current_group = list()
        else:
            current_group.append(number)
    grouped_cephalopod_numbers.append(current_group)
    return grouped_cephalopod_numbers


def parse_cephalopod_problems(lines: list[str]) -> list[list[int], bool]:
    problems = list()
    rows = split_rows(lines)
    cephalopod_numbers = parse_cephalopod_numbers(lines[:-1])
    grouped_cephalopod_numbers = group_cephalopod_numbers(cephalopod_numbers)
    operator_row = rows[len(rows) - 1]
    for i in range(len(operator_row)):
        problems.append(
            (
                grouped_cephalopod_numbers[i],
                operator_row[i] == "+",
            )
        )
    return problems


def part2(lines: list[str]) -> int:
    return sum(
        solve_problem(numbers, is_adding)
        for numbers, is_adding in parse_cephalopod_problems(lines)
    )
