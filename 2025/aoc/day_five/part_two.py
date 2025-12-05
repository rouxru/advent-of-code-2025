from aoc.api import get_data

TEST = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
]


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/5/input")
    # instructions = TEST

    split_idx = instructions.index("")
    ranges = []
    for line in instructions[:split_idx]:
        s, e = line.split("-")
        ranges.append((int(s), int(e)))

    ranges.sort()

    merged_ranges = []
    for start, end in ranges:
        if not merged_ranges or start > merged_ranges[-1][1] + 1:
            merged_ranges.append([start, end])
        else:
            merged_ranges[-1][1] = max(merged_ranges[-1][1], end)

    total = sum(end - start + 1 for start, end in merged_ranges)
    return total


if __name__ == "__main__":
    main()
