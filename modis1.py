import os
import glob
from pymodis import downmodis,parsemodis
dest = '/tmp'
tiles ='h18v04,h19v04'
day = '2018-04-18'
delta = 1
modisdown =downmodis.downModis(user='khalilmk',password='+wppc6b_jX@,ZMw',destinationFolder=dest,tiles=tiles,today=day,delta=delta)
modisdown.connect()
modisdown.downloadsAllDay()
files = glob.glob(os.path.join(dest,'MOD11A1.A2014*.hdf'))
print(files)
