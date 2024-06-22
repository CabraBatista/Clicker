from Rewards.Reward import Reward, RewardStatus


class CarrierAntReward(Reward):
    def __init__(self) -> None:
        super().__init__()
        self.price = 20
        self.name = "Carrier Ant"
        self.description = ""
        

    def apply_reward(self, clicker) -> bool:
        if clicker.points >= self.price:
            clicker.points -= self.price
            self.reward_status = RewardStatus.PURCHASED
            self.price += round(self.price / 100 * 35)
            hormigas = round(clicker.biter_ant / 100 * 15)    
            if hormigas == 0: 
                self.amount += 1
            else:
                self.amount += hormigas
        else:
            self.reward_status = RewardStatus.NO_MONEY

        self.start_purchased_timer()
        return self.reward_status == RewardStatus.PURCHASED
