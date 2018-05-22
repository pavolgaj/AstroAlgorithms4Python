'''Meeus: Astronomical Algorithms (2nd ed.), chapter 15'''  

import numpy as np

def rising(dec,lat):
    '''local hour angle for rising (alt=0 deg) - without refraction'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(dec,int) or isinstance(dec,float)) and (isinstance(lat,int) or isinstance(lat,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(dec,np.ndarray) or isinstance(lat,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(dec,list): dec=np.array(dec)   
    if isinstance(lat,list): lat=np.array(lat)
        
    
    if out_type=='num': dec=np.array([dec])
    
    dec=np.deg2rad(dec)
    lat=np.deg2rad(lat)
    
    ha=np.arccos(-np.tan(lat)*np.tan(dec))
    
    ha=np.rad2deg(ha)

    if out_type=='num':
        ha=ha[0]
    elif out_type=='lst':
        ha=ha.tolist()
    return ha

def times(dec,ra,lat,lon,sid0):
    '''calculate time of rising, transit and setting; sid0 - sidereal time at Oh UT at Greenwich'''
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(dec,int) or isinstance(dec,float)) and (isinstance(ra,int) or isinstance(ra,float)) and (isinstance(lat,int) or isinstance(lat,float)) and (isinstance(lon,int) or isinstance(lon,float)) and (isinstance(sid0,int) or isinstance(sid0,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(dec,np.ndarray) or isinstance(ra,np.ndarray) or isinstance(lat,np.ndarray) or isinstance(lon,np.ndarray) or isinstance(sid0,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(dec,list): dec=np.array(dec) 
    if isinstance(ra,list): ra=np.array(ra)
    if isinstance(lat,list): lat=np.array(lat)
    if isinstance(lon,list): lon=np.array(lon)
    if isinstance(sid0,list): sid0=np.array(sid0)
        
    
    if out_type=='num': sid0=np.array([sid0])
    
    dec=np.deg2rad(dec)
    lat=np.deg2rad(lat)
    
    ha=np.arccos(-np.tan(lat)*np.tan(dec))
    
    ha=np.rad2deg(ha)
    
    t=(ra-lon-sid0)/360.  #transit
    r=t-ha/360.           #rise
    s=t+ha/360.           #set
    
    r*=24
    t*=24
    s*=24

    r=r%24
    t=t%24
    s=s%24

    if out_type=='num':
        r=r[0]
        t=t[0]
        s=s[0]
    elif out_type=='lst':
        r=r.tolist()
        t=t.tolist()
        s=s.tolist()
    return r,t,s


