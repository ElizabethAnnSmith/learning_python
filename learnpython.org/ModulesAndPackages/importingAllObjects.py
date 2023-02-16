# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

# Using the * for importing can be risky as changes in the module ay affect the module which imports it
# but it is shorter, and doesn't require you to specify every object you want to import from the module.
