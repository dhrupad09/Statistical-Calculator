from pprint import pprint
from Statistics.proportion import prop
from Statistics.popuvar import popuvar

def variance_sample_prop(my_pop):
    p,proportion_success= prop(my_pop)
    return popuvar(proportion_success)
