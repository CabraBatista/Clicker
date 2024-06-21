import blessed


from Rewards.Reward import Reward, RewardStatus


class BagReward(Reward):
    def __init__(self) -> None:
        self.price = 10
        self.name = "Bag"
        self.description = ""
        self.reward_status = RewardStatus.NOT_PURCHASED

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.max_load += 5
            clicker.points -= self.price
            self.reward_status = RewardStatus.PURCHASED
            self.draw(clicker.terminal, self.reward_status)
        else:
            self.reward_status = RewardStatus.NO_MONEY

        self.draw(clicker.terminal, self.reward_status)
        return self.reward_status == RewardStatus.PURCHASED
