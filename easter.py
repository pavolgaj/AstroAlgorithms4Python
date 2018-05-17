'''Meeus: Astronomical Algorithms (2nd ed.), chapter 8'''

def gregorian(year):
    '''find Gregorian Easter'''
    a=year%19
    b=year//100
    c=year%100
    d=b//4
    e=b%4
    f=(b+8)//25
    g=(b-f+1)//3
    h=(19*a+b-d-g+15)%30
    i=c//4
    k=c%4
    l=(32+2*e+2*i-h-k)%7
    m=(a+11*h+22*l)//451
    n=(h+l-7*m+114)//31
    p=(h+l-7*m+114)%31
    
    return n,p+1  #moon and day of Easter Sunday


def julian(year,greg=True):
    '''find Julian Easter, date in gregorian or julian calendar'''
    a=year%4
    b=year%7
    c=year%19
    d=(19*c+15)%30
    e=(2*a+4*b-d+34)%7
    if greg: e+=13  #difference between gregorian and julian calendar - valid from 1900 to 2100
    f=(d+e+114)//31
    g=(d+e+114)%31
    
    return f,g+1  #moon and day of Easter Sunday
    
    