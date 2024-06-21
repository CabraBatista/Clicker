from Rewards.Reward import Reward, RewardStatus


class BagReward(Reward):
    def __init__(self) -> None:
        super().__init__()
        self.price = 5
        self.name = "Bag"
        self.description = ""
        

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.max_load += 5
            clicker.points -= self.price
            self.reward_status = RewardStatus.PURCHASED
        else:
            self.reward_status = RewardStatus.NO_MONEY

        self.start_purchased_timer()
        return self.reward_status == RewardStatus.PURCHASED
