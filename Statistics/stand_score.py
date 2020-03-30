from Statistics.mean import mean
from Statistics.popstand import popstand

def standardised_score(my_pop):
    my_mean = mean(my_pop)
    my_sd = popstand(my_pop)
    standardised_score = float(list())
    for x in my_pop:
        my_score = (x - my_mean) / my_sd
        standardised_score.append(my_score)
    return standardised_score