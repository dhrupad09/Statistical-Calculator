from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.squareroot import squareroot
from Statistics.popstand import popstand


def confidence_interval(numbers):
    num_value = len(numbers)
    result = popstand(numbers)
    result2 = squareroot(num_value)
    sample_error = division(result2, result)
    margin_error = multiplication(1.96,  sample_error)  # 1.96=z_value for 95% confidence interval
    result4 = addition(result, margin_error)
    result5 = subtraction(margin_error, result)
    return result4, result5
