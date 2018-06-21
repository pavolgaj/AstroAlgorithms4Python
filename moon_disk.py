'''Meeus: Astronomical Algorithms (2nd ed.), chapter 48''' 

import math

import sun
import moon

def fraction(jd,angle=False):
    '''illuminated fraction or phase angle of the Moon's disk'''
    raS,decS=sun.coordinates(jd)    
    R=sun.distance(jd)
    raM,decM,lon,lat,dist,par=moon.position(jd,full=True)
    
    raS=math.radians(raS)
    decS=math.radians(decS)
    raM=math.radians(raM)
    decM=math.radians(decM)
    
    psi=math.acos(math.sin(decS)*math.sin(decM)+math.cos(decS)*math.cos(decM)*math.cos(raS-raM))
    i=math.atan(R*math.sin(psi)/(dist-R*math.cos(psi)))
    
    k=(1+math.cos(i))/2.
    
    if angle: return math.degrees(i)
    return k
    
def angle(jd):
    '''position angle of the Moon's bright limb'''
    raS,decS=sun.coordinates(jd)    
    raM,decM=moon.position(jd)
    
    raS=math.radians(raS)
    decS=math.radians(decS)
    raM=math.radians(raM)
    decM=math.radians(decM)
    
    chi=math.atan2(math.cos(decS)*math.sin(raS-raM),math.sin(decS)*math.cos(decS)-math.cos(decS)*math.sin(decM)*math.cos(raS-raM))
    return math.degrees(chi)%360
    