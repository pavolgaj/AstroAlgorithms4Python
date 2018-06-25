'''Meeus: Astronomical Algorithms (2nd ed.), chapter 13'''

import numpy as np

from constants import *

def local_sid(sid,lon):
    '''calculation of local sidereal time from Greenwich sidereal time (in degrees)'''
    return sid+lon

def ra2ha(ra,sid):
    '''calculation of hour angle from RA'''
    return sid-ra

def ha2ra(ha,sid):
    '''calculation of RA from hour angle'''
    return sid-ha

def eq2azm(ha,dec,lat,sid=None,ra=False):
    '''transformation of equatorial coordinates (Hour angle, DEC) to azimutal (Azm - from South!, Alt); 
    or from (RA, DEC) - give RA as 1st arg. instead of ha, set ra=True and give sidereal time (sid)'''
    
    #type of output (same as input - number, list, numpy.array)
    if sid is None: sid=0
    out_type='lst'
    if (isinstance(ha,int) or isinstance(ha,float)) and (isinstance(dec,int) or isinstance(dec,float)) and (isinstance(sid,int) or isinstance(sid,float)) and (isinstance(lat,int) or isinstance(lat,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(ha,np.ndarray) or isinstance(dec,np.ndarray) or isinstance(sid,np.ndarray) or isinstance(lat,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(ha,list): ha=np.array(ha)
    if isinstance(dec,list): dec=np.array(dec)
    if isinstance(sid,list): sid=np.array(sid)      
    if isinstance(lat,list): lat=np.array(lat)
        
    if ra: t=sid-ha
    else: t=ha   #HA given
    
    if out_type=='num': t=np.array([t])
    
    t=np.deg2rad(t)
    dec=np.deg2rad(dec)
    lat=np.deg2rad(lat)
    
    alt=np.arcsin(np.sin(dec)*np.sin(lat)+np.cos(dec)*np.cos(lat)*np.cos(t))
    sinA=np.cos(dec)*np.sin(t)/np.cos(alt)
    cosA=(-np.cos(lat)*np.sin(dec)+np.sin(lat)*np.cos(dec)*np.cos(t))/np.cos(alt)
    azm=np.arctan2(sinA,cosA)
    azm[np.where(azm<0)]+=2*np.pi
    
    azm=np.rad2deg(azm)
    alt=np.rad2deg(alt)

    if out_type=='num':
        alt=alt[0]
        azm=azm[0]
    elif out_type=='lst':
        alt=alt.tolist()
        azm=azm.tolist()
    return azm,alt


def azm2eq(azm,alt,lat,sid=None,ra=False):
    '''transformation of azimutal coordinates (Azm - from South!, Alt) to equatorial (Hour angle, DEC);
    or to (RA, DEC) - set ra=True and give sidereal time (sid)'''
    
    #type of output (same as input - number, list, numpy.array)
    if sid is None: sid=0
    out_type='lst'
    if (isinstance(azm,int) or isinstance(azm,float)) and (isinstance(alt,int) or isinstance(alt,float)) and (isinstance(sid,int) or isinstance(sid,float)) and (isinstance(lat,int) or isinstance(lat,float)): 
        #all input args are numbers        
        out_type='num'           
    
    if isinstance(azm,np.ndarray) or isinstance(alt,np.ndarray) or isinstance(sid,np.ndarray) or isinstance(lat,np.ndarray):
        #numpy.array
        out_type='np'  
    
    if isinstance(azm,list): azm=np.array(azm)
    if isinstance(alt,list): alt=np.array(alt)
    if isinstance(sid,list): sid=np.array(sid)      
    if isinstance(lat,list): lat=np.array(lat)
            
    if out_type=='num': azm=np.array([azm])
    
    azm=np.deg2rad(azm)
    alt=np.deg2rad(alt)
    lat=np.deg2rad(lat)
    
    dec=np.arcsin(np.sin(lat)*np.sin(alt)-np.cos(lat)*np.cos(alt)*np.cos(azm))
    sinH=np.cos(alt)*np.sin(azm)/np.cos(dec)
    cosH=(np.sin(alt)*np.cos(lat)+np.cos(alt)*np.sin(lat)*np.cos(azm))/np.cos(dec)
    
    ha=np.arctan2(sinH,cosH)
    ha[np.where(ha<0)]+=2*np.pi
    
    ha=np.rad2deg(ha)
    dec=np.rad2deg(dec)
    
    if ra: ha=sid-ha
    
    if out_type=='num':
        dec=dec[0]
        ha=ha[0]
    elif out_type=='lst':
        dec=dec.tolist()
        ha=ha.tolist()
    return ha,dec
    

def eq2ecl(ra,dec):
    '''transformation of equatorial coordinates (RA, DEC) to ecliptical (lamda, beta)'''
    
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
    
    ra=np.deg2rad(ra)
    dec=np.deg2rad(dec)
    
    beta=np.arcsin(np.sin(dec)*np.cos(eps)-np.cos(dec)*np.sin(eps)*np.sin(ra))
    sinL=(np.sin(ra)*np.cos(dec)*np.cos(eps)+np.sin(dec)*np.sin(eps))/np.cos(beta)
    cosL=np.cos(ra)*np.cos(dec)/np.cos(beta)
    
    lam=np.arctan2(sinL,cosL)
    lam[np.where(lam<0)]+=2*np.pi
    
    lam=np.rad2deg(lam)
    beta=np.rad2deg(beta)

    if out_type=='num':
        beta=beta[0]
        lam=lam[0]
    elif out_type=='lst':
        beta=beta.tolist()
        lam=lam.tolist()
    return lam,beta    


def ecl2eq(lam,beta):
    '''transformation of ecliptical coordinates (lamda, beta) to equatorial (RA, DEC)'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(lam,int) or isinstance(lam,float)) and (isinstance(beta,int) or isinstance(beta,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(lam,np.ndarray) or isinstance(beta,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(lam,list): lam=np.array(lam)
    if isinstance(beta,list): beta=np.array(beta)
    
    if out_type=='num': lam=np.array([lam])
    
    lam=np.deg2rad(lam)
    beta=np.deg2rad(beta)
    
    dec=np.arcsin(np.sin(beta)*np.cos(eps)+np.cos(beta)*np.sin(eps)*np.sin(lam))
    sinR=(np.sin(lam)*np.cos(beta)*np.cos(eps)-np.sin(beta)*np.sin(eps))/np.cos(dec)
    cosR=np.cos(lam)*np.cos(beta)/np.cos(dec)
    
    ra=np.arctan2(sinR,cosR)
    ra[np.where(ra<0)]+=2*np.pi
    
    ra=np.rad2deg(ra)
    dec=np.rad2deg(dec)

    if out_type=='num':
        dec=dec[0]
        ra=ra[0]
    elif out_type=='lst':
        dec=dec.tolist()
        ra=ra.tolist()
    return ra,dec        


def eq2gal(ra,dec):
    '''transformation of equatorial coordinates (RA, DEC) to galactic (l, b)'''
    
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
    
    ra=np.deg2rad(ra)-raG
    dec=np.deg2rad(dec)
    
    b=np.arcsin(np.sin(dec)*np.sin(decG)+np.cos(dec)*np.cos(decG)*np.cos(ra))
    sinL=np.cos(dec)*np.sin(ra)/np.cos(b)
    cosL=(np.sin(dec)*np.cos(decG)-np.cos(dec)*np.sin(decG)*np.cos(ra))/np.cos(b)
    
    l=np.arctan2(sinL,cosL)
    l=lNP-l
    l[np.where(l>=2*np.pi)]-=2*np.pi
    l[np.where(l<0)]+=2*np.pi
    
    l=np.rad2deg(l)
    b=np.rad2deg(b)

    if out_type=='num':
        b=b[0]
        l=l[0]
    elif out_type=='lst':
        b=b.tolist()
        l=l.tolist()
    return l,b  


def gal2eq(l,b):
    '''transformation of galactic coordinates (l, b) to equatorial (RA, DEC)'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(l,int) or isinstance(l,float)) and (isinstance(b,int) or isinstance(b,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(l,np.ndarray) or isinstance(b,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(l,list): l=np.array(l)
    if isinstance(b,list): b=np.array(b)
    
    if out_type=='num': b=np.array([b])
    
    l=lNP-np.deg2rad(l)
    b=np.deg2rad(b)
    
    dec=np.arcsin(np.sin(decG)*np.sin(b)+np.cos(decG)*np.cos(b)*np.cos(l))
    sinR=np.cos(b)*np.sin(l)/np.cos(dec)
    cosR=(np.cos(decG)*np.sin(b)-np.sin(decG)*np.cos(b)*np.cos(l))/np.cos(dec)
    
    ra=np.arctan2(sinR,cosR)
    ra+=raG
    ra[np.where(ra>=2*np.pi)]-=2*np.pi
    ra[np.where(ra<0)]+=2*np.pi
    
    ra=np.rad2deg(ra)
    dec=np.rad2deg(dec)

    if out_type=='num':
        ra=ra[0]
        dec=dec[0]
    elif out_type=='lst':
        ra=ra.tolist()
        dec=dec.tolist()
    return ra,dec 
    