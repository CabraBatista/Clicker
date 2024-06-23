from Rewards.Reward import Reward, RewardStatus


class BagReward(Reward):
    def __init__(self) -> None:
        super().__init__()
        self.price = 10
        self.name = "Bag"
        self.description = ""
        

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.points -= self.price
            self.amount += 1
            self.reward_status = RewardStatus.PURCHASED
            más_espacio = round(clicker.max_load / 100 * 35)
            if más_espacio == 0:
                clicker.max_load += 1
            else:
                clicker.max_load += más_espacio
            self.price += round(self.price / 100 * 32)
        else:
            self.reward_status = RewardStatus.NO_MONEY

        self.start_purchased_timer()
        return self.reward_status == RewardStatus.PURCHASED
