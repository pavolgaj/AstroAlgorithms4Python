'''Meeus: Astronomical Algorithms (2nd ed.), chapter 11'''

import math

def distance(lat1,lon1,lat2,lon2):
    '''distance between 2 points on Earth'''
    a=6378.14
    f=1/298.257
    
    F=math.radians((lat1+lat2)/2.)
    G=math.radians((lat1-lat2)/2.)
    l=math.radians((lon1-lon2)/2.)
    S=math.sin(G)**2*math.cos(l)**2+math.cos(F)**2*math.sin(l)**2
    C=math.cos(G)**2*math.cos(l)**2+math.sin(F)**2*math.sin(l)**2
    w=math.atan(math.sqrt(S/C))
    R=math.sqrt(S*C)/w
    D=2*w*a
    H1=(3*R-1)/(2*C)
    H2=(3*R+1)/(2*S)
    return D*(1+f*H1*math.sin(F)**2*math.cos(G)**2-f*H2*math.cos(F)**2*math.sin(G)**2)
    