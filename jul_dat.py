'''Meeus: Astronomical Algorithms (2nd ed.), chapter 7'''

def date2jd(year,mon,day,h=0,m=0,s=0):
    '''convert date and time to julian date'''
    if mon<=2:
        year-=1
        mon+=12
    a=int(year/100)
    b=2-a+int(a/4)
    jd=int(365.25*(year+4716))+int(30.6001*(mon+1))+day+h/24.+m/1440.+s/86400.+b-1524.5
    return jd

def jd2date(jd):
    '''convert julian date to date and time'''
    jd+=0.5
    z=int(jd)
    f=jd%1
    if z<2299161: a=z
    else:
        alp=int((z-1867216.25)/36524.25)
        a=z+1+alp-int(alp/4)
    b=a+1524
    c=int((b-122.1)/365.25)
    d=int(365.25*c)
    e=int((b-d)/30.6001)
    
    h=int(f*24)
    m=int((f-h/24.)*1440)
    s=round((f-h/24.-m/1440.)*86400.,2)
    day=b-d-int(30.6001*e)
    if  e<14: mon=e-1
    else: mon=e-13
    if mon>2: year=c-4716
    else: year=c-4715
    
    return year,mon,day,h,m,s

def timeint(year1,mon1,day1,year2,mon2,day2):
    '''time interval between two dates in days'''
    jd1=date2jd(year1,mon1,day1)
    jd2=date2jd(year2,mon2,day2)
    return int(jd2-jd1)

def weekday(year,mon,day):
    '''day of week for given date'''
    jd=date2jd(year,mon,day)+1.5
    if jd%7==0: return 'Sunday'
    if jd%7==1: return 'Monday'
    if jd%7==2: return 'Tuesday'
    if jd%7==3: return 'Wednesday'
    if jd%7==4: return 'Thursday'
    if jd%7==5: return 'Friday'
    if jd%7==6: return 'Saturday'


