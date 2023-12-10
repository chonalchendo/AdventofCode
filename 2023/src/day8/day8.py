from itertools import cycle
from math import lcm


def create_data(data: list[str]) -> tuple[list[int | str], dict[str, list[str]]]:
    replace_vals = {"L": 0, "R": 1}
    instructions = [replace_vals.get(char, char) for char in data[0]]
    paths = [path.split(" = ") for path in data[1:] if path != ""]
    paths = {key: value[1:-1].split(", ") for key, value in paths}
    return instructions, paths


def solver(data: list[str], start: str, target: str) -> int:
    instructions, paths = create_data(data)
    ints = cycle(instructions)
    current_path = start
    for i, j in enumerate(ints):
        if len(target) == 3:
            if current_path == target:
                return i
        else:
            if current_path.endswith(target):
                return i
        current_path = paths[current_path][j]


def main():
    with open("input") as f:
        lines = f.read().strip().split("\n")
        _, paths = create_data(lines)

        # part 1
        part1 = solver(data=lines, start="AAA", target="ZZZ")
        print(part1)

        # part 2
        end_a = [char for char in paths.keys() if char[-1] == "A"]
        part_2 = lcm(*[solver(data=lines, start=start, target="Z") for start in end_a])
        print(part_2)


if __name__ == "__main__":
    main()
