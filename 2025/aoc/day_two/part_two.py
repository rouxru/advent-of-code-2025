from aoc.api import get_data


def is_invalid_repetition(str_num: str) -> bool:
    length = len(str_num)
    for block_size in range(1, length):
        if length % block_size == 0:
            repeat_count = length // block_size

            if repeat_count >= 2:
                block = str_num[:block_size]
                if block * repeat_count == str_num:
                    return True

    return False


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/2/input")
    instructions = instructions[0].split(",")

    invalid_ids = []
    for id_range in instructions:
        range_start, range_end = id_range.split("-")
        range_start, range_end = int(range_start), int(range_end)

        for num in range(range_start, range_end + 1):
            str_num = str(num)

            if is_invalid_repetition(str_num):
                invalid_ids.append(num)

    return print(sum(invalid_ids))


if __name__ == "__main__":
    main()
