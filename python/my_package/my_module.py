"""Module documentation:

package: {}
module: {}
path: {}
""".format(__package__, __name__, __file__)

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
print("import module `{}.py` from package {}".format(__name__, __package__))

# ========= #
# functions #
# ========= #

def print_hello(firstname, name):
    print('hello', firstname, name, '!')

def print_dir():
    for elem in dir():
        print(elem)
