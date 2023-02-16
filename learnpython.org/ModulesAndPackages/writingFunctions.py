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
