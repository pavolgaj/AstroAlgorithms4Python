'''Meeus: Astronomical Algorithms (2nd ed.), chapter 25'''   

import math

from nutation_ecliptic import ecliptic
from constants import AU

def coordinates(jd):
    '''equatorial coordinates of Sun'''
    lon=math.radians(longitude(jd))
    
    eps=math.radians(ecliptic(jd))
    
    ra=math.degrees(math.atan2(math.cos(eps)*math.sin(lon),math.cos(lon)))
    dec=math.degrees(math.asin(math.sin(eps)*math.sin(lon)))
    
    return ra,dec
        

def longitude(jd):
    '''longitude of Sun'''
    T=(jd-2451545)/36525.
    
    L=math.radians(280.46646+36000.76983*T+0.0003032*T**2)
    M=math.radians(357.52911+35999.05029*T-0.0001537*T**2)
    
    C=math.radians((1.914602-0.004817*T-0.000014*T**2)*math.sin(M)+(0.019993-0.000101*T)*math.sin(2*M)+0.000289*math.sin(3*M))
    
    lon=L+C
    
    return math.degrees(lon)


def distance(jd,km=True):
    '''Earth-Sun distance in km'''
    T=(jd-2451545)/36525.
    e=0.016708634-0.000042037*T-0.0000001267*T**2
    M=math.radians(357.52911+35999.05029*T-0.0001537*T**2)
    
    C=math.radians((1.914602-0.004817*T-0.000014*T**2)*math.sin(M)+(0.019993-0.000101*T)*math.sin(2*M)+0.000289*math.sin(3*M))
    
    nu=M+C
    R=1.000001018*(1-e**2)/(1+e*math.cos(nu))
    
    if km: R*=AU
    return R
    
