'''Meeus: Astronomical Algorithms (2nd ed.), chapter 12'''    

def sid_time(jd,deg=True):
    '''sidereal time on Greenwich in degrees or hours'''
    T=(jd-2451545.0)/36525
    sid=280.46061837+360.98564736629*(jd-2451545.0)+0.000387933*T**2-T**3/38710000
    sid=sid%360
    if deg: return sid
    else: return sid/15.
