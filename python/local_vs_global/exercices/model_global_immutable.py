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

# global coeff + display flag
coef = 1.
display = False


def projection(initial_pop):
    """Compute projected population for year 2016 to 2060"""
    proj_pop = initial_pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop[year] = proj_pop[year - 1] * coef
    if display:
        view(proj_pop)
    return proj_pop


def main():
    # load input
    pop = read_csv("input/pop_region.csv")

    # display projected arrays
    display = True

    # test several coefficient values
    coefs = [1.01, 1.02, 1.03]
    proj_pop = Session()
    for i, coef_val in enumerate(coefs):
        coef = coef_val
        proj_pop['proj_pop_sc{}'.format(i)] = projection(pop)

    # compare the projections
    # proj_pop.values() return the list of arrays of proj_pop session
    # compare(*[arr1, arr2, arr3]) is equivalent to compare(arr1, arr2, arr3)
    compare(*proj_pop.values())

    # aggregate first projection
    proj_pop_gy = proj_pop['proj_pop_sc1'].sum_by('gender', 'year')

    # view output
    view(proj_pop_gy)


main()
