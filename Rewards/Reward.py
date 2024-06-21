from enum import Enum

class RewardStatus(Enum):
    PURCHASED = 1,
    NOT_PURCHASED = 2,
    NO_MONEY = 3


class Reward:
    def __init__(self) -> None:
        self.price = None
        self.name = None
        self.description = None

    def draw(self, terminal, status: RewardStatus) -> None:
        self.x = 0
        self.y = 0


        box_length = len(self.name) + 6
        color = terminal.yellow
        if status == RewardStatus.PURCHASED:
            color = terminal.green
        elif status == RewardStatus.NOT_PURCHASED:
            color = terminal.yellow
        else:
            color = terminal.red

        print(terminal.move_xy(0, 0) + color(" " + "-"*box_length))
        print(terminal.move_xy(0, 1) + color("|" + " "*len(self.name) + self.name + " "*len(self.name) + "|" ))
        print(terminal.move_xy(0, 2) + color(" " + "-"*box_length))

