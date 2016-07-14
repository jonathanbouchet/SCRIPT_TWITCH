"""
Simple demo with multiple subplots.
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

data = mlab.csv2rec('./Overwatch2016-07-14.csv',delimiter='\t')
view = data['viewers']
chan = data['channels']
time = data['datetime']

plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.xlabel('time')
plt.ylabel('channels')
plt.plot(time,chan,'ko')
title = 'Channels vs time for day ' + str(data['date'][1])
plt.title(title)

plt.subplot(2, 1, 2)
plt.xlabel('time')
plt.ylabel('viewers')
plt.plot(time,view,'ko')
title = 'Viewers vs time for day ' + str(data['date'][1])
plt.title(title)

plt.tight_layout()
plt.show()
