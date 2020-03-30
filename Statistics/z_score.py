from Statistics.mean import mean
from Statistics.sample_standdev import samplestand
from Calculator.subtraction import subtraction
from Calculator.division import division

def zscore(data):

    x=64
    u=mean(data)
    sample_sd=samplestand(data)
    y=subtraction(x,u)
    return division(sample_sd,y)