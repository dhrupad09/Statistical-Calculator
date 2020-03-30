from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.squareroot import squareroot
from Statistics.popstand import popstand
from Statistics.mean import mean


def popuvar(numbers):
    num_value = len(numbers)
    total = 0
    for numb in numbers:
        result = subtraction(numb, mean(numb))
        result1 = square(result)
        result2 = division(num_value, result1)

    return result2
