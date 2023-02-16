# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# Advantages of using this is that you don't have to reference the module over and over.
# However, a namespace cannot have two objects with the same name , so the import command
# may replace an existing object in the namespace.
