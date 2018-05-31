'''Meeus: Astronomical Algorithms (2nd ed.), chapter 25'''   

import math

from nutation_ecliptic import ecliptic

def coordinates(jd):
    '''equatorial coordinates of Sun'''
    T=(jd-2451545)/36525.
    
    L=math.radians(280.46646+36000.76983*T+0.0003032*T**2)
    M=math.radians(357.52911+35999.05029*T-0.0001537*T**2)
    
    C=math.radians((1.914602-0.004817*T-0.000014*T**2)*math.sin(M)+(0.019993-0.000101*T)*math.sin(2*M)+0.000289*math.sin(3*M))
    
    lon=L+C
    
    eps=math.radians(ecliptic(jd))
    
    ra=math.degrees(math.atan2(math.cos(eps)*math.sin(lon),math.cos(lon)))
    dec=math.degrees(math.asin(math.sin(eps)*math.sin(lon)))
    
    return ra,dec
        
    
