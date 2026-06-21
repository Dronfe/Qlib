import math 
import matplotlib.pyplot as plt
import yfinance as yf
def normal_distribution(sig,meu, x):
    def function(x):
        return round(1/(2*3.1415*sig**2)**2.71828**-1/2*(x - meu/(sig)**2),2)
    d = {} 
    for i in x: 
        d[i] = function(i) 
    plt.scatter(d.key-s(),d.values(),color = 'blue',marker='o')    
    return d.values() 
    return 
def brownian_movement():
    return   

