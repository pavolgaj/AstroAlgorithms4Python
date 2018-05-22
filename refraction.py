'''Meeus: Astronomical Algorithms (2nd ed.), chapter 16'''  

import numpy as np

def apparent(alt,correction=False):
    '''refraction for apparent altitude (with optional correction)'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(alt,int) or isinstance(alt,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(alt,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(alt,list): alt=np.array(alt)  
    
    if out_type=='num': alt=np.array([alt])
    
    R=1/np.tan(np.deg2rad(alt+7.31/(alt+4.4)))/60.
    
    if correction: R=alt-R
    
    if out_type=='num':
        R=R[0]
    elif out_type=='lst':
        R=R.tolist()
    return R


def real(alt,correction=False):
    '''refraction for real altitude (with optional correction)'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if (isinstance(alt,int) or isinstance(alt,float)): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(alt,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(alt,list): alt=np.array(alt)  
    
    if out_type=='num': alt=np.array([alt])
    
    R=1.02/np.tan(np.deg2rad(alt+10.3/(alt+5.11)))/60.
    
    if correction: R+=alt
    
    if out_type=='num':
        R=R[0]
    elif out_type=='lst':
        R=R.tolist()
    return R
    