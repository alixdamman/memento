# ====== Global array variables - Exercise 4 ======

# Exercise 4: using global array variables in a model
#
#   There is something horribly wrong in this script.
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

# global pop and proj_pop
pop = LArray([])
proj_pop = LArray([])


def projection(coef):
    """Compute projected population for year 2016 to 2060"""
    # EXPLANATION: the use of the operator '=' creates a local array 'proj_pop'.
    # The global array 'proj_pop' is shadowed'
    proj_pop = pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop[year] = proj_pop[year - 1] * coef


def main():
    # load input
    # EXPLANATION: the use of the operator '=' creates a local array 'pop'.
    # The global array 'pop' is shadowed'
    pop = read_csv("input/pop_region.csv")

    # test several coefficient values
    coefs = [1.01, 1.02, 1.03]
    output = Session()
    i = 1
    for coef in coefs:
        projection(coef)
        scenario_name = 'scenario{}'.format(i)
        # A Session object does not store the content of arrays
        # but references (links) to them.
        # To avoid this, you must use the 'copy()' method.
        output[scenario_name] = proj_pop
        i = i + 1

    # compare the projections
    compare(output.scenario1, output.scenario2, output.scenario3)

# ======================================================== #
#             SOLUTION WITH LOCAL VARIABLES                #
# ======================================================== #
# 1) add an input argument 'initial_pop' to the function 'projection'
# 2) use the 'return' statement to return the local array 'proj_pop'
#    at the end of the function 'projection'
# 3) in the loop in the main() function, remove the line "projection(coef)"
#    and replace the line "output[scenario_name] = proj_pop" by
#    "output[scenario_name] = projection(pop, coef)"


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

# ======================================================== #
#             SOLUTION WITH GLOBAL VARIABLES               #
# ======================================================== #
# 1) initialize the global array 'pop' at declaration
# 2) initialize the global array 'proj_pop' at declaration (using reindex)
# 3) in the function 'projection', remove the call to reindex and reset values
#    of 'proj_pop' to 0 for the projection period
# 4) in the loop in the main() function, add '.copy()' to 'proj_pop'
#    (See the Tutorial of LArray)

# global pop and proj_pop
pop = read_csv("input/pop_region.csv")
proj_pop = pop.reindex('year', YEAR, fill_value=0)


def projection(coef):
    """Compute projected population for year 2016 to 2060"""
    proj_pop[FIRST_YEAR_PROJ:] = 0
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop[year] = proj_pop[year - 1] * coef


def main():
    # test several coefficient values
    coefs = [1.01, 1.02, 1.03]
    output = Session()
    i = 1
    for coef in coefs:
        projection(coef)
        scenario_name = 'scenario{}'.format(i)
        output[scenario_name] = proj_pop.copy()
        i = i + 1

    # compare the projections
    compare(output.scenario1, output.scenario2, output.scenario3)


main()
