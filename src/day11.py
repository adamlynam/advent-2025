import functools


def parse_node_lookup(line: str) -> (str, tuple[str]):
    inputs, outputs = line.split(":")
    return (inputs, tuple(outputs.split()))


def parse_nodes_lookups(lines: list[str]) -> frozenset[(str, tuple[str])]:
    return frozenset([parse_node_lookup(line) for line in lines])


@functools.cache
def unique_paths_from(current_node: str, nodes: frozenset[(str, tuple[str])]):
    if current_node == "out":
        return 1

    outputs = dict(nodes)[current_node]

    return sum(unique_paths_from(node, nodes) for node in outputs)


def part1(lines: list[str]) -> int:
    node_lookups = parse_nodes_lookups(lines)
    return unique_paths_from("you", node_lookups)


@functools.cache
def unique_paths_with_dac_and_fft_from(
    current_node: str,
    nodes: frozenset[(str, tuple[str])],
    dac_already_seen: bool,
    fft_already_seen: bool,
) -> int:
    if current_node == "out":
        if dac_already_seen and fft_already_seen:
            return 1
        else:
            return 0

    unique_paths_with_dac_and_fft = 0
    for node in dict(nodes)[current_node]:
        was_unqiue_paths = unique_paths_with_dac_and_fft_from(
            node,
            nodes,
            dac_already_seen or current_node == "dac",
            fft_already_seen or current_node == "fft",
        )
        unique_paths_with_dac_and_fft = unique_paths_with_dac_and_fft + was_unqiue_paths

    return unique_paths_with_dac_and_fft


def part2(lines: list[str]) -> int:
    node_lookups = parse_nodes_lookups(lines)
    return unique_paths_with_dac_and_fft_from(
        current_node="svr",
        nodes=node_lookups,
        dac_already_seen=False,
        fft_already_seen=False,
    )
