#!/usr/bin/fades

import blessed # fades

TERMINAL = blessed.Terminal()  

class Clicker:
    def __init__(self):
       self.x = 61
       self.y = 32
       self.food = 0

    def draw(self):
        print(TERMINAL.clear())
        print(TERMINAL.move_xy(self.x, self.y) + TERMINAL.orangered4("█") + TERMINAL.sienna("█"))

        print(TERMINAL.move_xy(150, 30) + TERMINAL.limegreen(".\^/."))
        print(TERMINAL.move_xy(147, 31) + TERMINAL.limegreen("'. |`|/| ." ))
        print(TERMINAL.move_xy(147, 32) + TERMINAL.limegreen("'|\|\|'|/|" ))
        print(TERMINAL.move_xy(145, 33) + TERMINAL.limegreen(".--'-\`|/-''--." ))
        print(TERMINAL.move_xy(146, 34) + TERMINAL.limegreen("\`-._\|./.-'/" ))
        print(TERMINAL.move_xy(147, 35) + TERMINAL.limegreen(">`-._|/.-'<" ))
        print(TERMINAL.move_xy(146, 36) + TERMINAL.limegreen("'~|/~~|~~\|~'" ))
        print(TERMINAL.move_xy(152, 37) + TERMINAL.limegreen("|"))
        print(TERMINAL.move_xy(141, 28) + TERMINAL.bold(TERMINAL.limegreen("[SPACE] to byte the Leaf")))

        print(TERMINAL.move_xy(50, 33) + "       _/======\_" )
        print(TERMINAL.move_xy(50, 34) + "     _/          \__" )
        print(TERMINAL.move_xy(50, 35) + "   _/               \_" )
        print(TERMINAL.move_xy(50, 36) + "  /                   \__")
        print(TERMINAL.move_xy(50, 37) + " /                       \==============---------==========------===----------================" )

        if self.food > 0:
            print(TERMINAL.move_xy(141, 36) + TERMINAL.forestgreen("█") +
                  TERMINAL.move_xy(140, 35) + TERMINAL.forestgreen("x" + str(self.food)))

    def keys(self):
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

        print(TERMINAL.clear())


clicker = Clicker()
clicker.keys()
           