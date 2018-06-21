'''Meeus: Astronomical Algorithms (2nd ed.), chapter 10''' 
'''based on https://eclipse.gsfc.nasa.gov/SEhelp/deltatpoly2004.html'''

def dT(jd):
    '''calculate dT = TD - UT in seconds for years 1986-2150'''
    t=(jd-2451545)/365.25
    
    if jd<2453371: return 63.86+0.3345*t-0.060374*t**2+0.0017275*t**3+0.000651814*t**4+0.00002373599*t**5  #years 1986-2005
    elif jd<2469807: return 62.92+0.32217*t+0.005589*t**2  #years 2005-2050
    else: return -20+32*((jd-2385800)/36525.)**22-0.5628*((2506331-jd)/365.25)
