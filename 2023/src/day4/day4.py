from collections import defaultdict

with open("input2") as f:
    data = f.read().strip().split("\n")

    total_score = 0
    total_cards = 0
    instance_counter = defaultdict(int)
    cards = []

    for index, line in enumerate(data):
        i = line.index("|")
        j = line.index(": ")

        a, b, c = line[:j], line[j + 1 : i].split(" "), line[i + 1 :].split(" ")

        b = [int(x) for x in b if x.isdigit()]
        c = [int(x) for x in c if x.isdigit()]
        winners = [i for i in b if i in c]

        score = 1

        if len(winners) > 1:
            for _ in range(len(winners) - 1):
                score *= 2
        if len(winners) == 0:
            score = 0
        if len(winners) == 1:
            score = 1

        total_score += score

    # part 2 attempt
    #
    # values = [index + x + 1 for x in range(1, len(winners) + 1)]
    #     cards.append(values)
    #
    #     if index > 0:
    #         values = values * len(winners)
    #
    # for i, j in enumerate(cards):
    #     if j in cards[i - 1] and i > 0:
    #         j *= len(cards[i - 1])
    #         print(j)
    # for j in range(1, len(winners) + 1):
    #     row = index + 1 + j
    #     instance_counter[row] += 1
    #     cards.append(row)
    # print(cards)
    # if len(winners) > 0:
    #     total_cards += (instance_counter[index + 1] + 1) * len(winners)
    # else:
    #     total_cards += instance_counter[index + 1] + 1
    #

    # card 1 = 1 instance = four matches = 1 copy of the next 4 cards = 4
    # card 2 = 2 instances = 2 matches each (4 matches) = 4 cards
    # card 3 = 4 instances = 2 matches each (8 matches) = 8 cards
    # card 4 = 8 instances = 1 match each (8 matches) = 8 cards
    # card 5 = 14 instances = 0 matches = 14 cards
    # card 6 = 1 instance = 0 matches = 1 card
