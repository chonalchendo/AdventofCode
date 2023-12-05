import re


def check_digits(num: str) -> int:
    number = str(num[0]) + str(num[-1])
    return int(number)


def num_convert() -> dict[str, str]:
    numbers_str = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    numbers_int = [str(x) for x in range(1, 10)]

    return {k: v for k, v in zip(numbers_str, numbers_int)}


def split_words(line: str, converter: dict[str, str]):
    index_pos = {}
    for pattern in list(converter.keys()):
        match = re.search(pattern, line)
        if match:
            index_pos[pattern] = match.start()

    if not index_pos:
        return line

    lowest_key = min(index_pos, key=index_pos.get)
    highest_key = max(index_pos, key=index_pos.get)

    values = [lowest_key, highest_key]

    if lowest_key and highest_key:
        new_line = line
        for value in values:
            new_line = re.sub(value, converter.get(value), new_line)
    return new_line


def deal_with_digit(line: str) -> int:
    converter = num_convert()
    value = split_words(line, converter)
    complete = "".join(filter(str.isdigit, value))
    # print(complete)
    final = check_digits(complete)
    print(final)
    return final


def main() -> None:
    with open("input", "r") as f:
        values = [deal_with_digit(x) for x in f if len(x.strip()) > 1]
        f.close()
        print(sum(values))


if __name__ == "__main__":
    main()
