# A module is a piece of software that has a specific functionality.
# For example, for a ping pong game, one module might be game logic and another might draw the game on the screen.
# Each module consists of a different file
# Modules have the .py extension and the module name is the file name
# A module can have a set of functions, classes or variables.

# Example
# mygame/
#     - mygame/game.py
#     - mygame/draw.py

# game.py implements the game and uses the function draw_game from the draw.py file (the draw module) which implements the logic for drawing the game on the screen.
# Modules are imported from other modules using the 'import' command.

# So game.py might look something like this...

# import draw
#
# def play_game():
#    ...
#
# def main():
#     result = play_game()
#     draw.draw_game(result)
#
# this means that if this script is executed, then 
# main() will be executed
# if __name__ == '__main__':
#     main()

# The draw.py module might look like this...

# def draw_game():
#     ...
#
# def clear_screen(screen):
#     ...

# game module imports the draw module which enables it to use functions implemented in that module. The main function uses the local function play_game to run the game and then draws the result of the game using a function implemented in the draw module.
# To use the function draw_game from the draw module, we need to specify in which module the function is implemented, using the dot operator. 
# To reference the draw_game function in the game module, we need to import the draw module and then call draw.draw_game().

# When 'import draw' runs, the interpreter looks for a file in the directory with the name and .py on the end. This cmd will look for draw.py and if found will be imported. If not found, it'll keep looking.

# When importing a module, a .pyc file is created - a complied Python file. Python compiles files into Python bytecode so it doesn't have to parse the files each time the modules are loaded. If a .pyc file exists, it gets loaded instead of .py file.

