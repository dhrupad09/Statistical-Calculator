from Calculator.addition import addition
from Calculator.division import division
from Statistics.getsample import getSample


def sample_mean(data):
    total = 0
    # check that get sample returns the proper number of samples
    # check that sample size is not 0
    # check that sample size is not larger than the population
    # https://realpython.com/python-exceptions/
    # https://stackoverflow.com/questions/129507/how-do-you-test-that-a-python-function-throws-an-exception
    num_values = len(data)
    for num in data:
        total = addition(total, num)
    return division(total, num_values)