from main import (
    invalid_id_part_one,
    invalid_id_part_two,
    main,
    IdRange,
    parse_input,
    summer,
)


def test_main():
    assert True


def test_with_simple():
    # Parse ranges
    # iterate between each range
    # 55, 6464, 123123 -> pattern matching
    # sum of invalid IDs
    input: str = """11-22,95-115,998-1012,1188511880-1188511890,222220-222224, 1698522-1698528,446443-446449,38593856-38593862,565653-565659, 824824821-824824827,2121212118-2121212124"""
    # input: str = """95-115"""

    print()
    input = input.split(",")

    parsed_input = parse_input(input)

    p1sum = summer(parsed_input, invalid_id_part_one)
    p2sum = summer(parsed_input, invalid_id_part_two)

    print("part one Sum:", p1sum)
    print("part two Sum:", p2sum)
