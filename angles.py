#simple routines with angles, not implamented in Meeus's Astronomical Algorithms

def dms(deg):
    '''convert angle in degrees to degrees, minutes and seconds'''
    m=int((deg%1)*60)
    s=round((deg%1-m/60.)*3600,3)
    return int(deg),m,s

def degree(d,m,s):
    '''convert angle in degrees, minutes and seconds to degrees'''
    return d+m/60.+s/3600.

def deg2hour(deg):
    '''convert angle from degrees to hours'''
    return deg/15.

def hour2deg(hour):
    '''convert angle from hours to degrees'''
    return hour*15.
