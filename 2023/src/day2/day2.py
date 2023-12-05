import math
import re


def extract_numbers(color: str, line: str) -> int:
    colored = [item for item in line if re.search(color, item)]
    strip = [int("".join(filter(str.isdigit, item))) for item in colored]
    return max(strip)


def process_colors(line: str) -> dict[str, int]:
    colors = ["red", "blue", "green"]
    return {color: extract_numbers(color, line) for color in colors}


def main() -> None:
    with open("input") as f:
        file = f.read().strip().split("\n")

        ids_count = 0
        total_power = 0

        for count, line in enumerate(file, start=1):
            clean_line = re.split(r"[:;,\n]", line)
            color_dict = process_colors(clean_line)
            if (
                color_dict["red"] <= 12
                and color_dict["green"] <= 13
                and color_dict["blue"] <= 14
            ):
                ids_count += count

            total_power += math.prod(color_dict.values())

    # part 1
    print(ids_count)

    # part 2
    print(total_power)


if __name__ == "__main__":
    main()
