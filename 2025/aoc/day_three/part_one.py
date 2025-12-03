from aoc.api import get_data


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/3/input")

    joltage_sum = 0
    for bank in instructions:
        first_highest_battery_str = max(bank[: len(bank) - 1])
        first_highest_index = bank.index(first_highest_battery_str)
        second_highest_battery = int(bank[-1])

        for battery in bank[first_highest_index + 1 :]:
            battery_int = int(battery)
            if second_highest_battery < battery_int:
                second_highest_battery = battery_int

        joltage_sum += int(first_highest_battery_str + str(second_highest_battery))
    return joltage_sum


if __name__ == "__main__":
    main()
