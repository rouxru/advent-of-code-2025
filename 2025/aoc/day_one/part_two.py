from aoc.api import get_data


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/1/input")
    dial = [num for num in range(0, 100)]
    dial_pointer = dial.index(50)
    password = 0

    for instruction in instructions:
        direction = instruction[0]
        clicks = int(instruction[1:])

        for _ in range(clicks):
            if dial_pointer == 0:
                password += 1

            if direction == "L":
                if dial_pointer == 0:
                    dial_pointer = len(dial) - 1
                else:
                    dial_pointer -= 1
            else:
                if dial_pointer == len(dial) - 1:
                    dial_pointer = 0
                else:
                    dial_pointer += 1

    return password


if __name__ == "__main__":
    main()
