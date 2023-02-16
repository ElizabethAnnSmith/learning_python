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



# game.py
# import the draw module
from draw import draw_game

def main():
    result = play_game()
    draw_game(result)

# Advantages of using this is that you don't have to reference the module over and over.
# However, a namespace cannot have two objects with the same name , so the import command
# may replace an existing object in the namespace.



# game.py
# import the draw module
from draw import *

def main():
    result = play_game()
    draw_game(result)

# Using the * for importing can be risky as changes in the module ay affect the module which imports it
# but it is shorter, and doesn't require you to specify every object you want to import from the module.



# Full list of built-in modules in the Python standard library
# Helpful functions - 'dir' and 'help'
# To import the module 'urllib', which enables us to create read data from URLs, we 'import' the module:
# import the library
import urllib

# use it
urllib.urlopen(...)



# Modules may be loaded under any name you want. Useful when importing a module conditionally to use the same name in the rest of the code.
# For example, if you have two 'draw' modules using slightly different names, you can ...
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



# Telling the python interpretor where to look for modules, aside from default local directory
# and built-in modules.
# Use 'PYTHONPATH' to specify additional directories to look for modules, like this...
PYTHONPATH=/foo python game.py

# This executes 'game.py' and enables the script to load modules from the 'foo' directory, as 
# well as the local directory.
# Can also use 'sys.path.append' function. Execute this before import command.
sys.path.append("/foo")



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



# Look for which functions are implemented in each module by using the dir function:
>>> import urllib
>>> dir(urllib)
['ContentTooShortError', 'FancyURLopener', 'MAXFTPCACHE', 'URLopener', '__all__', '__builtins__', 
'__doc__', '__file__', '__name__', '__package__', '__version__', '_ftperrors', '_get_proxies', 
'_get_proxy_settings', '_have_ssl', '_hexdig', '_hextochr', '_hostprog', '_is_unicode', '_localhost', 
'_noheaders', '_nportprog', '_passwdprog', '_portprog', '_queryprog', '_safe_map', '_safe_quoters', 
'_tagprog', '_thishost', '_typeprog', '_urlopener', '_userprog', '_valueprog', 'addbase', 'addclosehook', 
'addinfo', 'addinfourl', 'always_safe', 'basejoin', 'c', 'ftpcache', 'ftperrors', 'ftpwrapper', 'getproxies', 
'getproxies_environment', 'getproxies_macosx_sysconf', 'i', 'localhost', 'main', 'noheaders', 'os', 
'pathname2url', 'proxy_bypass', 'proxy_bypass_environment, 'proxy_bypass_macosx_sysconf', 'quote', 
'quote_plus', 'reporthook', 'socket', 'splitattr', 'splithost', 'splitnport', 'splitpasswd', 'splitport', 
'splitquery', 'splittag', 'splittype', 'splituser', 'splitvalue', 'ssl', 'string', 'sys', 'test', 'test1', 
'thishost', 'time', 'toBytes', 'unquote', 'unquote_plus', 'unwrap', 'url2pathname', 'urlcleanup', 'urlencode', 
'urlopen', 'urlretrieve']



# When we find the function in the module we want to use, we can read more about it with the help function
help(urllib.urlopen)



# Packages are namespaces containing multiple packages and modules. 
# They are just directories, but with certain requirements.

# Each package must contain a file called __init__.py
# It can be empty and indicates the directory is a python package.
# It can be imported the same way as a module.

# If we create a directory called 'foo', which marks the package name, we can then create a module
# inside that package called 'bar'. Then we add __init__.py file inside the 'foo' directory.

# To use the module 'bar' we can import in two ways:
import foo.bar    # OR
for foo import bar

# In the first example, we have to use the 'foo.' prefix whenever we access 'bar'
# In the second example, we don't.
# The __init__.py file can also decide which modules the package exports as the API, while keeping
# other modules interal, by overriding the __all__ variable like this;
__init__.py:
__all__ = ["bar"]
