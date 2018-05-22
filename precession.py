'''Meeus: Astronomical Algorithms (2nd ed.), chapter 21'''

#import numpy as np
import math

def precession(jd,jd0,ra,dec):
    '''calculate precession of (ra,dec) from epoch jd0 to jd'''
    T=(jd0-2451545)/36525.
    t=(jd-jd0)/36525.
    
    s=math.radians(((2306.2181+1.39656*T-0.000139*T**2)*t+(0.30188-0.000344*T)*t**2+0.017998*t**3)/3600.)
    z=math.radians(((2306.2181+1.39656*T-0.000139*T**2)*t+(1.09468+0.000066*T)*t**2+0.018203*t**3)/3600.)
    th=math.radians(((2004.3109-0.85330*T-0.000217*T**2)*t-(0.42665+0.000217*T)*t**2-0.041833*t**3)/3600.)
    
    ra=math.radians(ra)
    dec=math.radians(dec)
    
    A=math.cos(dec)*math.sin(ra+s)
    B=math.cos(th)*math.cos(dec)*math.cos(ra+s)-math.sin(th)*math.sin(dec)
    C=math.sin(th)*math.cos(dec)*math.cos(ra+s)+math.cos(th)*math.sin(dec)
    
    ra=math.degrees(z+math.atan2(A,B))
    dec=math.degrees(math.asin(C))
    
    return ra,dec

def ecliptic(jd,jd0,lam,bet):
    '''calculate precession of (lam,bet) from epoch jd0 to jd'''
    T=(jd0-2451545)/36525.
    t=(jd-jd0)/36525.
    
    n=math.radians(((47.0029-0.06603*T+0.000598*T**2)*t+(-0.03302+0.000598*T)*t**2+0.000060*t**3)/3600.)
    P=math.radians(174.876384+(3289.4789*T+0.60622*T**2-(869.8089+0.50491*T)*t+0.03536*t**2)/3600.)
    p=math.radians(((5029.0966-2.22226*T-0.000042*T**2)*t+(1.11113-0.000042*T)*t**2-0.000006*t**3)/3600.)
    
    lam=math.radians(lam)
    bet=math.radians(bet)
    
    A=math.cos(n)*math.cos(bet)*math.sin(P-lam)-math.sin(n)*math.sin(bet)
    B=math.cos(bet)*math.cos(P-lam)
    C=math.cos(n)*math.sin(bet)+math.sin(n)*math.cos(bet)*math.sin(P-lam)
    
    lam=math.degrees(p+P-math.atan2(A,B))
    bet=math.degrees(math.asin(C))
    
    return lam,bet