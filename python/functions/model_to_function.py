from larray import *

from params import *


# load input
pop = read_csv("input/pop_region.csv")
qx = read_csv("input/qx_region.csv")

# start model
proj_pop = pop.reindex("year", YEAR, fill_value=0)
for year in YEAR[FIRST_YEAR_PROJ:]:
    last_year_pop = proj_pop[year - 1]
    deceased = last_year_pop * qx[2015]
    survivors = last_year_pop - deceased
    proj_pop[year] = survivors
# end model

# aggregate result
proj_pop_gy = proj_pop.sum_by('gender', 'year')

# save output
if EXPORT_EXCEL:
    proj_pop_gy.to_excel('output/proj_pop.xlsx', 'bygender')
