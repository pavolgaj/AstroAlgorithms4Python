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
    
    return L,B,r

def Mercury(jd):
    '''heliocentric coordinates of Mercury'''
    L,B,r=_load('vsop87/VSOP87B.mer',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Venus(jd):
    '''heliocentric coordinates of Venus'''
    L,B,r=_load('vsop87/VSOP87B.ven',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Earth(jd):
    '''heliocentric coordinates of Earth'''
    L,B,r=_load('vsop87/VSOP87B.ear',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Mars(jd):
    '''heliocentric coordinates of Mars'''
    L,B,r=_load('vsop87/VSOP87B.mar',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Jupiter(jd):
    '''heliocentric coordinates of Jupiter'''
    L,B,r=_load('vsop87/VSOP87B.jup',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Saturn(jd):
    '''heliocentric coordinates of Saturn'''
    L,B,r=_load('vsop87/VSOP87B.sat',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Uranus(jd):
    '''heliocentric coordinates of Uranus'''
    L,B,r=_load('vsop87/VSOP87B.ura',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r

def Neptune(jd):
    '''heliocentric coordinates of Neptune'''
    L,B,r=_load('vsop87/VSOP87B.nep',jd)
    return math.degrees(L)%360,math.degrees(B)%360,r
    