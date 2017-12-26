"""Package documentation"""

print("import package `{package}`. Execute `{package}/__init__.py` module.".format(package=__package__))

# do some imports and initializations
from .another_module import print_another_var, another_function
