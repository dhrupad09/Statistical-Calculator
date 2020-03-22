from Calculator.Addition import add
from Calculator.Division import div
from Statistics.sample import getSample


def samplemean(data, sample_size):
    total = 0
    sample = getSample(data, sample_size)
    num_values = len(sample)
    for num in sample:
        total = add(total, num)
    return div(total, num_values)