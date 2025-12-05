from aoc.api import get_data


def main():
    instructions = get_data(url="https://adventofcode.com/2025/day/5/input")
    split_idx = instructions.index("")
    ingredient_ids_ranges = [id.split("-") for id in instructions[:split_idx]]
    available_ingredient_ids = instructions[split_idx + 1 :]

    fresh_ingredients_counter = 0

    for id in available_ingredient_ids:
        if any(
            int(id) >= int(start) and int(id) <= int(end)
            for start, end in ingredient_ids_ranges
        ):
            fresh_ingredients_counter += 1

    return fresh_ingredients_counter


if __name__ == "__main__":
    main()
