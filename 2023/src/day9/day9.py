def create_data(file):
    data = file.read().splitlines()
    return [[int(value) for value in line.split()] for line in data]


def solver(data: list[list[int]]):
    data = data.copy()
    count = 0
    while sum(data[-1]) != 0 or data[-1][-1] != 0:
        seq_cal = []
        for x in range(len(data[count])):
            if x != 0:
                diff = data[count][x] - data[count][x - 1]
                seq_cal.append(diff)
        print(seq_cal)
        count += 1
        data.append(seq_cal)
    return data


def calculate_next_seq(data: list[list[int]]):
    add_numbers = [seq[-1] for seq in data]
    return sum(add_numbers)


def part_1(data) -> int:
    solved = solver(data)
    total = calculate_next_seq(solved)
    return total


with open("input") as f:
    data = create_data(f)

    # part 1
    answer = [part_1([seq]) for seq in data]
    print(sum(answer))
