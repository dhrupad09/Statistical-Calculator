from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.squareroot import squareroot
from Statistics.popstand import popstand
from Statistics.mean import mean
from Statistics.z_score import zscore

def P_value(numbers):
    numbers = []
    num_value = len(numbers)
    score = zscore()
    for pos in num_value:
        if num_value == pos:
            numbers.append(pos)
    return pos
