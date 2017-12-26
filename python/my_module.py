"""Module documentation"""

# ========== #
# statements #
# ========== #

# global vars
var = 'my_module_var'
var2 = 'my_module_var2'

#print statement
print("import module `{}.py` and execute a print statement".format(__name__))

# ========= #
# functions #
# ========= #

def print_hello(firstname, name):
    print('hello', firstname, name, '!')

def print_sys_path():
    import sys
    for mod in sys.path:
        print(mod)
