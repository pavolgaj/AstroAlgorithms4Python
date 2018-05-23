'''Meeus: Astronomical Algorithms (2nd ed.), chapter 23 '''  

import numpy as np

import nutation_ecliptic as nut

def nutation(jd,ra,dec,correction=False):
    '''correction due to nutation (with optional correction of coordinates)'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(ra,int) or isinstance(ra,float)) and (isinstance(dec,int) or isinstance(dec,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(ra,np.ndarray) or isinstance(dec,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(ra,list): ra=np.array(ra)  
    if isinstance(dec,list): dec=np.array(dec)  
    
    if out_type=='num': ra=np.array([ra])
    
    dpsi,deps=nut.nutation(jd)
    eps=nut.ecliptic(jd)    
    
    eps=np.deg2rad(eps)
    ra=np.deg2rad(ra)
    dec=np.deg2rad(dec)
      
    dra=(np.cos(eps)+np.sin(eps)*np.sin(ra)*np.tan(dec))*dpsi-(np.cos(ra)*np.tan(dec))*deps
    ddec=(np.sin(eps)*np.cos(ra))*dpsi+np.sin(ra)*deps
    
    if correction:
        dra+=np.rad2deg(ra)
        ddec+=np.rad2deg(dec)
        
    if out_type=='num':
        dra=dra[0]
        ddec=ddec[0]
    elif out_type=='lst':
        dra=dra.tolist()
        ddec=ddec.tolist()
    
    return dra,ddec


def aberration(jd,ra,dec,correction=False):
    '''correction due to aberration (with optional correction of coordinates) - for non-corrected (on precession and nutation) RA, DEC'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(ra,int) or isinstance(ra,float)) and (isinstance(dec,int) or isinstance(dec,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(ra,np.ndarray) or isinstance(dec,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(ra,list): ra=np.array(ra)  
    if isinstance(dec,list): dec=np.array(dec)  
    
    if out_type=='num': ra=np.array([ra])
    
    T=(jd-2451545)/36525.
    
    L2=3.1761467+1021.3285546*T
    L3=1.7534703+628.3075849*T
    L4=6.2034809+334.0642431*T
    L5=0.5995465+52.9690965*T
    L6=0.8740168+21.3299095*T
    L7=5.4812939+7.4781599*T
    L8=5.3118863+3.8133036*T
    L=3.8103444+8399.6847337*T
    D=5.1984667+7771.3771486*T
    M=2.3555559+8328.6914289*T
    F=1.6279052+8433.4661601*T
    
    
    args=[L3,2*L3,L5,L,3*L3,L6,F,L+M,2*L5,2*L3-L5,3*L3-8*L4+3*L5,5*L3-8*L4+3*L5,2*L2-L3,L2,L7,L3-2*L5,L8,L3+L5,2*L2-2*L3,L3-L5,4*L3,3*L3-2*L5,L2-2*L3,2*L2-3*L3,2*L6,2*L2-4*L3,3*L3-2*L4,\
        L+2*D-M,8*L2-12*L3,8*L2-14*L3,2*L4,3*L2-4*L3,2*L3-2*L5,3*L2-3*L3,2*L3-2*L4,L-2*D]
    sinX=[-1719914-2*T,6434+141*T,715,715,486-5*T,159,0,39,33,31,8,8,21,-19,17,16,16,11,0,-11,-7,-10,-9,-9,0,0,8,8,-4,-4,-6,-1,4,0,5,5]
    cosX=[-25,28007-107*T,0,0,-236-4*T,0,0,0,-10,1,-28,-28,0,0,0,0,0,-1,-11,-2,-8,0,0,0,-9,-9,0,0,-7,-7,-5,-1,-6,-7,-5,0]
    sinY=[25-13*T,25697-95*T,6,0,-216-4*T,2,0,0,-9,1,25,-25,0,0,0,0,1,-1,-10,-2,-8,0,0,0,-8,8,0,0,-6,6,-4,-2,-5,-6,-4,0]
    cosY=[1578089+156*T,-5904-130*T,-657,-656,-446+5*T,-147,26,-36,-30,-28,8,-8,-19,17,-16,15,-15,-10,0,9,6,9,-9,-8,0,0,-8,-7,4,-4,5,-7,-4,0,-5,-5]
    sinZ=[10+32*T,11141-48*T,-15,0,-94,-6,0,0,-5,0,11,-11,0,0,0,1,-3,-1,-4,-1,-3,0,0,0,-3,3,0,0,-3,3,-2,1,-2,-3,-2,0]
    cosZ=[684185-358*T,-2559-55*T,-282,-285,-193,-61,-59,-16,-13,-12,3,-3,-8,8,-7,7,-6,-5,0,4,3,4,-4,-4,0,0,-3,-3,2,-2,2,-4,-2,0,-2,-2]
    
    X=0
    Y=0
    Z=0
    
    for i in range(len(args)):
        s=np.sin(args[i])
        c=np.cos(args[i])
        
        X+=sinX[i]*s+cosX[i]*c
        Y+=sinY[i]*s+cosY[i]*c
        Z+=sinZ[i]*s+cosZ[i]*c
        
    c=17314463350.  #speed of light in 1e-8 AU per day
        
    ra=np.deg2rad(ra)
    dec=np.deg2rad(dec)
    
    dra=(Y*np.cos(ra)-X*np.sin(ra))/(c*np.cos(dec))
    ddec=-((X*np.cos(ra)+Y*np.sin(ra))*np.sin(dec)-Z*np.cos(dec))/c
    
    if correction:
        dra+=ra
        ddec+=dec
    
    dra=np.rad2deg(dra)
    ddec=np.rad2deg(ddec)
    
    if out_type=='num':
        dra=dra[0]
        ddec=ddec[0]
    elif out_type=='lst':
        dra=dra.tolist()
        ddec=ddec.tolist()
    
    return dra,ddec
    
    