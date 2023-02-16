# The first time a module is loaded into a running python script, it is initialized by executing
# the code in the module once. If another module in your code imports the same module again, 
# it will not be loaded again, so loacl variables inside the module act as a 'singleton', meaning
# they are initialized only once. You can then use this to initialize objects.

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
