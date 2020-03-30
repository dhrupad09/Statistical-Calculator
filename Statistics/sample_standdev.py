from random import sample
from Statistics.mean import mean
from Calculator.subtraction import subtraction
from Calculator.square import square
from Calculator.addition import addition
from Calculator.division import division
from Calculator.squareroot import squareroot



def samplestand(data):

    dev=0

    sample_values=len(sample)

    x_bar=mean()
    x=sample_values
    n=subtraction(sample_values,1)
    for dev in sample:
        dev=subtraction(x,x_bar)
        sqaure_x_bar=square(dev)
        add=addition(sqaure_x_bar,sqaure_x_bar)
        result=division(add,n)
    return squareroot(result)