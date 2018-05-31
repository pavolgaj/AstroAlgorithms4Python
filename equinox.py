'''Meeus: Astronomical Algorithms (2nd ed.), chapter 27'''

import math

def _corrections(jd):
    '''corrections to times of equinox/solstice'''
    T=(jd-2451545)/36525.
    
    W=math.radians(35999.373*T-2.47)
    dl=1+0.0334*math.cos(W)+0.0007*math.cos(2*W)
    
    A=[485,203,199,182,156,136,77,74,70,58,52,50,45,44,29,18,17,16,14,12,12,12,9,8]
    B=[324.96,337.23,342.08,27.85,73.14,171.52,222.54,296.72,243.58,119.81,297.17,21.02,247.54,325.15,60.93,155.12,288.79,198.04,199.76,95.39,287.11,320.81,227.73,15.45]
    C=[1934.136,32964.467,20.186,445267.112,45036.886,22518.443,65928.934,3034.906,9037.513,33718.147,150.678,2281.226,29929.562,31555.956,4443.417,67555.328,4562.452,62894.029,31436.921,
       14577.848,31931.756,34777.259,1222.114,16859.074] 
    
    S=0
    for i in range(len(A)): S+=A[i]*math.cos(math.radians(B[i]+C[i]*T))
    return jd+0.00001*S/dl
    

def spring(year):
    '''calculate spring (March) equinox for given year'''
    Y=(year-2000)/1000.
    jd0=2451623.80984+365242.37404*Y+0.05169*Y**2-0.00411*Y**3-0.00057*Y**4
    return _corrections(jd0)
    
def summer(year):
    '''calculate summer (June) solstice for given year'''
    Y=(year-2000)/1000.
    jd0=2451716.56767+365241.62603*Y+0.00325*Y**2+0.00888*Y**3-0.00030*Y**4
    return _corrections(jd0)
    
def autumn(year):
    '''calculate autumn (September) equinox for given year'''
    Y=(year-2000)/1000.
    jd0=2451810.21715+365242.01767*Y-0.11575*Y**2+0.00337*Y**3+0.00078*Y**4
    return _corrections(jd0)
    
def winter(year):
    '''calculate winter (December) solstice for given year'''
    Y=(year-2000)/1000.
    jd0=2451900.05952+365242.74049*Y-0.06223*Y**2-0.00823*Y**3+0.00032*Y**4
    return _corrections(jd0)


def year(year):
    '''calculate equinoxes and solstices for given year'''
    return spring(year),summer(year),autumn(year),winter(year)
    
    