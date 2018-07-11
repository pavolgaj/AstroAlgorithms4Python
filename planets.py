'''Meeus: Astronomical Algorithms (2nd ed.), chapter 33''' 

import math

import position
import coordinates

def _calculate(L,B,r,jd):
    L0,B0,r0=position.Earth(jd)
    
    L=math.radians(L)
    B=math.radians(B)
    L0=math.radians(L0)
    B0=math.radians(B0)
    
    x=r*math.cos(B)*math.cos(L)-r0*math.cos(B0)*math.cos(L0)
    y=r*math.cos(B)*math.sin(L)-r0*math.cos(B0)*math.sin(L0)
    z=r*math.sin(B)-r0*math.sin(B0)
    
    l=math.degrees(math.atan2(y,x))
    b=math.degrees(math.atan2(z,math.sqrt(x**2+y**2)))
    
    return coordinates.ecl2eq(l,b)

def Mercury(jd):
    '''equatorial coordinates of Mercury'''
    L,B,r=position.Mercury(jd)
    return _calculate(L,B,r,jd)

def Venus(jd):
    '''equatorial coordinates of Venus'''
    L,B,r=position.Venus(jd)
    return _calculate(L,B,r,jd)

def Mars(jd):
    '''equatorial coordinates of Mars'''
    L,B,r=position.Mars(jd)
    return _calculate(L,B,r,jd)

def Jupiter(jd):
    '''equatorial coordinates of Jupiter'''
    L,B,r=position.Jupiter(jd)
    return _calculate(L,B,r,jd)

def Saturn(jd):
    '''equatorial coordinates of Saturn'''
    L,B,r=position.Saturn(jd)
    return _calculate(L,B,r,jd)

def Uranus(jd):
    '''equatorial coordinates of Uranus'''
    L,B,r=position.Uranus(jd)
    return _calculate(L,B,r,jd)

def Neptune(jd):
    '''equatorial coordinates of Neptune'''
    L,B,r=position.Neptune(jd)
    return _calculate(L,B,r,jd)
    