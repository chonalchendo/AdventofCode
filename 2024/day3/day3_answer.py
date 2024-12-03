import re
from itertools import chain


def main() -> None:
    with open("day3/day3_data.txt") as f:
        data = f.read()

        # first part
        matches = re.findall(pattern=r"mul\((\d+),(\d+)\)", string=data)
        answer1 = sum([int(match[0]) * int(match[1]) for match in matches])

        # second part
        matches2 = re.findall(
            pattern=r"(?:\w*do\(\))(.*?)(?:\w*don't\(\))", string=data, flags=re.DOTALL
        )

        # get data before first don't
        to_first_dont = re.search(r"(.*?)don't\(\)", data)
        matches2.append(str(to_first_dont.group(1)))

        # parse new data
        data2 = list(
            chain.from_iterable(
                [
                    re.findall(pattern=r"mul\((\d+),(\d+)\)", string=match)
                    for match in matches2
                ]
            )
        )
        answer2 = sum([int(match[0]) * int(match[1]) for match in data2])

        print(answer1)
        print(answer2)


if __name__ == "__main__":
    main()
