# Modules are the same as libraries in Java

# Writing modules
"""
# draw.py
def draw_game():
    pass


def clear_screen(screen):
    pass

"""


"""
# game.py
import draw  # importing the draw module

def play_game():
    pass
    

def main():
    result = play_game()
    draw.draw_game(result)  # do need to add the module name followed by a dot
    
# this means that if this script is executed, then
# main() will be executed
if __name__ == '__main__':
    main()
    
"""

# Importing module objects to the current namespace
"""
# game.py
# import the draw module
from draw import draw_game  # this means we can use only draw_game() method in this file

def main():
    result = play_game()
    draw_game(result)  # don't need to add the module name followed by a dot

"""

# Importing all objects from module
"""
# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

"""

# Custom import name
"""
# game.py
# import the draw module
if visual_mode:
    # in visual mode, we draw using graphics
    import draw_visual as draw
else:
    # in textual mode, we print out text
    import draw_textual as draw

def main():
    result = play_game()
    # this can either be visual or textual depending on visual_mode
    draw.draw_game(result)

"""

# Module initialization
# if one module is imported more than one time in the same module that imported,
# that module is imported only once. This first importing is the module initializing
"""
# draw.py

def draw_game():
    # when clearing the screen we can use the main screen object initialized in this module
    clear_screen(main_screen)
    ...

def clear_screen(screen):
    ...

class Screen():
    ...

# initialize main_screen as a singleton
main_screen = Screen()

"""

# Extending module load path (To research more)

# Exploring built-in modules => is the same as importing built-in libraries or packages
# Example: importing the urllib that enables to create read data from urls
"""
import urllib

# using that library
urllib.urlopen(...)

# if we want to know which function is doing what, then
print(help(urllib.urlopen))
"""

# Writing packages (need to research more)
