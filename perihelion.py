'''Meeus: Astronomical Algorithms (2nd ed.), chapter 38'''

def Mercury(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Mercury'''
    k=4.15201*(jd-2451590.257)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2451590.257+87.96934963*k0,)
    if aphe: out+=(2451590.257+87.96934963*k1,)
    if len(out)==1: return out[0]
    return out

def Venus(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Venus'''
    k=1.62549*(jd-2451738.233)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2451738.233+224.7008188*k0-0.0000000327*k0**2,)
    if aphe: out+=(2451738.233+224.7008188*k1-0.0000000327*k1**2,)
    if len(out)==1: return out[0]
    return out

def Earth(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Earth'''
    k=0.99997*(jd-2451547.507)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2451547.507+365.2596358*k0+0.0000000156*k0**2,)
    if aphe: out+=(2451547.507+365.2596358*k1+0.0000000156*k1**2,)
    if len(out)==1: return out[0]
    return out

def Mars(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Mars'''
    k=0.53166*(jd-2452195.026)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2452195.026+686.9957857*k0-0.0000001187*k0**2,)
    if aphe: out+=(2452195.026+686.9957857*k1-0.0000001187*k1**2,)
    if len(out)==1: return out[0]
    return out

def Jupiter(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Jupiter'''
    k=0.08430*(jd-2455636.936)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2455636.936+4332.897065*k0+0.0001367*k0**2,)
    if aphe: out+=(2455636.936+4332.897065*k1+0.0001367*k1**2,)
    if len(out)==1: return out[0]
    return out

def Saturn(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Saturn'''
    k=0.03393*(jd-2452830.120)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2452830.120+10764.21676*k0+0.000827*k0**2,)
    if aphe: out+=(2452830.120+10764.21676*k1+0.000827*k1**2,)
    if len(out)==1: return out[0]
    return out

def Uranus(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Uranus'''
    k=0.01190*(jd-2470213.500)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2470213.500+30694.8767*k0-0.00541*k0**2,)
    if aphe: out+=(2470213.500+30694.8767*k1-0.00541*k1**2,)
    if len(out)==1: return out[0]
    return out

def Neptune(jd,peri=True,aphe=True):
    '''perihelion and aphelion of Neptune'''
    k=0.00607*(jd-2468895.100)/365.25
    k0=k//1+1
    if k0-k>=0.5: k1=k0-0.5
    else: k1=k0+0.5
    out=()
    if peri: out+=(2468895.100+60190.33*k0+0.03429*k0**2,)
    if aphe: out+=(2468895.100+60190.33*k1+0.03429*k1**2,)
    if len(out)==1: return out[0]
    return out
