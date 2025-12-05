from dataclasses import dataclass
from pathlib import Path
from readline import parse_and_bind
from typing import Callable


INPUT = Path("./input.txt").resolve()


@dataclass(frozen=True)
class IdRange:
    start: int
    end: int

    @staticmethod
    def from_string(s: str) -> "IdRange":
        if not s or "-" not in s:
            raise ValueError(f"Invalid instruction format: {s}")

        split_s = s.split("-")

        return IdRange(int(split_s[0]), int(split_s[1]))


def invalid_id_part_one(n: int):
    len_ele = len(str(n))
    if not len_ele % 2 == 0:
        return False
    midpoint = len_ele // 2
    first_half = str(n)[0:midpoint]
    second_half = str(n)[midpoint::]
    if not first_half == second_half:
        return False
    return True


def invalid_id_part_two(n: int):
    s = str(n)
    s_twice = s + s
    return s_twice.find(s, 1) != len(s)


def summer(id_ranges: list[IdRange], mthd: Callable[[int], bool]):
    sum = 0

    # every range in input
    for id_range in id_ranges:  # every range
        # every id in range
        for ele in range(id_range.start, id_range.end + 1):
            if mthd(ele):
                sum += ele

    return sum


def read_input(path: Path) -> list[str]:
    return path.read_text().split(",")


def parse_input(data: list[str]) -> list[IdRange]:
    return [IdRange.from_string(ele) for ele in data]


def main():
    # Parse ranges
    # iterate between each range
    # 55, 6464, 123123 -> pattern matching
    # sum of invalid IDs
    input = read_input(INPUT)
    parsed_input = parse_input(input)

    part_one_sum = summer(parsed_input, invalid_id_part_one)
    print(f"Part 1: {part_one_sum}")
    part_two_sum = summer(parsed_input, invalid_id_part_two)
    print(f"Part 2: {part_two_sum}")


if __name__ == "__main__":
    main()
