'''Meeus: Astronomical Algorithms (2nd ed.), chapter 14'''

import numpy as np
from constants import eps

def paralactic(ha,dec,lat):
    '''calculation of paralactic angle'''
    out_type='lst'
    if (isinstance(ha,int) or isinstance(ha,float)) and (isinstance(dec,int) or isinstance(dec,float)) and (isinstance(lat,int) or isinstance(lat,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(ha,np.ndarray) or isinstance(dec,np.ndarray) or isinstance(lat,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(ha,list): ha=np.array(ha)
    if isinstance(dec,list): dec=np.array(dec)   
    if isinstance(lat,list): lat=np.array(lat)        
    
    if out_type=='num': ha=np.array([ha])
    
    ha=np.deg2rad(ha)
    dec=np.deg2rad(dec)
    lat=np.deg2rad(lat)
    
    q=np.arctan(np.sin(ha)/(np.tan(lat)*np.cos(dec)-np.sin(dec)*np.cos(ha)))
    q=np.rad2deg(q)

    if out_type=='num':
        q=q[0]
    elif out_type=='lst':
        q=q.tolist()
    return q

def paralacticRS(dec,lat):
    '''calculation of paralactic angle for rising or setting'''
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
    
    q=np.arccos(np.sin(lat)/np.cos(dec))
    q=np.rad2deg(q)

    if out_type=='num':
        q=q[0]
    elif out_type=='lst':
        q=q.tolist()
    return q

def ecl_hor(sid,lat):
    '''angle between ecliptic and horizon'''
    out_type='lst'
    if (isinstance(sid,int) or isinstance(sid,float)) and (isinstance(lat,int) or isinstance(lat,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(sid,np.ndarray) or isinstance(lat,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(sid,list): sid=np.array(sid)   
    if isinstance(lat,list): lat=np.array(lat)        
    
    if out_type=='num': sid=np.array([sid])
    
    sid=np.deg2rad(sid)
    lat=np.deg2rad(lat)
    
    I=np.arccos(np.cos(eps)*np.sin(lat)-np.sin(eps)*np.cos(lat)*np.sin(sid))
    I=np.rad2deg(I)

    if out_type=='num':
        I=I[0]
    elif out_type=='lst':
        I=I.tolist()
    return I

def angle_hor(dec,lat):
    '''angle between diurnal (daily) path of object and horizont'''
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
    
    B=np.tan(dec)*np.tan(lat)
    C=np.sqrt(1-B**2)
    J=np.arctan(C*np.cos(dec)/np.tan(lat))
    
    J=np.rad2deg(J)

    if out_type=='num':
        J=J[0]
    elif out_type=='lst':
        J=J.tolist()
    return J

