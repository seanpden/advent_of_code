from enum import StrEnum
from dataclasses import dataclass
from pathlib import Path


INPUT = Path("./input.txt").resolve()
TEST_INPUT = Path("./test_input.txt").resolve()


class Direction(StrEnum):
    LEFT = "left"
    RIGHT = "left"


@dataclass
class DialInstruction:
    direction: Direction
    movement: int


class DialState:
    def __init__(self) -> None:
        self._current_number: int = 50  # 0-99

    def turn_left(self, num: int):
        if self._current_number - num < 0:
            self._current_number = 99 - ((num - 1) - self._current_number)
            return

        self._current_number -= num

    def turn_right(self, num: int):
        if self._current_number + num > 99:
            self._current_number = self._current_number + num - 100
            return self._current_number

        self._current_number += num


def read_input(path: Path):
    with open(path, "r") as f:
        data = f.read()
    return data


def parse_input(data: str) -> list[DialInstruction]:
    raise NotImplementedError


def main():
    data = read_input(TEST_INPUT)
    print(data)
    dial_state = DialState()


if __name__ == "__main__":
    main()
