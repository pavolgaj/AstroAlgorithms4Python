'''Meeus: Astronomical Algorithms (2nd ed.), chapter 52'''

import math

def _common(k):
    '''some common values'''
    T=k/1336.86
    
    D=333.0705546*k-0.0004214*T**2+0.00000011*T**3
    M=26.9281592*k-0.00003555*T**2-0.00000010*T**3
    Mm=356.9562794*k+0.0103066*T**2+0.00001251*T**3
    F=1.4467807*k-0.0020690*T**2-0.00000215*T**3
    
    E=1-0.002516*T-0.0000047*T**2
    
    jd=27.321582247*k+0.000119804*T**2-0.000000141*T**3
    dec=23.6961-0.013004*T
    
    return D,M,Mm,F,E,jd,dec
    

def north(jd0):
    '''maximum northern declination'''
    k=(jd0-2451554.4575)/365.25*13.3686
    
    k=k//1+1
    
    D,M,Mm,F,E,jd,dec=_common(k)
    
    D=math.radians(152.2029+D)
    M=math.radians(14.8591+M)
    Mm=math.radians(4.6881+Mm)
    F=math.radians(325.8867+F)
    
    jd+=2451562.5897
    
    coef=[0.8975,-0.4726,-0.1030,-0.0976,-0.0462,-0.0461,-0.0438,0.0162*E,-0.0157,0.0145,0.0136,-0.0095,-0.0091,-0.0089,0.0075,-0.0068,0.0061,-0.0047,-0.0043*E,-0.0040,-0.0037,0.0031,0.0030,\
        -0.0029,-0.0029*E,-0.0027,0.0024*E,-0.0021,0.0019,0.0018,0.0018,0.0017,0.0017,-0.0014,0.0013,0.0013,0.0012,0.0011,-0.0011,0.0010,0.0010*E,-0.0009,0.0007,-0.0007]
    args=[F,Mm,2*F,2*D-Mm,Mm-F,Mm+F,2*D,M,3*F,Mm+2*F,2*D-F,2*D-Mm-F,2*D-Mm+F,2*D+F,2*Mm,Mm-2*F,2*Mm-F,Mm+3*F,2*D-M-Mm,Mm-2*F,2*D-2*Mm,F,2*D+Mm,Mm+2*F,2*D-M,Mm+F,M-Mm,Mm-3*F,2*Mm+F,2*D-2*Mm-F,\
        3*F,Mm+3*F,2*Mm,2*D-Mm,2*D+Mm+F,Mm,3*Mm+F,2*D-Mm+F,2*D-2*Mm,D+F,M+Mm,2*D-2*F,2*Mm+F,3*Mm+F]
    func=[math.cos,math.sin,math.sin,math.sin,math.cos,math.cos,math.sin,math.sin,math.cos,math.sin,math.cos,math.cos,math.cos,math.cos,math.sin,math.sin,math.cos,math.sin,math.sin,math.cos,\
        math.sin,math.sin,math.sin,math.cos,math.sin,math.sin,math.sin,math.sin,math.sin,math.cos,math.sin,math.cos,math.cos,math.cos,math.cos,math.cos,math.sin,math.sin,math.cos,math.cos,\
        math.sin,math.sin,math.cos,math.cos]
    
    for i in range(len(args)): jd+=coef[i]*func[i](args[i])
    
    coef=[5.1093,0.2658,0.1448,-0.0322,0.0133,0.0125,-0.0124,-0.0101,0.0097,-0.0087*E,0.0074,0.0067,0.0063,0.0060*E,-0.0057,-0.0056,0.0052,0.0041,-0.0040,0.0038,-0.0034,-0.0029,0.0029,-0.0028*E,\
        -0.0028,-0.0023,-0.0021,0.0019,0.0018,0.0017,0.0015,0.0014,-0.0012,-0.0012,-0.0010,-0.0010,0.0006]
    args=[F,2*F,2*D-F,3*F,2*D-2*F,2*D,Mm-F,Mm+2*F,F,2*D+M-F,Mm+3*F,D+F,Mm-2*F,2*D-M-F,2*D-Mm-F,Mm+F,Mm+2*F,2*Mm+F,Mm-3*F,2*Mm-F,Mm-2*F,2*Mm,3*Mm+F,2*D+M-F,Mm-F,3*F,2*D+F,Mm+3*F,D+F,2*Mm-F,\
        3*Mm+F,2*D+2*Mm+F,2*D-2*Mm-F,2*Mm,Mm,2*F,Mm+F]
    func=[math.sin,math.cos,math.sin,math.sin,math.cos,math.cos,math.sin,math.sin,math.cos,math.sin,math.sin,math.sin,math.sin,math.sin,math.sin,math.cos,math.cos,math.cos,math.cos,math.cos,\
        math.cos,math.sin,math.sin,math.cos,math.cos,math.cos,math.sin,math.cos,math.cos,math.sin,math.cos,math.cos,math.sin,math.cos,math.cos,math.sin,math.sin]

    for i in range(len(args)): dec+=coef[i]*func[i](args[i])
    
    return jd,dec


