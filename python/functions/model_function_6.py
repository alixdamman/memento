# ====== Default argument values ======
#
# Exercise 6: add an argument with a default value to the function "projection"
#
# * add a boolean argument display with default value set to False
# * before returning the result in function "projection", start the viewer if display is True
# * change calls to function "projection" so that it displays the result before it returns the result of projection


from larray import *

# define constants
FIRST_YEAR_OBS = 1991
FIRST_YEAR_PROJ = 2016
LAST_YEAR_PROJ = 2060
YEAR = Axis('year={}..{}'.format(FIRST_YEAR_OBS, LAST_YEAR_PROJ))


def projection(initial_pop, coef, display=False):
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

    # start projection
    proj_pop1 = projection(pop, 1.01, True)

    # start projection with a new coefficient value
    proj_pop2 = projection(pop, coef=1.02, display=True)

    # start projection with a new coefficient value
    proj_pop3 = projection(coef=1.03, initial_pop=pop, display=True)

    # compare the projections
    compare(proj_pop1, proj_pop2, proj_pop3)

    # aggregate first projection
    proj_pop_gy = proj_pop1.sum_by('gender', 'year')

    # view output
    view(proj_pop_gy)


main()
