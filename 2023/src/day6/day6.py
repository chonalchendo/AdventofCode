import math

with open("input") as f:
    data = f.read().strip().split("\n")

    stats = []

    for index, line in enumerate(data):
        stat = [x for x in line.split(" ") if x.strip()]
        stats.append(stat)

    games = dict(zip(stats[0][1:], stats[1][1:]))
    games["95"] = stats[1][-2]

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

    answer = math.prod(counts)

    # part 1
    print(answer)
