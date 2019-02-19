'''Meeus: Astronomical Algorithms (2nd ed.), chapter 53 '''

import math

import moon
import nutation_ecliptic
import sidereal

I=math.radians(1.54242)   #inclination of mean lunar equator to ecliptic

def optical(jd):
    '''optical librations of Moon'''
    T=(jd-2451545)/36525.
    
    F=math.radians(93.2720950+483202.0175233*T-0.0036539*T**2-T**3/3526000.+T**4/863310000.)
    w=math.radians(125.0445479-1934.1362891*T+0.0020754*T**2+T**3/467441.-T**4/60616000.)
    
    ra,dec,lon,lat,dist,par=moon.position(jd,full=True)
    psi,eps=nutation_ecliptic.nutation(jd)
    
    lon=math.radians(lon)
    lat=math.radians(lat)
    psi=math.radians(psi)
    
    W=lon-psi-w
    A=math.atan2(math.sin(W)*math.cos(lat)*math.cos(I)-math.sin(lat)*math.sin(I),math.cos(W)*math.cos(lat))
    
    l=math.degrees(A-F)%360
    if l>180: l-=360
    
    b=math.degrees(math.asin(-math.sin(W)*math.cos(lat)*math.sin(I)-math.sin(lat)*math.cos(I)))%360
    if b>180: b-=360
    
    return l,b


def physical(jd):
    '''physcial librations of Moon'''
    T=(jd-2451545)/36525.
    
    D=math.radians(297.8501921+445267.1114034*T-0.0018819*T**2+T**3/545868.-T**4/113065000.)
    M=math.radians(357.5291092+35999.0502909*T-0.0001536*T**2+T**3/24490000.)
    Mm=math.radians(134.9633964+477198.8675055*T+0.0087414*T**2+T**3/69699.-T**4/14712000.)
    F=math.radians(93.2720950+483202.0175233*T-0.0036539*T**2-T**3/3526000.+T**4/863310000.)
    W=math.radians(125.0445479-1934.1362891*T+0.0020754*T**2+T**3/467441.-T**4/60616000.)
    
    E=1-0.002516*T-0.0000047*T**2
    
    K1=math.radians(119.75+131.849*T)
    K2=math.radians(72.56+20.186*T)
    
    rho=-0.02752*math.cos(Mm)-0.02245*math.sin(F)+0.00684*math.cos(Mm-2*F)-0.00293*math.cos(2*F)-0.00085*math.cos(2*F-2*D)-0.00054*math.cos(Mm-2*D)-0.00020*math.sin(Mm+F)-0.00020*math.cos(Mm+2*F)\
        -0.00020*math.cos(Mm-F)+0.00014*math.cos(Mm+2*F-2*D)
    sig=-0.02816*math.sin(Mm)+0.02244*math.cos(F)-0.00682*math.sin(Mm-2*F)-0.00279*math.sin(2*F)-0.00083*math.sin(2*F-2*D)+0.00069*math.sin(Mm-2*D)+0.00040*math.cos(Mm+F)-0.00025*math.sin(2*Mm)\
        -0.00023*math.sin(Mm+2*F)+0.00020*math.cos(Mm-F)+0.00019*math.sin(Mm-F)+0.00013*math.sin(Mm+2*F-2*D)-0.00010*math.cos(Mm-3*F)
    tau=0.02520*E*math.sin(M)+0.00473*math.sin(2*Mm-2*F)-0.00467*math.sin(Mm)+0.00396*math.sin(K1)+0.00276*math.sin(2*Mm-2*D)+0.00196*math.sin(W)-0.00183*math.cos(Mm-F)+0.00115*math.sin(Mm-2*D)\
        -0.00096*math.sin(Mm-D)+0.00046*math.sin(2*F-2*D)-0.00039*math.sin(Mm-F)-0.00032*E*math.sin(Mm-M-D)+0.00027*E*math.sin(2*Mm-M-2*D)+0.00023*math.sin(K2)-0.00014*math.sin(2*D)\
        +0.00014*math.cos(2*Mm-2*F)-0.00012*math.sin(Mm-2*F)-0.00012*math.sin(2*Mm)+0.00011*E*math.sin(2*Mm-2*M-2*D)
    
    l1,b1=optical(jd)
    A=math.radians(l1)+F
    
    l=-tau+(rho*math.cos(A)+sig*math.sin(A))*math.tan(math.radians(b1))
    b=sig*math.cos(A)-rho*math.sin(A)
    
    return l,b
    

def topocentric(jd,lon,lat,correct=True):
    '''topocentric libration of Moon'''
    ra,dec,lon1,lat1,dist,par=moon.position(jd,full=True)
    
    sid=sidereal.sid_time(jd)
    
    ha=math.radians(sid-ra)
    dec=math.radians(dec)
    par=math.radians(par)
    
    Q=math.atan2(math.cos(lat)*math.sin(ha),math.cos(dec)*math.sin(lat)-math.sin(dec)*math.cos(lat)*math.cos(ha))
    z=math.acos(math.sin(dec)*math.sin(lat)+math.cos(dec)*math.cos(lat)*math.cos(ha))
    pi=par*(math.sin(z)+0.0084*math.sin(2*z))
    
    T=(jd-2451545)/36525.
    
    D=math.radians(297.8501921+445267.1114034*T-0.0018819*T**2+T**3/545868.-T**4/113065000.)
    Mm=math.radians(134.9633964+477198.8675055*T+0.0087414*T**2+T**3/69699.-T**4/14712000.)
    F=math.radians(93.2720950+483202.0175233*T-0.0036539*T**2-T**3/3526000.+T**4/863310000.)
    W=math.radians(125.0445479-1934.1362891*T+0.0020754*T**2+T**3/467441.-T**4/60616000.)

    rho=-0.02752*math.cos(Mm)-0.02245*math.sin(F)+0.00684*math.cos(Mm-2*F)-0.00293*math.cos(2*F)-0.00085*math.cos(2*F-2*D)-0.00054*math.cos(Mm-2*D)-0.00020*math.sin(Mm+F)-0.00020*math.cos(Mm+2*F)\
        -0.00020*math.cos(Mm-F)+0.00014*math.cos(Mm+2*F-2*D)
    sig=-0.02816*math.sin(Mm)+0.02244*math.cos(F)-0.00682*math.sin(Mm-2*F)-0.00279*math.sin(2*F)-0.00083*math.sin(2*F-2*D)+0.00069*math.sin(Mm-2*D)+0.00040*math.cos(Mm+F)-0.00025*math.sin(2*Mm)\
        -0.00023*math.sin(Mm+2*F)+0.00020*math.cos(Mm-F)+0.00019*math.sin(Mm-F)+0.00013*math.sin(Mm+2*F-2*D)-0.00010*math.cos(Mm-3*F)
    
    psi,eps=nutation_ecliptic.nutation(jd)
    eps=math.radians(eps+nutation_ecliptic.ecliptic(jd))
    
    V=W+math.radians(psi+sig/math.sin(I))
    X=math.sin(I+rho)*math.sin(V)
    Y=math.sin(I+rho)*math.cos(V)*math.cos(eps)-math.cos(I+rho)*math.sin(eps)
    
    l,b=optical(jd)
    l1,b1=physical(jd)
    
    w=math.atan2(X,Y)
    P=math.asin(math.sqrt(X**2+Y**2)*math.cos(math.radians(ra)-w)/math.cos(math.radians(b+b1)))
    
    dl=-pi*math.sin(Q-P)/math.cos(b)
    db=pi*math.cos(Q-P)
    
    if correct: return l+l1+dl,b+b1+db

    return dl,db
    
