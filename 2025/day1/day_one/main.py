from enum import StrEnum
from dataclasses import dataclass
from pathlib import Path


INPUT = Path("./input.txt").resolve()
TEST_INPUT = Path("./test_input.txt").resolve()


class Direction(StrEnum):
    LEFT = "left"
    RIGHT = "right"


@dataclass
class DialInstruction:
    direction: Direction
    movement: int


class DialState:
    def __init__(self) -> None:
        self._current_number: int = 50  # 0-99
        self._zero_counter: int = 0

    def turn_dial(self, direction: Direction, num: int):
        num = num % 100
        match direction:
            case Direction.LEFT:
                curr = self._turn_left(num)
                if curr == 0:
                    self._zero_counter += 1
            case Direction.RIGHT:
                curr = self._turn_right(num)
                if curr == 0:
                    self._zero_counter += 1

    def _turn_left(self, num: int):
        if self._current_number - num < 0:
            self._current_number = self._current_number - num + 100
            return self._current_number

        self._current_number -= num
        return self._current_number

    def _turn_right(self, num: int):
        if self._current_number + num > 99:
            self._current_number = self._current_number + num - 100
            return self._current_number

        self._current_number += num
        return self._current_number


def read_input(path: Path):
    with open(path, "r") as f:
        data = f.read().splitlines()
    return data


def _get_direction(data: str) -> Direction:
    dir: Direction
    match data[0]:
        case "L":
            dir = Direction.LEFT
        case "R":
            dir = Direction.RIGHT
        case _:
            raise ValueError(f"Unexpected instruction: {data}")
    return dir


def _get_count(data: str) -> int:
    return int(data[1::])


def parse_input(data: list[str]) -> list[DialInstruction]:
    resp = []
    for ele in data:
        dir = _get_direction(ele)
        count = _get_count(ele)
        resp.append(DialInstruction(dir, count))

    return resp


def main():
    data = read_input(INPUT)
    parsed_data = parse_input(data)
    dial_state = DialState()

    for ele in parsed_data:
        dial_state.turn_dial(ele.direction, ele.movement)
    print(dial_state._zero_counter)


if __name__ == "__main__":
    main()
