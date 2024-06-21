from Rewards.Reward import Reward, RewardStatus


class BiterAntReward(Reward):
    def __init__(self) -> None:
        super().__init__()
        self.price = 20
        self.name = "Biter Ant"
        self.description = ""
        

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.points -= self.price
            self.amount += 1
            self.reward_status = RewardStatus.PURCHASED
            hormigas = round(clicker.biter_ant / 100 * 15)
            if hormigas == 0:
                clicker.biter_ant += 1
            else:
                clicker.biter_ant += hormigas
            self.price += round(self.price / 100 * 35)
        else:
            self.reward_status = RewardStatus.NO_MONEY

        self.start_purchased_timer()
        return self.reward_status == RewardStatus.PURCHASED
