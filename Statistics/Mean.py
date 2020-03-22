from src.Calculator.Addition import add
from src.Calculator.Division import div


def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = add(total, num)
    return div(total, num_values)