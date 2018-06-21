'''Meeus: Astronomical Algorithms (2nd ed.), chapter 49''' 

import math

def _corrections(jd,k):
    '''corrections to times of phases'''
    T=(jd-2451545)/36525.
    
    E=1-0.002516*T-0.0000047*T**2
    
    M=math.radians(2.5534+29.10535670*k-0.0000014*T**2-0.00000011*T**3)
    Mm=math.radians(201.5643+385.81693528*k+0.0107582*T**2+0.00001238*T**3-0.000000058*T**4)
    F=math.radians(160.7108+390.67050284*k-0.0016118*T**2-0.00000227*T**3+0.000000011*T**4)
    W=math.radians(124.7746-1.56375588*k+0.0020672*T**2+0.00000215*T**3)
    
    A=[math.degrees(299.77+0.107408*k-0.009173*T**2),math.degrees(251.88+0.016321*k),math.degrees(251.83+26.651886*k),math.degrees(349.42+36.412478*k),math.degrees(84.66+18.206239*k),\
       math.degrees(141.74+53.303771*k),math.degrees(207.14+2.453732*k),math.degrees(154.84+7.306860*k),math.degrees(34.52+27.261239*k),math.degrees(207.19+0.121824*k),\
       math.degrees(291.34+1.844379*k),math.degrees(161.72+24.198154*k),math.degrees(239.56+25.513099*k),math.degrees(331.55+3.592518*k)]
    Ac=[325,165,164,126,110,62,60,56,47,42,40,37,35,23]
    
    if (k*2)%1==0:
        #new or full moon
        args=[Mm,M,2*Mm,2*F,Mm-M,Mm+M,2*M,Mm-2*F,Mm+2*F,2*Mm+M,3*Mm,M+2*F,M-2*F,2*Mm-M,W,Mm+2*M,2*Mm-2*F,3*M,Mm+M-2*F,2*Mm+2*F,Mm+M+2*F,Mm-M+2*F,Mm-M-2*F,3*Mm+M,4*Mm]
        if k%1==0:
            #new moon
            coef=[-0.4072,0.17241*E,0.01608,0.01039,0.00739*E,-0.00514*E,0.00208*E**2,-0.00111,-0.00057,0.00056*E,-0.00042,0.00042*E,0.00038*E,-0.00024*E,-0.00017,-0.00007,0.00004,0.00004,\
                0.00003,0.00003,-0.00003,0.00003,-0.00002,-0.00002,0.00002]
        else:
            #full moon
            coef=[-0.40614,0.17302*E,0.01614,0.01043,0.00734*E,-0.00515*E,0.00209*E**2,-0.00111,-0.00057,0.00056*E,-0.00042,0.00042*E,0.00038*E,-0.00024*E,-0.00017,-0.00007,0.00004,0.00004,\
                0.00003,0.00003,-0.00003,0.00003,-0.00002,-0.00002,0.00002]
    else:
        #quaters
        args=[Mm,M,Mm+M,2*Mm,2*F,Mm-M,2*M,Mm-2*F,Mm+2*F,3*Mm,2*Mm-M,M+2*F,M-2*F,Mm+2*M,2*Mm+M,W,Mm-M-2*F,2*Mm+2*F,Mm+M+2*F,Mm-2*M,Mm+M-2*F,3*M,2*Mm-2*F,Mm-M+2*F,3*Mm+M]
        coef=[-0.62801,0.17172*E,-0.01183*E,0.00862,0.00804,0.00454*E,0.00204*E**2,-0.00180,-0.00070,0.00040,-0.00034*E,0.00032*E,0.00032*E,-0.00028*E**2,0.00027*E,-0.00017,-0.00005,0.00004,\
            -0.00004,0.00004,0.00003,0.00003,0.00002,0.00002,-0.00002]
        W=0.00306-0.00038*E*math.cos(M)+0.00026*math.cos(Mm)-0.00002*math.cos(Mm-M)+0.00002*math.cos(Mm+M)+0.00002*math.cos(2*F)
        if (k*4)%4==1: jd+=W #first quater
        else: jd-=W #last quater
        
    for i in range(len(args)): jd+=coef[i]*math.sin(args[i])
    for i in range(len(A)): jd+=Ac[i]*1e-6*math.sin(A[i])
    
    return jd    
    

def _phase(jd,k):
    '''calculate time of phase'''
    T=k/1236.85

    jd0=2451550.09766+29.530588861*k+0.00015437*T**2-0.000000150*T**3+0.00000000073*T**4
    if jd0<jd: 
        jd0+=29.530588861
        k+=1
    return jd0,k
    
def new(jd):
    '''calculate next new moon'''
    k=(((jd-2451545)/365.25)*12.3685)//1
    jd0,k=_phase(jd,k)

    return _corrections(jd0,k)

def first(jd):
    '''calculate next first quater'''
    k=(((jd-2451545)/365.25)*12.3685)//1+0.25
    jd0,k=_phase(jd,k)

    return _corrections(jd0,k)
    
def full(jd):
    '''calculate next full moon'''
    k=(((jd-2451545)/365.25)*12.3685)//1+0.5
    jd0,k=_phase(jd,k)

    return _corrections(jd0,k)
    
def last(jd):
    '''calculate next last quater'''
    k=(((jd-2451545)/365.25)*12.3685)//1+0.75
    jd0,k=_phase(jd,k)

    return _corrections(jd0,k)



def month(jd):
    '''calculate all next phases of Moon'''
    return new(jd),first(jd),full(jd),last(jd)
