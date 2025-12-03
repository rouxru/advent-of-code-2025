from aoc.api import get_data


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/3/input")

    joltage_sum = 0
    for bank in instructions:
        keep = 12
        remove = len(bank) - keep
        stack = []

        for battery in bank:
            while stack and remove and battery > stack[-1]:
                stack.pop()
                remove -= 1
            stack.append(battery)

        stack = stack[:keep]

        joltage_sum += int("".join(stack))

    print(joltage_sum)


if __name__ == "__main__":
    main()
