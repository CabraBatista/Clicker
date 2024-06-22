#!/usr/bin/fades

import blessed # fades
import time

from Rewards.BagReward import BagReward
from Rewards.AnthillReward import AnthillReward
from Rewards.BiterAntReward import BiterAntReward
from Rewards.CarrierAntReward import CarrierAntReward

TERMINAL = blessed.Terminal()


def debug(*textos):
    with open("/tmp/debugblessed.txt", "at") as fh:
        fh.write(f"{time.ctime()} {' '.join(map(str, textos))}\n")


class Clicker:
    def __init__(self):

        self.draws_size_x = 120
        self.draws_size_y = 9

        self.draw_base_hormiguero_x = int((TERMINAL.width - self.draws_size_x) / 2)
        self.draw_base_hormiguero_y = int((TERMINAL.height - self.draws_size_y) / 2)

        self.ant_x = 11
        self.ant_y = -5
        self.food = 0
        self.terminal = TERMINAL
        self.load = 0
        self.points = 0
        self.max_load = 1
        self.biter_ant = 0
        self.anthills = 1
        self.biter_ant_reward = BiterAntReward()
        self.carrier_ant_reward = CarrierAntReward()
        self.rewards = []
        self.rewards.append(BagReward())
        self.rewards.append(self.biter_ant_reward)
        self.rewards.append(self.carrier_ant_reward)
        self.rewards.append(AnthillReward())

        self.base_time = time.time()

    def draw(self):
        print(TERMINAL.clear())
        
        print(TERMINAL.move_xy(self.ant_x + self.draw_base_hormiguero_x,self.ant_y + self.draw_base_hormiguero_y,)
            + TERMINAL.orangered4("█") + TERMINAL.sienna("█"))

        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 7, self.draw_base_hormiguero_y - 8)   
            + TERMINAL.goldenrod1(TERMINAL.bold("COINS:" + str(self.points))))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 100, self.draw_base_hormiguero_y - 7)
            + TERMINAL.limegreen(".\^/."))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 97, self.draw_base_hormiguero_y - 6)
            + TERMINAL.limegreen("'. |`|/| ."))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 97, self.draw_base_hormiguero_y - 5)
            + TERMINAL.limegreen("'|\|\|'|/|"))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 95, self.draw_base_hormiguero_y - 4)
            + TERMINAL.limegreen(".--'-\`|/-''--."))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 96, self.draw_base_hormiguero_y - 3)
            + TERMINAL.limegreen("\`-._\|./.-'/"))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 97, self.draw_base_hormiguero_y - 2)
            + TERMINAL.limegreen(">`-._|/.-'<"))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 96, self.draw_base_hormiguero_y - 1)
            + TERMINAL.limegreen("'~|/~~|~~\|~'"))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 102, self.draw_base_hormiguero_y)
            + TERMINAL.limegreen("|"))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 91, self.draw_base_hormiguero_y - 9)
            + TERMINAL.bold(TERMINAL.limegreen("[SPACE] to byte the Leaf")))

        self.draw_anthills()
        self.draw_rewards()
        self.draw_points()

        self.draw_rewards()
        self.draw_baiter_ants()



        if self.food > 0:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 92, self.draw_base_hormiguero_y - 1)
                + TERMINAL.forestgreen("█")+ TERMINAL.move_xy(self.draw_base_hormiguero_x + 91, self.draw_base_hormiguero_y - 2)
                + TERMINAL.forestgreen("x" + str(int(self.food))))
        if self.load > 0:
            print(TERMINAL.move_xy(self.ant_x + self.draw_base_hormiguero_x,self.draw_base_hormiguero_y + self.ant_y - 1,)
                + TERMINAL.forestgreen("█"))
            print(TERMINAL.move_xy(self.ant_x + self.draw_base_hormiguero_x,self.draw_base_hormiguero_y + self.ant_y - 2,)
                + str(self.load))


    def draw_rewards(self):
        for i, reward in enumerate(self.rewards):
            reward.draw(self.terminal, i)


    def draw_anthills(self):
        for i in range(self.anthills):
            self.draw_anthill(i)

    def draw_anthill(self, anthill_number = 0):
        base = self.draw_base_hormiguero_y - anthill_number * 7
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, base - 4) + "       _/======\_" )
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, base - 3) + "     _/          \__" )
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, base - 2) + "   _/               \_" )
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, base - 1) + "  /                   \__")
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, base) +     " /                       \==============---------==========------===----------===========##===" )
        
    def on_update(self):
        #Baiter Ants Function
        new_time = time.time()
        delta_t = new_time - self.base_time
        self.base_time = new_time

        rate = self.biter_ant_reward.amount / 10
        self.food += rate * delta_t
        debug("Delta T:", delta_t, "Self.Food:", self.food)

        #Carrier Ant
        

    def loop(self):
        with TERMINAL.cbreak():
            val = ""
            while val.lower() != "k":
                self.draw()
                self.on_update()

                val = TERMINAL.inkey(timeout=0.5)
                if val.lower() == " ":
                    if self.can_bite_leaf():
                        self.food += 1
                elif val.lower() == "d":
                    if self.ant_x != 89:
                        self.ant_x += 1
                        self.walk()
                elif val.lower() == "a":
                    if self.ant_x != 11:
                        self.ant_x -= 1
                        self.walk()
                elif val.lower() == "e":
                    if self.ant_x == 89:
                        self.load_food()
                    else:
                        self.drop_food()   
                elif val.lower() == "1":
                    if not self.rewards[0].apply_reward(self):
                        continue
                elif val.lower() == "2":
                    if not self.rewards[1].apply_reward(self):
                        continue
                elif val.lower() == "3":
                    if not self.rewards[2].apply_reward(self):
                        continue
                #elif val.lower() == "4":
                 #   if not self.rewards[3].apply_reward(self):
                  #      continue

                self.draw_base_hormiguero_x = int((TERMINAL.width - self.draws_size_x) / 2)
                self.draw_base_hormiguero_y = int((TERMINAL.height - self.draws_size_y) / 6 * 5)


                

        print(TERMINAL.clear())

    def can_bite_leaf(self):
        return self.ant_x == 89

    def can_load_food(self):
        return (
            self.ant_y == -1
            and self.load < self.max_load
            and self.food >= 1
)

    def load_food(self):
        if self.can_load_food():
            self.load += 1
            self.food -= 1

    def can_drop_food(self):
        return (self.load > 0 and self.ant_x > 10 and self.ant_x < 16 and self.ant_y == -5)

    def drop_food(self):
        if self.can_drop_food():
            if self.load + self.points > 500:
                self.load -= (self.load + self.points) - 500

            self.points += self.load
            self.load = 0

    def draw_points(self):

        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 6, self.draw_base_hormiguero_y - 8)
                + TERMINAL.goldenrod1(TERMINAL.bold(f"COINS: {self.points}")))
        
        almacenamiento = [
            (0, 3, 0, TERMINAL.forestgreen("█")),
            (8, 4, 0, TERMINAL.webgreen("█")),
            (16, 5, 0, TERMINAL.green3("█")),
            (24, 6, 0, TERMINAL.forestgreen("█")),
            (32, 7, 0, TERMINAL.webgreen("█")),
            (40, 8, 0, TERMINAL.forestgreen("█")),
            (48, 9, 0, TERMINAL.webgreen("█")),
            (56, 10, 0, TERMINAL.webgreen("█")),
            (64, 11, 0, TERMINAL.forestgreen("█")),
            (72, 12, 0, TERMINAL.green3("█")),
            (80, 13, 0, TERMINAL.webgreen("█")),
            (88, 14, 0, TERMINAL.forestgreen("█")),
            (96, 15, 0, TERMINAL.forestgreen("█")),
            (104, 16, 0, TERMINAL.green3("█")),
            (112, 17, 0, TERMINAL.webgreen("█")),
            (120, 18, 0, TERMINAL.forestgreen("█")),
            (128, 19, 0, TERMINAL.green3("█")),
            (136, 20, 0, TERMINAL.green3("█")),
            (144, 21, 0, TERMINAL.green3("█")),
            (152, 22, 0, TERMINAL.forestgreen("█")),
            (160, 23, 0, TERMINAL.webgreen("█")),
           
            (168, 4, -1, TERMINAL.forestgreen("█")),
            (176, 5, -1, TERMINAL.green3("█")),
            (185, 6, -1, TERMINAL.webgreen("█")),
            (193, 7, -1, TERMINAL.green3("█")),
            (201, 8, -1, TERMINAL.webgreen("█")),
            (209, 9, -1, TERMINAL.webgreen("█")),
            (217, 10, -1, TERMINAL.green3("█")),
            (225, 11, -1, TERMINAL.forestgreen("█")),
            (233, 12, -1, TERMINAL.green3("█")),
            (241, 13, -1, TERMINAL.webgreen("█")),
            (249, 14, -1, TERMINAL.forestgreen("█")),
            (257, 15, -1, TERMINAL.webgreen("█")),
            (265, 16, -1, TERMINAL.forestgreen("█")),
            (273, 17, -1, TERMINAL.green3("█")),
            (281, 18, -1, TERMINAL.green3("█")),
            (289, 19, -1, TERMINAL.green3("█")),
            (297, 20, -1, TERMINAL.webgreen("█")),
            
            (305, 6, -2, TERMINAL.green3("█")),
            (313, 7, -2, TERMINAL.forestgreen("█")),
            (321, 8, -2, TERMINAL.green3("█")),
            (328, 9, -2, TERMINAL.forestgreen("█")),
            (337, 10, -2, TERMINAL.webgreen("█")),
            (345, 11, -2, TERMINAL.webgreen("█")),
            (353, 12, -2, TERMINAL.webgreen("█")),
            (361, 13, -2, TERMINAL.green3("█")),
            (369, 14, -2, TERMINAL.forestgreen("█")),
            (377, 15, -2, TERMINAL.forestgreen("█")),
            (385, 16, -2, TERMINAL.webgreen("█")),
            (393, 17, -2, TERMINAL.green3("█")),
            (401, 18, -2, TERMINAL.webgreen("█")),

            (409, 8, -3, TERMINAL.forestgreen("█")),
            (417, 9, -3, TERMINAL.forestgreen("█")),
            (425, 10, -3, TERMINAL.webgreen("█")),
            (433, 11, -3, TERMINAL.webgreen("█")),
            (441, 12, -3, TERMINAL.forestgreen("█")),
            (449, 13, -3, TERMINAL.webgreen("█")),
            (457, 14, -3, TERMINAL.green3("█")),
            (465, 15, -3, TERMINAL.green3("█")),
        ]
        
        for limit, x, y, char in almacenamiento:
            if self.points > limit:
                print(TERMINAL.move_xy(self.draw_base_hormiguero_x + x, self.draw_base_hormiguero_y + y) + char)
        
    def draw_baiter_ants(self):
        almacenamiento = [
            (0, 106, -7, TERMINAL.darkorange4("o")),
            (5, 110, -4, TERMINAL.orange4("o")),
            (10, 94, -5, TERMINAL.sienna("o")),
            (15, 112, -1, TERMINAL.darkorange4("o")),
            (25, 104, 0, TERMINAL.orange4("o")),
            (35, 94, -3, TERMINAL.sienna("o")),
            (45, 97, 0, TERMINAL.darkorange4("o")),
            (55, 97, -8, TERMINAL.orange4("o")),
            (70, 110, 1, TERMINAL.sienna("o")),
            (85, 111, -6, TERMINAL.darkorange4("o")),
            (100, 115, -3, TERMINAL.orange4("o")),
            (115, 103, 2, TERMINAL.sienna("o")),
            (135, 91, -4, TERMINAL.darkorange4("o")),
            (155, 109, -8, TERMINAL.orange4("o")),
            (175, 104, -5, TERMINAL.sienna("o")),
            (195, 100, -2, TERMINAL.darkorange4("o")),
            (220, 99, -4, TERMINAL.orange4("o")),
            (245, 105, -3, TERMINAL.sienna("o")),
            (275, 93, -7, TERMINAL.darkorange4("o")),
            (300, 100, -6, TERMINAL.orange4("o")),
            (330, 102, -8, TERMINAL.sienna("o ")),
            
        ]

        for limit, x, y, char in almacenamiento:
            if self.biter_ant_reward.amount > limit:
                print(TERMINAL.move_xy(self.draw_base_hormiguero_x + x, self.draw_base_hormiguero_y + y) + char)

    def walk(self):
        if self.ant_x >= 10 and self.ant_x <= 16:
            self.ant_y = -5
        elif self.ant_x >= 17 and self.ant_x <= 19:
            self.ant_y = -4
        elif self.ant_x >= 20 and self.ant_x <= 21:
            self.ant_y = -3
        elif self.ant_x >= 22 and self.ant_x <= 24:
            self.ant_y = -2
        else:
            self.ant_y = -1


clicker = Clicker()
clicker.loop()
