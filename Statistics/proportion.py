from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.squareroot import squareroot
from Statistics.popstand import popstand
from Statistics.mean import mean

def prop(numbers):
    num_value = len(numbers)
    result = 0
    for num in numbers:
        if result > 10:
            addition(result, result)
    return division(num, num_value)