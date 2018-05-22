'''Meeus: Astronomical Algorithms (2nd ed.), chapter 17'''  

import math

def separation(ra1,dec1,ra2,dec2):
    '''angular separation between 2 objects'''
    dec1=math.radians(dec1)
    dec2=math.radians(dec2)
    ra=math.radians(ra1-ra2)
    d=math.acos(math.sin(dec1)*math.sin(dec2)+math.cos(dec1)*math.cos(dec2)*math.cos(ra))
    return math.degrees(d)

def positionAngle(ra1,dec1,ra2,dec2):
    '''position angle of (ra1,dec1) with respect to (ra2,dec2)'''
    dec1=math.radians(dec1)
    dec2=math.radians(dec2)
    ra=math.radians(ra1-ra2)
    P=math.degrees(math.atan2(math.sin(ra),math.cos(dec2)*math.tan(dec1)-math.sin(dec2)*math.cos(ra)))
    P=P%360
    return P
    
    