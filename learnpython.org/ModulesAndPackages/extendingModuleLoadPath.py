# Telling the python interpretor where to look for modules, aside from default local directory
# and built-in modules.
# Use 'PYTHONPATH' to specify additional directories to look for modules, like this...
PYTHONPATH=/foo python game.py

# This executes 'game.py' and enables the script to load modules from the 'foo' directory, as 
# well as the local directory.
# Can also use 'sys.path.append' function. Execute this before import command.
sys.path.append("/foo")
