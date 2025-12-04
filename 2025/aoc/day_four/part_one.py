from aoc.api import get_data


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/4/input")
    instructions = [list(row) for row in instructions]

    total_removed = 0
    valid_paper_rolls_count = 0
    paper_roll_col = -1
    paper_roll_row = -1

    while True:
        to_remove = []
        for i, row in enumerate(instructions):
            for j, col in enumerate(row):
                if col == "@":
                    paper_roll_row = i
                    paper_roll_col = j

                    neighbor_paper_rolls_count = 0
                    for r, c in [
                        [paper_roll_row - 1, paper_roll_col - 1],
                        [paper_roll_row - 1, paper_roll_col],
                        [paper_roll_row - 1, paper_roll_col + 1],
                        [paper_roll_row, paper_roll_col - 1],
                        [paper_roll_row, paper_roll_col + 1],
                        [paper_roll_row + 1, paper_roll_col - 1],
                        [paper_roll_row + 1, paper_roll_col],
                        [paper_roll_row + 1, paper_roll_col + 1],
                    ]:
                        if r >= 0 and c >= 0 and r < len(row) and c < len(row):
                            if instructions[r][c] == "@":
                                neighbor_paper_rolls_count += 1

                    if neighbor_paper_rolls_count < 4:
                        valid_paper_rolls_count += 1
                        to_remove.append((i, j))

        if not to_remove:
            break

        for r, c in to_remove:
            instructions[r][c] = "."
            total_removed += 1

    print(total_removed)


if __name__ == "__main__":
    main()
