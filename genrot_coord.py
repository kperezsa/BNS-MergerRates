from numpy import *
from astropy.time import Time
import ephem

dir='/Users/hsinyuc/research/'

time = ['1899-12-31 12:00:00']
t_ephem_start = Time(time, format='iso', scale='utc')

start_time='2017/05/01 00:00:00'
end_time='2017/05/31 23:45:00'
time_interval=0.25#time interval in hour.

event_time=arange(ephem.Date(start_time),ephem.Date(end_time)+1e-10,ephem.hour*time_interval)

ra_rot=zeros(size(event_time))
for i in range(0,size(event_time)):
    ra_rot[i]=rot_overtime(event_time[i])

table=column_stack((event_time+t_ephem_start.mjd,ra_rot))
savetxt(dir+'/obsbias/data/2017may_rot_fine.txt',table)