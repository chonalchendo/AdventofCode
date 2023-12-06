import math


def calculate_wins(games: dict[str, str]):
    counts = []

    for key, value in games.items():
        count = 0
        if key == "95":
            key = int(key) - 1
        for x in range(1, int(key) + 1):
            distance = (int(key) - x) * x
            if distance > int(value):
                count += 1
        counts.append(count)

    return math.prod(counts)


with open("input") as f:
    data = f.read().strip().split("\n")

    # part 1
    stats = [[x for x in line.split(" ") if x.strip()] for line in data]

    games = dict(zip(stats[0][1:], stats[1][1:]))
    games["95"] = stats[1][-2]

    answer_1 = calculate_wins(games)

    print(answer_1)

    # part 2
    final_stat = ["".join(x).split(":") for x in stats]
    final_game = {final_stat[0][1]: final_stat[1][1]}
    answer_2 = calculate_wins(final_game)

    print(answer_2)
