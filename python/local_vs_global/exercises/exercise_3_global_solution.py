# ====== Global array variables - Exercise 3 ======

# Exercise 3: using global array variables in functions
#
#   We propose 5 different functions to fill a global array "pop" with a given value.
#   Some are correct and some are not.
#   The use of different functions are activated through "run_function" flags.
#
#   Set to True the "run_function" flags associated with correct ways of
#   modifying global arrays inside a function.
#   If you don't choose well, the program will crash...


from larray import *

AGE = Axis("age=0..5")

fill_value = 5
expected_pop = full(AGE, fill_value)

# SOLUTION:
run_function_1 = False
run_function_2 = True
run_function_3 = True
run_function_4 = False
run_function_5 = True


# ================= VERSION 1 =================
if run_function_1:
    pop = zeros(AGE)

    # EXPLANATION: the use of operator '=' creates a new local array 'pop'.
    # Inside the function, the global array 'pop' is shadowed by the local array 'pop'.
    def fill_pop_1(fill_value):
        pop = full(AGE, fill_value)

    fill_pop_1(fill_value)
    assert larray_equal(pop, expected_pop), "version 1 of fill_pop function is incorrect"


# ================= VERSION 2 =================
if run_function_2:
    pop = zeros(AGE)

    # EXPLANATION: the use of [:] next to the array 'pop' avoid to create a local array.
    def fill_pop_2(fill_value):
        pop[:] = full(AGE, fill_value)

    fill_pop_2(fill_value)
    assert larray_equal(pop, expected_pop), "version 2 of fill_pop function is incorrect"


# ================= VERSION 3 =================
if run_function_3:
    pop = zeros(AGE)

    # EXPLANATION: the use of operator '=' creates a new local array 'pop' but
    # this local array is returned at the end of the function and its content
    # set to the global array 'pop' by typing "pop = fill_pop_3(fill_value)"
    def fill_pop_3(fill_value):
        pop = full(AGE, fill_value)
        return pop

    pop = fill_pop_3(fill_value)
    assert larray_equal(pop, expected_pop), "version 3 of fill_pop function is incorrect"


# ================= VERSION 4 =================
if run_function_4:
    pop = zeros(AGE)

    # EXPLANATION: input arguments are local variables.
    def fill_pop_4(pop, fill_value):
        pop = full(AGE, fill_value)

    fill_pop_4(pop, fill_value)
    assert larray_equal(pop, expected_pop), "version 4 of fill_pop function is incorrect"

# ================= VERSION 5 =================
if run_function_5:
    pop = zeros(AGE)

    # EXPLANATION: the use of [:] next to the array 'pop' avoid to create a local array.
    def fill_pop_5(pop, fill_value):
        pop[:] = full(AGE, fill_value)

    fill_pop_5(pop, fill_value)
    assert larray_equal(pop, expected_pop), "version 5 of fill_pop function is incorrect"
