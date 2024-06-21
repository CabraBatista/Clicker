#!/usr/bin/fades

import blessed # fades
import time

from Rewards.BagReward import BagReward
from Rewards.AnthillReward import AnthillReward

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
        self.anthills = 1
        self.rewards = []
        self.rewards.append(BagReward())
        self.rewards.append(AnthillReward())
        debug("Arrancando")

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

        if self.food > 0:
            print(
                TERMINAL.move_xy(
                    self.draw_base_hormiguero_x + 92, self.draw_base_hormiguero_y - 1
                )
                + TERMINAL.forestgreen("█")
                + TERMINAL.move_xy(
                    self.draw_base_hormiguero_x + 91, self.draw_base_hormiguero_y - 2
                )
                + TERMINAL.forestgreen("x" + str(self.food))
            )
        if self.load > 0:
            print(
                TERMINAL.move_xy(
                    self.ant_x + self.draw_base_hormiguero_x,
                    self.draw_base_hormiguero_y + self.ant_y - 1,
                )
                + TERMINAL.forestgreen("█")
            )
            print(
                TERMINAL.move_xy(
                    self.ant_x + self.draw_base_hormiguero_x,
                    self.draw_base_hormiguero_y + self.ant_y - 2,
                )
                + str(self.load)
            )


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
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, base) +     " /                       \==============---------==========------===----------================" )
        




    def loop(self):
        with TERMINAL.cbreak():
            val = ""
            while val.lower() != "k":
                self.draw()

                val = TERMINAL.inkey(timeout=1)
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
                #elif val.lower() == "2":
                 #   if not self.rewards[1].apply_reward(self):
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
            debug("self.load:", repr(self.load))
            self.load = 0

    def draw_points(self):

        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 6, self.draw_base_hormiguero_y - 8)
                + TERMINAL.goldenrod1(TERMINAL.bold(f"POINTS: {self.points}")))

        if self.points > 0:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 5, self.draw_base_hormiguero_y)
                + TERMINAL.forestgreen("█"))
        if self.points >= 5:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 6, self.draw_base_hormiguero_y) +                       TERMINAL.forestgreen("█"))
        if self.points >= 10:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 7, self.draw_base_hormiguero_y) +
                TERMINAL.forestgreen("█"))
        if self.points >= 15:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 5, self.draw_base_hormiguero_y - 1) +
                TERMINAL.forestgreen("█"))
        if self.points >= 20:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 6, self.draw_base_hormiguero_y - 1) +
                TERMINAL.forestgreen("█"))
        if self.points >= 30:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 8, self.draw_base_hormiguero_y) +
                TERMINAL.forestgreen("█"))
        if self.points >= 40:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 9, self.draw_base_hormiguero_y) +
                TERMINAL.forestgreen("█"))
        if self.points >= 45:
            print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 7, self.draw_base_hormiguero_y - 1) +
                TERMINAL.forestgreen("█"))
                
                       
        


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
