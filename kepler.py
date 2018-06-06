'''Meeus: Astronomical Algorithms (2nd ed.), chapter 30'''

import numpy as np

def method1(e,M,eps=1e-8):
    '''1st method for solving Kepler's equation'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if isinstance(M,int) or isinstance(M,float): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(M,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(M,list): M=np.array(M)
    if out_type=='num': M=np.array([M])
    
    M=np.deg2rad(M)
    E=M
    E0=E+1e3
    #i=0
    while max(abs(E-E0))>eps:
        E0=np.array(E)
        E=M+e*np.sin(E)  
        #i+=1
    #print i
    
    E=np.rad2deg(E)
    if out_type=='num': E=E[0]
    elif out_type=='lst': E=E.tolist()
    return E


def method2(e,M,eps=1e-8):
    '''2nd method for solving Kepler's equation'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if isinstance(M,int) or isinstance(M,float): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(M,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(M,list): M=np.array(M)
    if out_type=='num': M=np.array([M])
    
    M=np.deg2rad(M)
    E=M
    E0=E+1e3
    #i=0
    while max(abs(E-E0))>eps:
        E0=np.array(E)
        E=E+(M+e*np.sin(E)-E)/(1-e*np.cos(E))  
        #i+=1
    #print i
    
    E=np.rad2deg(E)
    if out_type=='num': E=E[0]
    elif out_type=='lst': E=E.tolist()
    return E

def method3(e,M,eps=1e-8):
    '''3rd method for solving Kepler's equation'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if isinstance(M,int) or isinstance(M,float): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(M,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(M,list): M=np.array(M)
    if out_type=='num': M=np.array([M])
    
    M=np.deg2rad(M)
    
    F=np.sign(M)
    M=np.abs(M)/(2*np.pi)
    M=(M-M//1)*2*np.pi*F
    M[np.where(M<0)]+=2*np.pi
    F=np.ones(M.shape)
    F[np.where(M>np.pi)]=-1
    M[np.where(M>np.pi)]=2*np.pi-M[np.where(M>np.pi)]
    
    E=np.pi/2.*np.ones(M.shape)
    D=np.pi/4.
    E0=np.ones(M.shape)
    #i=0
    while max(abs(E-E0))>eps:
        E0=np.array(E)
        E+=D*np.sign(M-(E-e*np.sin(E)))
        D/=2.
        #i+=1
    #print i
    
    E*=F
    E[np.where(E<0)]+=2*np.pi
    E=np.rad2deg(E)
    if out_type=='num': E=E[0]
    elif out_type=='lst': E=E.tolist()
    return E


def method4(e,M,eps=1e-8):
    '''4th method (approximation) for solving Kepler's equation'''
    
    #type of output (same as input - number, list, numpy.array)
    out_type='lst'
    if isinstance(M,int) or isinstance(M,float): 
        #all input args are numbers        
        out_type='num' 
        
    if isinstance(M,np.ndarray):
        #numpy.array
        out_type='np' 
        
    if isinstance(M,list): M=np.array(M)
    if out_type=='num': M=np.array([M])
    
    M=np.deg2rad(M)
    
    E=np.arctan2(np.sin(M),np.cos(M)-e)
    
    E[np.where(E<0)]+=2*np.pi
    E=np.rad2deg(E)
    if out_type=='num': E=E[0]
    elif out_type=='lst': E=E.tolist()
    return E