'''Meeus: Astronomical Algorithms (2nd ed.), chapter 51'''

import math

def _calculate(k):
    T=k/1342.23
    
    D=math.radians(183.6380+331.73735682*k+0.0014852*T**2+0.00000209*T**3-0.000000010*T**4)
    M=math.radians(17.4006+26.82037250*k+0.0001186*T**2+0.00000006*T**3)
    Mm=math.radians(38.3776+355.52747313*k+0.0123499*T**2+0.000014627*T**3-0.000000069*T**4)
    W=math.radians(123.9767-1.44098956*k+0.0020608*T**2+0.00000214*T**3-0.000000016*T**4)
    V=math.radians(299.75+132.85*T-0.009173*T**2)
    P=W+math.radians(272.75-2.3*T)
    
    E=1-0.002516*T-0.0000047*T**2
    
    jd=2451565.1619+27.212220817*k+0.0002762*T**2+0.000000021*T**3-0.000000000088*T**4
    
    coef=[-0.4721,-0.1649,-0.0868,0.0084,-0.0083*E,-0.0039*E,0.0034,-0.0031,0.0030*E,0.0028*E,0.0026*E,0.0025,0.0024,0.0022*E,0.0017,0.0014,0.0005*E,0.0004*E,-0.0003*E,0.0003*E,0.0003,0.0003]
    args=[Mm,2*D,2*D-Mm,2*D+Mm,2*D-M,2*D-M-Mm,2*Mm,2*D-2*Mm,2*D+M,M-Mm,M,4*D,D,M+Mm,W,4*D-Mm,2*D+M-Mm,2*D-M+Mm,2*D-2*M,4*D-M,V,P]
    for i in range(len(args)):
        jd+=coef[i]*math.sin(args[i])
    return jd
    

def nodes(jd,asc=True,desc=True):
    '''calculate times of passages Moon through the Nodes'''
    k=(jd-2451561.7625)/365.25*13.4223
    
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    
    out=()
    if asc: out+=(_calculate(k0),)
    if desc: out+=(_calculate(k1),)
    if len(out)==1: out=out[0]
    
    return out