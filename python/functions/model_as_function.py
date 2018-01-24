from larray import *

def main():
    #define constants
    FIRST_YEAR_OBS = 1991
    FIRST_YEAR_PROJ = 2016
    LAST_YEAR_PROJ = 2060
    YEAR = Axis('year={}..{}'.format(FIRST_YEAR_OBS, LAST_YEAR_PROJ))

    # load input
    pop = read_csv("input/pop_region.csv")

    # start projection with coef = 1.01
    coef = 1.01
    proj_pop1 = pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop1[year] = proj_pop1[year - 1] * coef

    # start projection with coef = 1.02
    coef = 1.02
    proj_pop2 = pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop2[year] = proj_pop2[year - 1] * coef

    # start projection with coef = 1.03
    coef = 1.03
    proj_pop3 = pop.reindex("year", YEAR, fill_value=0)
    for year in YEAR[FIRST_YEAR_PROJ:]:
        proj_pop3[year] = proj_pop3[year - 1] * coef

    # compare the projections
    compare(proj_pop1, proj_pop2, proj_pop3)

    # aggregate first projection
    proj_pop_gy = proj_pop1.sum_by('gender', 'year')

    # view output
    view(proj_pop_gy)


main()
