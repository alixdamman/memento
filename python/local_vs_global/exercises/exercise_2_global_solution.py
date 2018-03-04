# ====== Global non-array variables - Exercise 2 ======

# Exercise 2: using global non-array variables in a model
#
#   There is something terribly wrong in this script.
#   a) Find and explain what is wrong in the code.
#   b) Modify the code so as it does what it is expected to do.


from larray import *

# define constants
FIRST_YEAR_OBS = 1991
FIRST_YEAR_PROJ = 2016
LAST_YEAR_PROJ = 2060
YEAR = Axis('year={}..{}'.format(FIRST_YEAR_OBS, LAST_YEAR_PROJ))

# ======================================================== #
#           ORIGINAL CODE WITH EXPLANATIONS                #
# ======================================================== #
# In the main() function, the line:
# coef = coef_val
# creates a local variable 'coef' while the global variable 'coef' remains unchanged.
# As a consequence, the global variable 'coef' in the function 'projection' represents
# always the same value: 1.0


# global coeff
coef = 1.


def projection(initial_pop):
    """Compute projected population for year 2016 to 2060"""
    proj_pop = initial_pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop[year] = proj_pop[year - 1] * coef
    return proj_pop


def main():
    # load input
    pop = read_csv("input/pop_region.csv")

    # test several coefficient values
    coefs = [1.01, 1.02, 1.03]
    output = Session()
    i = 1
    for coef_val in coefs:
        coef = coef_val
        scenario_name = 'scenario{}'.format(i)
        output[scenario_name] = projection(pop)
        i = i + 1

    # compare the projections
    compare(output.scenario1, output.scenario2, output.scenario3)


# ======================================================== #
#                         SOLUTION                         #
# ======================================================== #
# 1) remove the global variable 'coef',
# 2) add an input argument 'coef' to the function 'projection',
# 3) pass the different values of 'coef' as argument in the loop in the main() function


def projection(initial_pop, coef):
    """Compute projected population for year 2016 to 2060"""
    proj_pop = initial_pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop[year] = proj_pop[year - 1] * coef
    return proj_pop


def main():
    # load input
    pop = read_csv("input/pop_region.csv")

    # test several coefficient values
    coefs = [1.01, 1.02, 1.03]
    output = Session()
    i = 1
    for coef in coefs:
        scenario_name = 'scenario{}'.format(i)
        output[scenario_name] = projection(pop, coef)
        i = i + 1

    # compare the projections
    compare(output.scenario1, output.scenario2, output.scenario3)


main()
