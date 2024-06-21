from Rewards.Reward import Reward, RewardStatus


class AnthillReward(Reward):
    def __init__(self) -> None:
        super().__init__()
        self.price = 15
        self.name = "Anthill"
        self.description = ""
        

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.points -= self.price
            clicker.anthills += 1
            self.reward_status = RewardStatus.PURCHASED
        else:
            self.reward_status = RewardStatus.NO_MONEY

        self.start_purchased_timer()
        return self.reward_status == RewardStatus.PURCHASED
