'''Meeus: Astronomical Algorithms (2nd ed.), chapter 43''' 

import math

def calculate(jd):
    '''calculation of Jupiter's parameters: Earth-Jup distance, longitudes of central meridian, planetocentric dec. of Earth and Sun'''
    d=jd-2451545.0
    
    V=math.radians(172.74+0.00111588*d)
    M=math.radians(357.529+0.9856003*d)
    N=math.radians(20.020+0.0830853*d+0.329*math.sin(V))
    
    J=66.115+0.9025179*d-0.329*math.sin(V)
    
    A=1.915*math.sin(M)+0.020*math.sin(2*M)
    B=5.555*math.sin(N)+0.168*math.sin(2*N)
    
    K=math.radians(J+A-B)
    
    R=1.00014-0.01671*math.cos(M)-0.00014*math.cos(2*M)
    r=5.20872-0.25208*math.cos(N)-0.00611*math.cos(2*N)
    D=math.sqrt(r**2+R**2-2*r*R*math.cos(K))
    
    psi=math.degrees(math.asin(R/D*math.sin(K)))
    
    w1=(210.98+877.8169088*(d-D/173.)+psi-B)%360.
    w2=(187.23+870.1869088*(d-D/173.)+psi-B)%360.
    
    l=34.35+0.083091*d+0.329*math.sin(V)+B
        
    DS=3.12*math.sin(math.radians(l+42.8))
    DE=DS-2.22*math.sin(math.radians(psi))*math.cos(math.radians(l+22))-1.30*(r-D)/D*math.sin(math.radians(l-100.5))    
    
    return D,w1,w2,DE,DS
    
    
    