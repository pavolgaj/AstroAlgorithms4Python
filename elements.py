'''Meeus: Astronomical Algorithms (2nd ed.), chapter 31'''

def _common(jd,Li,ai,ei,ii,Wi,pi):
    '''common cycle for all planets'''
    T=(jd-2451545)/36525.
    L=0
    a=0
    e=0
    i=0
    W=0
    p=0
    
    for j in range(len(Li)):
        L+=Li[j]*T**j
        a+=ai[j]*T**j
        e+=ei[j]*T**j
        i+=ii[j]*T**j
        W+=Wi[j]*T**j
        p+=pi[j]*T**j
    
    L=L%360
    i=i%360
    W=W%360
    p=p%360
    return L,a,e,i,W,p


def Mercury(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Mercury for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[252.250906,149472.6746358,-0.00000536,0.000000002]
        ai=[0.387098310,0,0,0]
        ei=[0.20563175,0.000020407,-0.0000000283,-0.00000000018]
        ii=[7.004986,-0.0059516,0.00000080,0.000000043]
        Wi=[48.330893,-0.1254227,-0.00008833,-0.000000200]
        pi=[77.456119,0.1588643,-0.00001342,-0.000000007]
    else:
        Li=[252.250906,149474.0272491,0.00030350,0.000000018]
        ai=[0.387098310,0,0,0]
        ei=[0.20563175,0.000020407,-0.0000000283,-0.00000000018]
        ii=[7.004986,0.0018215,-0.00001810,0.000000056]
        Wi=[48.330893,1.1861883,0.00017542,0.000000215]
        pi=[77.456119,1.5564776,0.00029544,0.000000009]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M


def Venus(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Venus for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[181.979801,58517.8156760,0.00000165,-0.000000002]
        ai=[0.723329820,0,0,0]
        ei=[0.00677192,-0.000047765,0.0000000981,0.00000000046]
        ii=[3.394662,-0.0008568,-0.00003244,0.000000009]
        Wi=[76.679920,-0.2780134,-0.00014257,-0.000000164]
        pi=[131.563703,0.0048746,-0.00138467,-0.000005695]
    else:
        Li=[181.979801,58519.2130302,0.00031014,0.000000015]
        ai=[0.723329820,0,0,0]
        ei=[0.00677192,-0.000047765,0.0000000981,0.00000000046]
        ii=[3.394662,0.0010037,-0.00000088,-0.000000007]
        Wi=[76.679920,0.9011206,0.00040618,-0.000000093]
        pi=[131.563703,1.4022288,-0.00107618,-0.000005678]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M


def Earth(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Earth for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[100.466457,35999.3728565,-0.00000568,-0.000000001]
        ai=[1.000001018,0,0,0]
        ei=[0.01670863,-0.000042037,-0.0000001267,0.00000000014]
        ii=[0,0.0130548,-0.00000931,-0.000000034]
        Wi=[174.873176,-0.2410908,0.00004262,0.000000001]
        pi=[102.937348,0.3225654,0.00014799,-0.000000039]
    else:
        Li=[100.466457,36000.7698278,0.00030322,0.000000020]
        ai=[1.000001018,0,0,0]
        ei=[0.01670863,-0.000042037,-0.0000001267,0.00000000014]
        ii=[0,0,0,0]
        Wi=[180,0,0,0]
        pi=[102.937348,1.7195366,0.00045688,-0.000000018]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M


def Mars(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Mars for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[355.433000,19140.2993039,0.00000262,-0.000000003]
        ai=[1.523679342,0,0,0]
        ei=[0.09340065,0.000090484,-0.0000000806,-0.00000000025]
        ii=[1.849726,-0.0081477,-0.00002255,-0.000000029]
        Wi=[49.558093,-0.2950250,-0.00064048,-0.000001964]
        pi=[336.060234,0.4439016,-0.00017313,0.000000518]
    else:
        Li=[355.433000,19141.6964471,0.00031052,0.000000016]
        ai=[1.523679342,0,0,0]
        ei=[0.09340065,0.000090484,-0.0000000806,-0.00000000025]
        ii=[1.849726,-0.0006011,0.00001276,-0.000000007]
        Wi=[49.558093,0.7720959,0.00001557,0.000002267]
        pi=[336.060234,1.8410449,0.00013477,0.000000536]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M


def Jupiter(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Jupiter for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[34.351519,3034.9056606,-0.00008501,0.000000016]
        ai=[5.202603209,0.0000001913,0,0]
        ei=[0.04849793,0.000163225,-0.0000004714,-0.00000000201]
        ii=[1.303267,-0.0019877,0.00003320,0.000000097]
        Wi=[100.464407,0.1767232,0.00090700,-0.000007272]
        pi=[14.331207,0.2155209,0.00072211,-0.000004485]
    else:
        Li=[34.351519,3036.3027748,0.00022330,0.000000037]
        ai=[5.202603209,0.0000001913,0,0]
        ei=[0.04849793,0.000163225,-0.0000004714,-0.00000000201]
        ii=[1.303267,-0.0054965,0.00000466,-0.000000002]
        Wi=[100.464407,1.0209774,0.00040315,0.000000404]
        pi=[14.331207,1.6126352,0.00103042,-0.000004464]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M    


def Saturn(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Saturn for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[50.077444,1222.1138488,0.00021004,-0.000000046]
        ai=[9.554909192,-0.0000021930,0.000000004,0]
        ei=[0.05554814,-0.000346641,-0.0000006436,0.00000000340]
        ii=[2.488879,0.0025514,-0.00004906,0.000000017]
        Wi=[113.665503,-0.2566722,-0.00018399,0.000000480]
        pi=[93.057237,0.5665415,0.00052850,0.000004912]
    else:
        Li=[50.077444,1223.5110686,0.00051908,-0.000000030]
        ai=[9.554909192,-0.0000021930,0.000000004,0]
        ei=[0.05554814,-0.000346641,-0.0000006436,0.00000000340]
        ii=[2.488879,-0.0037362,-0.00001519,0.000000087]
        Wi=[113.665503,0.8770880,-0.00012176,-0.000002249]
        pi=[93.057237,1.9637613,0.00083753,0.000004928]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M     


def Uranus(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Uranus for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[314.055005,428.4669983,-0.00000486,0.000000006]
        ai=[19.218446062,-0.0000000372,0.00000000098,0]
        ei=[0.04638122,-0.000027293,0.0000000789,0.00000000024]
        ii=[0.773197,-0.0016869,0.00000349,0.000000016]
        Wi=[74.005957,0.0741431,0.00040539,0.000000119]
        pi=[173.005291,0.0893212,-0.00009470,0.000000414]
    else:
        Li=[314.055005,429.8640561,0.00030390,0.000000026]
        ai=[19.218446062,-0.0000000372,0.00000000098,0]
        ei=[0.04638122,-0.000027293,0.0000000789,0.00000000024]
        ii=[0.773197,0.0007744,0.00003749,-0.000000092]
        Wi=[74.005957,0.5211278,0.00133947,0.000018484]
        pi=[173.005291,1.4863790,0.00021406,0.000000434]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M    


def Neptune(jd,j2k=True):
    '''orbital elements (mean longitude, semimajor axis, eccentricity, inclination, long. of ascedinf node, long. of perihelium, arg. of perihelium, mean anomaly) of Neptune for equinox J2000.0 or mean equinox'''
    if j2k:
        Li=[304.348665,218.4862002,0.00000059,-0.000000002]
        ai=[30.110386869,-0.0000001663,0.00000000069,0]
        ei=[0.00945575,0.000006033,0,-0.00000000005]
        ii=[1.769953,0.0002256,0.00000023,0]
        Wi=[131.784057,-0.0061651,-0.00000219,-0.000000078]
        pi=[48.120276,0.0291866,0.00007610,0]
    else:
        Li=[304.348665,219.8833092,0.00030882,0.00000018]
        ai=[30.110386869,-0.0000001663,0.00000000069,0]
        ei=[0.00945575,0.000006033,0,-0.00000000005]
        ii=[1.769953,-0.0093082,-0.00000708,0.000000027]
        Wi=[131.784057,1.1022039,0.00025952,-0.000000637]
        pi=[48.120276,1.4262957,0.00038434,0.000000020]
    
    L,a,e,i,W,p=_common(jd,Li,ai,ei,ii,Wi,pi)
    w=p-W
    if w<0: w+=360
    
    M=L-p
    if M<0: M+=360
    return L,a,e,i,W,p,w,M   
