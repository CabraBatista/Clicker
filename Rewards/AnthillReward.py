from Rewards.Reward import Reward, RewardStatus


class AnthillReward(Reward):
    def __init__(self) -> None:
        super().__init__()
        self.price = 500
        self.name = "Anthill"
        self.description = ""
        

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.points -= self.price
            clicker.anthills += 1
            self.amount += 1
            self.reward_status = RewardStatus.PURCHASED
            if clicker.anthills < 8:
                self.price = clicker.anthills * 500
            else:
                self.price = "X"
        else:
            self.reward_status = RewardStatus.NO_MONEY

        clicker.price = self.price
        self.start_purchased_timer()
        return self.reward_status == RewardStatus.PURCHASED
