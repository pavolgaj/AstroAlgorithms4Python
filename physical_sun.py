'''Meeus: Astronomical Algorithms (2nd ed.), chapter 29''' 

import math

from nutation_ecliptic import nutation,ecliptic
from sun import longitude

def PBL(jd):
    '''calculate position angle P, heliographic lat. of center L0, hel. long. of center B0'''
    th=(jd-2398220)*360/25.38
    I=math.radians(7.25)
    K=math.radians(73.6667+1.3958333*(jd-2396758)/36525.)
    
    psi,eps=nutation(jd)    
    eps=math.radians(eps+ecliptic(jd))
    psi=math.radians(psi)
    
    lon=math.radians(longitude(jd))    
    
    x=math.degrees(math.atan(-math.cos(lon+psi)*math.tan(eps)))
    y=math.degrees(math.atan(-math.cos(lon-K)*math.tan(I)))
    
    P=x+y
    B=math.degrees(math.asin(math.sin(lon-K)*math.sin(I)))
    nu=math.degrees(math.atan2(-math.sin(lon-K)*math.cos(I),-math.cos(lon-K)))    
    
    L=(nu-th)%360    
    
    return P,B,L

def rotation(jd):
    '''Carrington rotation number'''
    jd0=2398140.10155
    return int(((jd-jd0)/27.2752316)//1)

def rotation_start(n):
    '''time of begining Carrington rotation'''
    jd=2398140.2270+27.2752316*n
    
    M=math.radians(281.96+26.882476*n)
    return jd+0.1454*math.sin(M)-0.0085*math.sin(2*M)-0.0141*math.cos(2*M)
