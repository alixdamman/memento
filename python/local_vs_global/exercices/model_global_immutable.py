# ====== Global immutable variables ======
#
# Exercise 1: There is something horribly wrong in this script
#
# a) Find and explain what is wrong in the code below
# b) modify the code below so as it does what it is expected to do


from larray import *

# define constants
FIRST_YEAR_OBS = 1991
FIRST_YEAR_PROJ = 2016
LAST_YEAR_PROJ = 2060
YEAR = Axis('year={}..{}'.format(FIRST_YEAR_OBS, LAST_YEAR_PROJ))

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


main()
