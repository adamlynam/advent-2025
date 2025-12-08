import math
from itertools import combinations


def parse_juction_box_locations(lines: list[str]) -> list[(int, int, int)]:
    return [
        (int(line.split(",")[0]), int(line.split(",")[1]), int(line.split(",")[2]))
        for line in lines
    ]


def generate_all_pairs_by_distance(
    boxes: list[(int, int, int)],
) -> list[((int, int, int), (int, int, int), int)]:
    return list(
        map(
            lambda pair: (
                pair[0],
                pair[1],
                math.sqrt(
                    pow(pair[0][0] - pair[1][0], 2)
                    + pow(pair[0][1] - pair[1][1], 2)
                    + pow(pair[0][2] - pair[1][2], 2)
                ),
            ),
            combinations(boxes, 2),
        )
    )


def sort_pairs_by_distance(
    pairs: list[(int, int, int), (int, int, int), int],
) -> list[(int, int, int), (int, int, int), int]:
    return sorted(pairs, key=lambda x: x[2])


def connect_pair_to_circuits(
    pair: ((int, int, int), (int, int, int), int), circuits: list[set[(int, int, int)]]
) -> list[set[(int, int, int)]]:
    first_box, second_box, _ = pair
    first_box_in_circuit = None
    second_box_in_circuit = None
    for circuit in circuits:
        if first_box in circuit:
            first_box_in_circuit = circuit
        if second_box in circuit:
            second_box_in_circuit = circuit
    if first_box_in_circuit is None and second_box_in_circuit is None:
        # not in an existing circuit, make a new one
        circuits.append(set([first_box, second_box]))
    elif first_box_in_circuit == second_box_in_circuit:
        return circuits
    elif first_box_in_circuit is not None and second_box_in_circuit is None:
        # add second box to first box circuit
        first_box_in_circuit.add(second_box)
    elif second_box_in_circuit is not None and first_box_in_circuit is None:
        # add second box to first box circuit
        second_box_in_circuit.add(first_box)
    elif first_box_in_circuit is not None and second_box_in_circuit is not None:
        # both boxes in different circuits, merge them
        circuits.remove(first_box_in_circuit)
        circuits.remove(second_box_in_circuit)
        circuits.append(first_box_in_circuit | second_box_in_circuit)
    else:
        raise NotImplementedError("Unhandled circuit case")

    return circuits


def connect_circuts(
    pairs: list[((int, int, int), (int, int, int), int)], connect: int
) -> list[set[(int, int, int)]]:
    circuits = list()
    for i in range(connect):
        circuits = connect_pair_to_circuits(pairs[i], circuits)
    return circuits


def top_three_circuit_lengths(
    circuits: list[set[(int, int, int)]],
) -> list[set[(int, int, int)]]:
    sorted_by_length = sorted(circuits, key=lambda x: len(x), reverse=True)
    # print(sorted_by_length)
    return [
        len(sorted_by_length[0]),
        len(sorted_by_length[1]),
        len(sorted_by_length[2]),
    ]


def part1(lines: list[str], connect: int) -> int:
    return math.prod(
        top_three_circuit_lengths(
            connect_circuts(
                sort_pairs_by_distance(
                    generate_all_pairs_by_distance(parse_juction_box_locations(lines))
                ),
                connect,
            )
        )
    )


def part2(lines: list[str]) -> int:
    junction_boxes = parse_juction_box_locations(lines)
    pairs = sort_pairs_by_distance(generate_all_pairs_by_distance(junction_boxes))
    circuits = list()
    next_pair = pairs.pop(0)
    while len(circuits) == 0 or len(circuits[0]) != len(junction_boxes):
        # print(next_pair)
        last_pair = next_pair
        circuits = connect_pair_to_circuits(pair=next_pair, circuits=circuits)
        next_pair = pairs.pop(0)
    # return last_pair
    return last_pair[0][0] * last_pair[1][0]
