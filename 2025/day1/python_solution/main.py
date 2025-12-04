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
    def __init__(self, any_click: bool = False) -> None:
        self.position: int = 50  # 0-99
        self.zero_count: int = 0
        self.any_click: bool = any_click

    def turn_dial(self, instruction: DialInstruction) -> None:
        match instruction.direction:
            case Direction.LEFT:
                # pos-1 -> Shift boundary for floor
                # (pos - 1) // 100 -> Which bucket are we in
                # (pos-1)-1, (pos-1)-2, ..., (pos-1)-clicks -> Ending position with shift
                # ((pos - 1) - clicks) // 100 -> Which bucket is the ending pos in
                # ((P - 1) // 100) - ((P - 1 - M) // 100) -> Start - End
                if self.any_click:
                    self.zero_count += (self.position - 1) // 100 - (
                        self.position - 1 - instruction.movement
                    ) // 100
                self.position = self.position - instruction.movement
            case Direction.RIGHT:
                # pos+1, pos+2, ..., pos+clicks -> how many clicks to move
                # (pos + clicks) // 100 -> How many group of 100 in ending position
                # pos // 100 -> how many complete groups of 100 in position
                # ((P + M) // 100) - (P // 100) -> End position 100 groupings - current groupings
                if self.any_click:
                    self.zero_count += (
                        self.position + instruction.movement
                    ) // 100 - self.position // 100
                self.position = self.position + instruction.movement

        self.position = self.position % 100

        if not self.any_click and self.position == 0:
            self.zero_count += 1


def read_input(path: Path) -> list[str]:
    return path.read_text().splitlines()


def parse_input(data: list[str]) -> list[DialInstruction]:
    return [DialInstruction.from_string(ele) for ele in data]


def main():
    dial_state = DialState(True)

    data = read_input(INPUT)
    parsed_data = parse_input(data)

    for ele in parsed_data:
        dial_state.turn_dial(ele)

    print("Password: ", dial_state.zero_count)


if __name__ == "__main__":
    main()