def south(jd0):
    '''maximum southern declination'''
    k=(jd0-2451554.4575)/365.25*13.3686
    
    k=k//1+1
    
    D,M,Mm,F,E,jd,dec=_common(k)
    
    D=math.radians(345.6676+D)
    M=math.radians(1.3951+M)
    Mm=math.radians(186.2100+Mm)
    F=math.radians(145.1633+F)
    
    jd+=2451548.9289
    
    coef=[-0.8975,-0.4726,-0.1030,-0.0976,0.0541,0.0516,-0.0438,0.0112*E,0.0157,0.0023,-0.0136,0.0110,0.0091,0.0089,0.0075,-0.0030,-0.0061,-0.0047,-0.0043*E,0.0040,-0.0037,-0.0031,0.0030,0.0029,\
        -0.0029*E,-0.0027,0.0024*E,-0.0021,-0.0019,-0.0006,-0.0018,-0.0017,0.0017,0.0014,-0.0013,-0.0013,0.0012,0.0011,0.0011,0.0010,0.0010*E,-0.0009,-0.0007,-0.0007]
    args=[F,Mm,2*F,2*D-Mm,Mm-F,Mm+F,2*D,M,3*F,Mm+2*F,2*D-F,2*D-Mm-F,2*D-Mm+F,2*D+F,2*Mm,Mm-2*F,2*Mm-F,Mm+3*F,2*D-M-Mm,Mm-2*F,2*D-2*Mm,F,2*D+Mm,Mm+2*F,2*D-M,Mm+F,M-Mm,Mm-3*F,2*Mm+F,2*D-2*Mm-F,\
        3*F,Mm+3*F,2*Mm,2*D-Mm,2*D+Mm+F,Mm,3*Mm+F,2*D-Mm+F,2*D-2*Mm,D+F,M+Mm,2*D-2*F,2*Mm+F,3*Mm+F]
    func=[math.cos,math.sin,math.sin,math.sin,math.cos,math.cos,math.sin,math.sin,math.cos,math.sin,math.cos,math.cos,math.cos,math.cos,math.sin,math.sin,math.cos,math.sin,math.sin,math.cos,\
        math.sin,math.sin,math.sin,math.cos,math.sin,math.sin,math.sin,math.sin,math.sin,math.cos,math.sin,math.cos,math.cos,math.cos,math.cos,math.cos,math.sin,math.sin,math.cos,math.cos,\
        math.sin,math.sin,math.cos,math.cos]
    
    for i in range(len(args)): jd+=coef[i]*func[i](args[i])
    
    coef=[-5.1093,0.2658,-0.1448,0.0322,0.0133,0.0125,-0.0015,0.0101,-0.0097,0.0087*E,0.0074,0.0067,-0.0063,-0.0060*E,0.0057,-0.0056,-0.0052,-0.0041,-0.0040,-0.0038,0.0034,-0.0029,0.0029,\
        0.0028*E,-0.0028,0.0023,0.0021,0.0019,0.0018,-0.0017,0.0015,0.0014,0.0012,-0.0012,0.0010,-0.0010,0.0037]
    args=[F,2*F,2*D-F,3*F,2*D-2*F,2*D,Mm-F,Mm+2*F,F,2*D+M-F,Mm+3*F,D+F,Mm-2*F,2*D-M-F,2*D-Mm-F,Mm+F,Mm+2*F,2*Mm+F,Mm-3*F,2*Mm-F,Mm-2*F,2*Mm,3*Mm+F,2*D+M-F,Mm-F,3*F,2*D+F,Mm+3*F,D+F,2*Mm-F,\
        3*Mm+F,2*D+2*Mm+F,2*D-2*Mm-F,2*Mm,Mm,2*F,Mm+F]
    func=[math.sin,math.cos,math.sin,math.sin,math.cos,math.cos,math.sin,math.sin,math.cos,math.sin,math.sin,math.sin,math.sin,math.sin,math.sin,math.cos,math.cos,math.cos,math.cos,math.cos,\
        math.cos,math.sin,math.sin,math.cos,math.cos,math.cos,math.sin,math.cos,math.cos,math.sin,math.cos,math.cos,math.sin,math.cos,math.cos,math.sin,math.sin]
    
    for i in range(len(args)): dec+=coef[i]*func[i](args[i])
    
    return jd,-dec

    
    
    
