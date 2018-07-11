'''Meeus: Astronomical Algorithms (2nd ed.), chapter 54'''  

import math

import moon_phases

def _common(jd,k):
    T=(jd-2451545)/36525.
    
    F=math.radians(160.7108+390.67050284*k-0.0016118*T**2-0.00000227*T**3+0.000000011*T**4)
    
    E=1-0.002516*T-0.0000047*T**2
    
    M=math.radians(2.5534+29.10535670*k-0.0000014*T**2-0.00000011*T**3)
    Mm=math.radians(201.5643+385.81693528*k+0.0107582*T**2+0.00001238*T**3-0.000000058*T**4)
    W=math.radians(124.7746-1.56375588*k+0.0020672*T**2+0.00000215*T**3)
    
    F1=F-math.radians(0.02665)*math.sin(W)
    
    P=0.2070*E*math.sin(M)+0.0024*E*math.sin(2*M)-0.0392*math.sin(Mm)+0.0116*math.sin(2*Mm)-0.0073*E*math.sin(Mm+M)+0.0067*E*math.sin(Mm-M)+0.0118*math.sin(2*F1)
    Q=5.2207-0.0048*E*math.cos(M)+0.0020*E*math.cos(2*M)-0.3299*math.cos(Mm)-0.0060*E*math.cos(Mm+M)+0.0041*E*math.cos(Mm-M)
    
    W=abs(math.cos(F1))
    g=(P*math.cos(F1)+Q*math.sin(F1))*(1-0.0048*W)
    u=0.0059+0.0046*E*math.cos(M)-0.0182*math.cos(Mm)+0.0004*math.cos(2*Mm)-0.0005*E*math.cos(M+Mm)
    
    return u,g,Mm

def lunar(jd0,full=False):
    '''find next lunar eclipse'''
    jd=moon_phases.full(jd0) 
    k=(((jd-2451545)/365.25)*12.3685)//1+0.5
        
    found=False
    while not found:
        T=(jd-2451545)/36525.        
        F=math.radians(160.7108+390.67050284*k-0.0016118*T**2-0.00000227*T**3+0.000000011*T**4)
        while abs(math.sin(F))>0.36:
            jd+=29.530588861
            T=(jd-2451545)/36525.
            k+=1
            F=math.radians(160.7108+390.67050284*k-0.0016118*T**2-0.00000227*T**3+0.000000011*T**4)
        
        jd=moon_phases.full(jd-1)     
        
        u,g,Mm=_common(jd,k)
    
        mp=(1.5573+u-abs(g))/0.5450
        if mp<0:
            jd+=29.530588861
            k+=1
        else: found=True
    
    if not full: return jd
    
    mu=(1.0128-u-abs(g))/0.5450
    
    p=1.0128-u
    t=0.4687-u
    n=0.5458+0.0400*math.cos(Mm)
    
    pt=1./n*math.sqrt(p**2-g**2)/24.
    tt=1./n*math.sqrt(t**2-g**2)/24.
    
    h=1.5573+u
    put=1./n*math.sqrt(h**2-g**2)/24.
    
    info={}
    info['max']=jd
    info['P1']=jd-put
    info['P4']=jd+put
    if mu<0:
        info['type']='penumbral'
        info['mag']=mp
    else:
        info['mag']=mu
        info['U1']=jd-pt
        info['U4']=jd+pt
        if mu<1: info['type']='partial'
        else:
            info['type']='total'
            info['U2']=jd-tt
            info['U3']=jd+tt        
    
    return info
    


def solar(jd0,full=False):
    '''find next solar eclipse'''
    jd=moon_phases.new(jd0)     
    k=(((jd-2451545)/365.25)*12.3685)//1
        
    found=False
    while not found:
        T=(jd-2451545)/36525. 
        F=math.radians(160.7108+390.67050284*k-0.0016118*T**2-0.00000227*T**3+0.000000011*T**4)
        
        while abs(math.sin(F))>0.36:
            jd+=29.530588861
            T=(jd-2451545)/36525.
            k+=1
            F=math.radians(160.7108+390.67050284*k-0.0016118*T**2-0.00000227*T**3+0.000000011*T**4)
        
        jd=moon_phases.new(jd-1)
        
        u,g,Mm=_common(jd,k)
        
        if abs(g)>1.5433+u:
            jd+=29.530588861
            k+=1
        else: found=True

    if not full: return jd

    mag=(1.5433+u-abs(g))/(0.5461+2*u)
    
    info={}
    info['max']=jd
    info['mag']=mag
    
    if abs(g)>=0.9972+abs(u): info['type']='partial'
    elif abs(g)>0.9972: info['type']='non-central annular/total'
    elif u<0: info['type']='total'
    elif u>0.0047: info['type']='annular'
    elif u<0.00464*math.sqrt(1-g**2): info['type']='hybrid'
    else: info['type']='annular'
    
    return info
    

