def main() -> None:
    with open("day2/day2_data.txt", "r") as f:
        data = [
            [int(value) for value in row.strip().split(" ")] for row in f.readlines()
        ]

        answer1 = 0

        for row in data:
            descending = all(row[i] > row[i + 1] for i in range(len(row) - 1))
            ascending = all(row[i] < row[i + 1] for i in range(len(row) - 1))

            valid_differences = all(
                0 < abs(row[i] - row[i + 1]) <= 3 for i in range(len(row) - 1)
            )

            if (descending or ascending) and valid_differences:
                answer1 += 1

            descending_pairs = [row[i] > row[i + 1] for i in range(len(row) - 1)]
            descending_nearly_false = sum(1 for x in descending_pairs if not x) == 1
            print(descending_nearly_false)


if __name__ == "__main__":
    main()
