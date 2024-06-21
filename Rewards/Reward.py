from enum import Enum
import threading

class RewardStatus(Enum):
    PURCHASED = 1,
    NOT_PURCHASED = 2,
    NO_MONEY = 3


class Reward:
    def __init__(self) -> None:
        self.price = None
        self.name = None
        self.description = None
        self.reward_status = RewardStatus.NOT_PURCHASED

    def draw(self, terminal, reward_number) -> None:
        box_length = len(self.name)*3
        color = terminal.yellow
        if self.reward_status == RewardStatus.PURCHASED:
            color = terminal.green
        elif self.reward_status == RewardStatus.NO_MONEY:
            color = terminal.red

        print(terminal.move_xy(reward_number * 20, 0) + color(" " + "-"*box_length))
        print(terminal.move_xy(reward_number * 20, 1) + color("|" + " "*len(self.name) + self.name + " "*len(self.name) + "|" ))
        print(terminal.move_xy(reward_number * 20, 2) + color(" " + "-"*box_length))

    
    def set_not_purchased(self):
        self.reward_status = RewardStatus.NOT_PURCHASED

    def start_purchased_timer(self):
        timer = threading.Timer(1.0, self.set_not_purchased)
        timer.start()

