import numpy as np 
import matplotlib
matplotlib.use('Pdf')
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_pdf import PdfPages 
import matplotlib.patches as patches
import matplotlib.font_manager as fm

#"id","name","application_id","priority","sun_angle","minimum_latitude","maximum_latitude","minimum_longitude","maximum_longitude","pixel_resolution","description","details","created_at","updated_at"

pp=PdfPages('regions.pdf')
file="./MoonMasterImages.csv"

import pandas

data=pandas.read_csv(file)
#print data['details'][0][11:17]
#print data['minimum_latitude'][0]

max_y=data['minimum_latitude'].min()
min_x= data['minimum_longitude'].min()

max_x=data['maximum_latitude'].max()
min_y=data['maximum_longitude'].max()

min_lat=data['minimum_latitude']
max_lat=data['maximum_latitude']
min_lon=data['minimum_longitude']
max_lon=data['maximum_longitude']
details=data['details']


#matplotlib.patches.Rectangle(xy, width, height, angle=0.0, **kwargs)

color_vec=['k','r','b','g','y','m','c']

NUM_COLORS = 27
cm = plt.get_cmap('gist_rainbow')

colors = plt.cm.Spectral(np.linspace(0,1,NUM_COLORS))

prop = fm.FontProperties(size=7)
fig= plt.figure()
ax=fig.add_subplot(111)
ax.set_color_cycle( [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]  )
for i, (a,b,c,d, e) in enumerate(zip(min_lon, max_lat, max_lon, min_lat, details)):
    print a,b,c,d
    #print (a,b), a+c, b+d
    sun_angle=float(e[11:17])
    ax.add_patch( patches.Rectangle( (a,b), a+c, b+d, fill=False ))
    #ax.legend(loc='upper_right', fancybox=True, ncol=2, numpoints=1, prop = prop)
plt.xlim([-500,15])
plt.ylim([-500,100])
pp.savefig()


fig= plt.figure()
ax=fig.add_subplot(111)
ax.set_color_cycle( [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]  )
for i, (a,b,c,d, e) in enumerate(zip(min_lon, max_lat, max_lon, min_lat, details)):
    if a < 0: continue
    print (a,b), a+c, b+d
    sun_angle=float(e[11:17])
    ax.add_patch( patches.Rectangle( (a,b), a+c, b+d, fill=False, 
                                          label='%g'%sun_angle, edgecolor= color_vec[i%len(color_vec)] ))
    ax.legend(loc='upper right', fancybox=True, ncol=2, numpoints=1, prop = prop)
plt.xlim([0,15])
plt.ylim([0,100])
pp.savefig()


fig= plt.figure()
ax=fig.add_subplot(111)
ax.set_color_cycle( [cm(1.*i/NUM_COLORS) for i in range(NUM_COLORS)]  )
for i, (a,b,c,d, e) in enumerate(zip(min_lon, max_lat, max_lon, min_lat, details)):
    if a > 0: continue
    print (a,b), a+c, b+d
    sun_angle=float(e[11:17])
    ax.add_patch( patches.Rectangle( (a,b), a+c, b+d, fill=False, 
                                          label='%g'%sun_angle, edgecolor= color_vec[i%len(color_vec)] ))
    ax.legend(loc='upper right', fancybox=True, ncol=2, numpoints=1, prop = prop)
plt.xlim([-180,-240])
plt.ylim([-57,-57.2])
pp.savefig()

pp.close()
