import re


def main() -> None:
    with open("input") as f:
        lines = f.read().split("\n")

        special_positions = {
            (i, p): k
            for i, l in enumerate(lines)
            for p, k in enumerate(l)
            if k != "." and not k.isdigit()
        }
        print(special_positions)
        part_nums = 0

        for i, l in enumerate(lines):
            for match in re.finditer(r"\d+", l):
                for (y, x), p in special_positions.items():
                    if (match.start() - 1 <= x <= match.end()) and (
                        i - 1 <= y <= i + 1
                    ):
                        num = int(match.group())
                        part_nums += num
    print(part_nums)


if __name__ == "__main__":
    main()
