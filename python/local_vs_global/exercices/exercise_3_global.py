# ====== Global arrays ======
#
# Exercise 3: using arrays as global variables
#
# set to True the "run_function" flags below to run the different version of "fill_pop" functions.
# If you chose well, the program should not crash

from larray import *

AGE = Axis("age=0..5")

fill_value = 5
expected_pop = full(AGE, fill_value)

# set to True the right ones
run_function_1 = False
run_function_2 = False
run_function_3 = False
run_function_4 = False
run_function_5 = False


# ================= VERSION 1 =================
if run_function_1:
    pop = zeros(AGE)

    def fill_pop_1(fill_value):
        pop = full(AGE, fill_value)

    fill_pop_1(fill_value)
    assert pop.equals(expected_pop), "version 1"


# ================= VERSION 2 =================
if run_function_2:
    pop = zeros(AGE)

    def fill_pop_2(fill_value):
        pop[:] = full(AGE, fill_value)

    fill_pop_2(fill_value)
    assert pop.equals(expected_pop), "version 2"


# ================= VERSION 3 =================
if run_function_3:
    pop = zeros(AGE)

    def fill_pop_3(fill_value):
        pop = full(AGE, fill_value)
        return pop

    pop = fill_pop_3(fill_value)
    assert pop.equals(expected_pop), "version 3"


# ================= VERSION 4 =================
if run_function_4:
    pop = zeros(AGE)

    def fill_pop_4(pop, fill_value):
        pop = full(AGE, fill_value)


    fill_pop_4(pop, fill_value)
    assert pop.equals(expected_pop), "version 4"

# ================= VERSION 5 =================
if run_function_5:
    pop = zeros(AGE)

    def fill_pop_5(pop, fill_value):
        pop[:] = full(AGE, fill_value)


    fill_pop_5(pop, fill_value)
    assert pop.equals(expected_pop), "version 5"
