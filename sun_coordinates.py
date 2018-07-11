'''Meeus: Astronomical Algorithms (2nd ed.), chapter 26''' 

import math

import position
import nutation_ecliptic

def coordinates(jd):
    '''rectangular coordinates of Sun to mean equinox'''
    LE,BE,r=position.Earth(jd)
    
    L=math.radians(LE+180)
    B=-math.radians(BE)
    eps=math.radians(nutation_ecliptic.ecliptic(jd))
    
    X=r*math.cos(B)*math.cos(L)
    Y=r*(math.cos(B)*math.sin(L)*math.cos(eps)-math.sin(B)*math.sin(eps))
    Z=r*(math.cos(B)*math.sin(L)*math.sin(eps)+math.sin(B)*math.cos(eps))
    
    return X,Y,Z
