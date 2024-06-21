#!/usr/bin/fades

import blessed # fades

TERMINAL = blessed.Terminal()  

class Clicker:
    def __init__(self):
       self.x = 61
       self.y = 32
       self.food = 0

       self.draws_size_x = 120
       self.draws_size_y = 9

       self.draw_base_hormiguero_x = int((TERMINAL.width - self.draws_size_x) / 2)
       self.draw_base_hormiguero_y = int((TERMINAL.height - self.draws_size_y) / 2)

    def draw(self):
        print(TERMINAL.clear())
        print(TERMINAL.move_xy(self.x, self.y) + TERMINAL.orangered4("█") + TERMINAL.sienna("█"))

        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 100, self.draw_base_hormiguero_y - 7) + TERMINAL.limegreen(".\^/."))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 97, self.draw_base_hormiguero_y - 6) + TERMINAL.limegreen("'. |`|/| ." ))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 97, self.draw_base_hormiguero_y - 5) + TERMINAL.limegreen("'|\|\|'|/|" ))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 95, self.draw_base_hormiguero_y - 4) + TERMINAL.limegreen(".--'-\`|/-''--." ))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 96, self.draw_base_hormiguero_y - 3) + TERMINAL.limegreen("\`-._\|./.-'/" ))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 97, self.draw_base_hormiguero_y - 2) + TERMINAL.limegreen(">`-._|/.-'<" ))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 96, self.draw_base_hormiguero_y - 1) + TERMINAL.limegreen("'~|/~~|~~\|~'" ))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 102, self.draw_base_hormiguero_y) + TERMINAL.limegreen("|"))
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x + 91, self.draw_base_hormiguero_y - 9) + TERMINAL.bold(TERMINAL.limegreen("[SPACE] to byte the Leaf")))

        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, self.draw_base_hormiguero_y - 4) + "       _/======\_" )
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, self.draw_base_hormiguero_y - 3) + "     _/          \__" )
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, self.draw_base_hormiguero_y - 2) + "   _/               \_" )
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, self.draw_base_hormiguero_y - 1) + "  /                   \__")
        print(TERMINAL.move_xy(self.draw_base_hormiguero_x, self.draw_base_hormiguero_y) + " /                       \==============---------==========------===----------================" )

        if self.food > 0:
            print(TERMINAL.move_xy(141, 36) + TERMINAL.forestgreen("█") +
                  TERMINAL.move_xy(140, 35) + TERMINAL.forestgreen("x" + str(self.food)))

    def loop(self):
        with TERMINAL.cbreak():
            val = ''
            while val.lower() != "q":
                self.draw()

                val = TERMINAL.inkey(timeout=1)
                if val.lower() == " ":
                    self.food += 1
                elif val.lower() == "d":
                    self.x += 1
                elif val.lower() == "a":
                    self.x -= 1
                elif val.lower() == "s":
                    self.y += 1
                elif val.lower() == "w":
                    self.y -= 1

                self.draw_base_hormiguero_x = int((TERMINAL.width - self.draws_size_x) / 2)
                self.draw_base_hormiguero_y = int((TERMINAL.height - self.draws_size_y) / 6 * 5 )

        print(TERMINAL.clear())


clicker = Clicker()
clicker.loop()
           