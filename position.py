'''Meeus: Astronomical Algorithms (2nd ed.), chapter 32''' 
'''using VSOP87 data from http://cdsarc.u-strasbg.fr/viz-bin/Cat?cat=VI%2F81&target=brief&'''

import math

def _load(name,jd):
    T=(jd-2451545.0)/365250.
    
    f=open(name,'r')
    
    L=0
    B=0
    r=0
    tmp=0

    for l in f:
        temp=l.split()
        try: float(temp[0])
        except:
            if abs(tmp)>0: 
                if v==1: L+=tmp*T**n
                elif v==2: B+=tmp*T**n
                elif v==3: r+=tmp*T**n
            i=l.find('**')
            n=int(l[i+2:i+4])
            i=l.find('VARIABLE')
            v=int(l[i+8:i+11])
            tmp=0
            continue
        tmp+=float(temp[-3])*math.cos(float(temp[-2])+float(temp[-1])*T)
    if v==1: L+=tmp*T**n
    elif v==2: B+=tmp*T**n
    elif v==3: r+=tmp*T**n
    f.close()
    
    Ll=L-math.radians(1.397*T+0.00031*T**2)
    L+=math.radians((-0.09033+0.03916*(math.cos(Ll)+math.sin(Ll))*math.tan(B))/3600.)
    B+=math.radians(0.03916*(math.cos(Ll)-math.sin(Ll))/3600.)
    
    L=math.degrees(L)%360
    B=math.degrees(B)%360
    
    if B>180: B-=360
    
    return L,B,r

def Mercury(jd):
    '''heliocentric coordinates of Mercury'''
    return _load('vsop87/VSOP87B.mer',jd)    

def Venus(jd):
    '''heliocentric coordinates of Venus'''
    return _load('vsop87/VSOP87B.ven',jd)    

def Earth(jd):
    '''heliocentric coordinates of Earth'''
    return _load('vsop87/VSOP87B.ear',jd)

def Mars(jd):
    '''heliocentric coordinates of Mars'''
    return _load('vsop87/VSOP87B.mar',jd)

def Jupiter(jd):
    '''heliocentric coordinates of Jupiter'''
    return _load('vsop87/VSOP87B.jup',jd)

def Saturn(jd):
    '''heliocentric coordinates of Saturn'''
    return _load('vsop87/VSOP87B.sat',jd)

def Uranus(jd):
    '''heliocentric coordinates of Uranus'''
    return _load('vsop87/VSOP87B.ura',jd)

def Neptune(jd):
    '''heliocentric coordinates of Neptune'''
    return _load('vsop87/VSOP87B.nep',jd)
    