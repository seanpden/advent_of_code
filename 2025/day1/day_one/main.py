from enum import StrEnum
from dataclasses import dataclass
from pathlib import Path


INPUT = Path("./input.txt").resolve()
TEST_INPUT = Path("./test_input.txt").resolve()


class Direction(StrEnum):
    LEFT = "left"
    RIGHT = "right"


@dataclass(frozen=True)
class DialInstruction:
    direction: Direction
    movement: int

    @staticmethod
    def from_string(s: str) -> "DialInstruction":
        if not s or len(s) < 2:
            raise ValueError(f"Invalid instruction format: {s}")

        match s[0]:
            case "L":
                direction = Direction.LEFT
            case "R":
                direction = Direction.RIGHT
            case invalid:
                raise ValueError(f"Unexpected instruction: {invalid}")

        movement = int(s[1:])
        return DialInstruction(direction, movement)


class DialState:
    def __init__(self) -> None:
        self.position: int = 50  # 0-99
        self.zero_count: int = 0

    def turn_dial(self, instruction: DialInstruction) -> None:
        num = instruction.movement % 100

        match instruction.direction:
            case Direction.LEFT:
                self.position = (self.position - num) % 100
            case Direction.RIGHT:
                self.position = (self.position + num) % 100

        if self.position == 0:
            self.zero_count += 1


def read_input(path: Path) -> list[str]:
    return path.read_text().splitlines()


def parse_input(data: list[str]) -> list[DialInstruction]:
    return [DialInstruction.from_string(ele) for ele in data]


def main():
    dial_state = DialState()

    data = read_input(INPUT)
    parsed_data = parse_input(data)

    for ele in parsed_data:
        dial_state.turn_dial(ele)

    print("Password: ", dial_state.zero_count)


if __name__ == "__main__":
    main()
