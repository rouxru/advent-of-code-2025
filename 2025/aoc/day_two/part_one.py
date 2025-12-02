from aoc.api import get_data


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/2/input")
    instructions = instructions[0].split(",")
    invalid_ids = []
    for id_range in instructions:
        range_start, range_end = id_range.split("-")
        range_start, range_end = int(range_start), int(range_end)

        for num in range(range_start, range_end + 1):
            str_num = str(num)
            if len(str_num) % 2 == 0:
                half = int(len(str_num) / 2)
                first_seq, second_seq = str_num[:half], str_num[half:]
                if first_seq == second_seq:
                    invalid_ids.append(num)

    return sum(invalid_ids)


if __name__ == "__main__":
    main()
