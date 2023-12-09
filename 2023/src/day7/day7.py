from collections import Counter


def card_values():
    values = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    return dict(zip(values, range(2, 15)))


def translate_hand(hand: str):
    card_value = card_values()
    return [card_value[card] for card in hand]


def sort_hands(hand):
    return sorted(hand.items(), key=lambda x: x[1], reverse=True)


def main():
    with open("input") as f:
        data = f.read().strip().split("\n")
        df = [hand.split(" ") for hand in data]

        hands_bids = {hand: int(bid) for hand, bid in df}

        total_count = []
        for hand in hands_bids.keys():
            value_count = [char for char in hand]
            count = Counter(value_count)
            total_count.append({hand: count})

        five_kind = {}
        four_kind = {}
        full_house = {}
        three_kind = {}
        two_pair = {}
        one_pair = {}
        high_card = {}

        for handpair in total_count:
            for hand, count in handpair.items():
                values = [value for _, value in count.items()]
                if 5 in values:
                    five_kind.update({hand: translate_hand(hand)})
                if 4 in values:
                    four_kind.update({hand: translate_hand(hand)})
                if 3 in values and 2 in values:
                    full_house.update({hand: translate_hand(hand)})
                if 3 in values and 2 not in values:
                    three_kind.update({hand: translate_hand(hand)})
                if values.count(2) == 2:
                    two_pair.update({hand: translate_hand(hand)})
                if values.count(2) == 1 and 3 not in values:
                    one_pair.update({hand: translate_hand(hand)})
                if values.count(1) == 5:
                    high_card.update({hand: translate_hand(hand)})

    five_kind = sort_hands(five_kind)
    four_kind = sort_hands(four_kind)
    full_house = sort_hands(full_house)
    three_kind = sort_hands(three_kind)
    two_pair = sort_hands(two_pair)
    one_pair = sort_hands(one_pair)
    high_card = sort_hands(high_card)

    winning_list = (
        [*five_kind]
        + [*four_kind]
        + [*full_house]
        + [*three_kind]
        + [*two_pair]
        + [*one_pair]
        + [*high_card]
    )

    score = 0
    for i, hand in enumerate(reversed(winning_list), start=1):
        score += hands_bids[hand[0]] * i

    print(score)


if __name__ == "__main__":
    main()
