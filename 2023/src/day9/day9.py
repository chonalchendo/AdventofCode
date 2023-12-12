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
        count += 1
        data.append(seq_cal)
    return data


def add_extrapolate(data: list[list[int]]):
    result = [seq[-1] for seq in data]
    return sum(result)


def part_1(data: list[list[int]]) -> int:
    solved = solver(data)
    return add_extrapolate(solved)


with open("input") as f:
    data = create_data(f)

    # part 1
    part_1_ans = [part_1([seq]) for seq in data]
    print(sum(part_1_ans))

    part_2_ans = [part_1([seq[::-1]]) for seq in data]
    print(sum(part_2_ans))
