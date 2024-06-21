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
        self.amount = 0

    def draw(self, terminal, reward_number) -> None:
        box_length = 25
        color = terminal.yellow
        if self.reward_status == RewardStatus.PURCHASED:
            color = terminal.green
        elif self.reward_status == RewardStatus.NO_MONEY:
            color = terminal.red

        amount_price = "$:" + str(self.price) + "  Amount:" + str(self.amount)

        print(terminal.move_xy(reward_number * 32, 0) + color(" " + "-"*box_length))
        print(terminal.move_xy(reward_number * 32, 1) + color("|" + self.name.center(box_length) + "|" ))
        print(terminal.move_xy(reward_number * 32, 2) + color(" " + "-"*box_length))
        print(terminal.move_xy(reward_number * 32, 3) + color(amount_price.center(box_length)))

    
    def set_not_purchased(self):
        self.reward_status = RewardStatus.NOT_PURCHASED

    def start_purchased_timer(self):
        timer = threading.Timer(1.0, self.set_not_purchased)
        timer.start()

