"""Module documentation"""

# restrict what is imported from this module using
# from my_package.my_module import *
__all__ = ['var', 'var2', 'print_dir']


# ========== #
# statements #
# ========== #

# global vars
var = 'my_module_var'
var2 = 'my_module_var2'

#print statement
print("import module `{}` from package `{}`".format(__file__, __package__))

# ========= #
# functions #
# ========= #

def print_hello(firstname, name):
    print('hello', firstname, name, '!')

def print_dir():
    for elem in dir():
        print(elem)
