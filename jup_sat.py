'''Meeus: Astronomical Algorithms (2nd ed.), chapter 44''' 

import math

def _common(jd):
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
    
    l=34.35+0.083091*d+0.329*math.sin(V)+B
        
    DS=3.12*math.sin(math.radians(l+42.8))
    DE=math.radians(DS-2.22*math.sin(math.radians(psi))*math.cos(math.radians(l+22))-1.30*(r-D)/D*math.sin(math.radians(l-100.5)))
    
    return d-D/173.,psi-B,DE

def Io(jd):
    '''position of moon Io in units of Jupiter's equatorial radius'''
    dt,pB,DE=_common(jd)
    
    u=math.radians(163.8069+203.4058646*dt+pB)
    u2=math.radians(358.4140+101.2916335*dt+pB)
    
    u+=math.radians(0.473*math.sin(2*(u-u2)))
    r=5.9057-0.0244*math.cos(2*(u-u2))
    
    x=r*math.sin(u)
    y=-r*math.cos(u)*math.sin(DE)
    
    return x,y

def Europe(jd):
    '''position of moon Europe in units of Jupiter's equatorial radius'''
    dt,pB,DE=_common(jd)
    
    u=math.radians(358.4140+101.2916335*dt+pB)
    u3=math.radians(5.7176+50.2345180*dt+pB)
    
    u+=math.radians(1.065*math.sin(2*(u-u3)))
    r=9.3966-0.0882*math.cos(2*(u-u3))
    
    x=r*math.sin(u)
    y=-r*math.cos(u)*math.sin(DE)
    
    return x,y    

def Ganymede(jd):
    '''position of moon Ganymede in units of Jupiter's equatorial radius'''
    dt,pB,DE=_common(jd)

    u=math.radians(5.7176+50.2345180*dt+pB)
    G=math.radians(331.18+50.310482*dt)
    
    u+=math.radians(0.165*math.sin(G))
    r=14.9883-0.0216*math.cos(G)
    
    x=r*math.sin(u)
    y=-r*math.cos(u)*math.sin(DE)
    
    return x,y    

def Callisto(jd):
    '''position of moon Ganymedes in units of Jupiter's equatorial radius'''
    dt,pB,DE=_common(jd)

    u=math.radians(224.8092+21.4879800*dt+pB)
    H=math.radians(87.45+21.569231*dt)
    
    u+=math.radians(0.843*math.sin(H))
    r=26.3627-0.1939*math.cos(H)
    
    x=r*math.sin(u)
    y=-r*math.cos(u)*math.sin(DE)
    
    return x,y  
