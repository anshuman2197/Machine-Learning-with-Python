# -*- coding: utf-8 -*-
"""Goeduhub 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12kRJS8CHRcF4IcpdYzuKTBUk2i7p3UUd
"""

pip install matplotlib

from matplotlib import pyplot as plt
plt.plot([1,2,3],[4,5,1])
plt.title('Information')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()

x=[15,18,20]
y=[22,26,16]
x2=[6,9,11]
y2=[6,15,7]
plt.plot(x,y,'red',label='line',linewidth=5)
plt.plot(x2,y2,'green',label='Line Two',linewidth=8)
plt.legend()
plt.title('Graph')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.grid()
plt.show()

"""## Bar Graph"""

from matplotlib import pyplot as plt
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,20,60],
        label="BMW",color='r',width=.1)
plt.bar([.75,1.75,2.25,3.75,4.75],[80,20,20,50,60],
        label="Audi",color='b',width=.5)
plt.legend()
plt.xlabel('Days')
plt.ylabel('Distance')
plt.title('Information')
plt.show()

"""## Histogram"""

age=[18,19,29,18,18,20,25,24,23,22,22,23,43,23,56,44,18,18,18,191,81,37]
bins=[0,5,10,15,20,25,30,35]
plt.hist(age,bins,histtype='step')
plt.show()

"""## Scatter plot"""

x=[2,2.5,3,3.5,4,4.5,5]
y=[8,8.5,9,9.5,10,10.1,10.2]
plt.scatter(x,y,color='r',label='line 1')
plt.xlabel('income')
plt.ylabel('saving')
plt.title("Scatter plot")
plt.legend()
plt.plot()
plt.show()

import numpy as np
plt.plot([1,2,3,4,],[1,4,9,16],'ro-',label='Line1')
plt.plot([1,2,3,4,],[1,2,3,4],label='Line2')
plt.plot([1,2,3,4,],[6,6,6,6],'g*',label='Line3')
plt.legend()
plt.show()

t=np.arange(0,5,.2)
plt.plot(t,t,'r--',t,t**2,'bo')

"""# Matplot 3-D"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

iris=pd.read_csv('/content/Iris.csv')
iris

for species,irissubset in iris.groupby('Species'):
  plt.scatter(irissubset['PetalLengthCm'],irissubset['PetalWidthCm'],label=species)
plt.show()

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

for species,irissubset in iris.groupby('Species'):
  plt.scatter(irissubset['PetalLengthCm'],irissubset['PetalWidthCm'],irissubset['SepalLengthCm'],label=species)
  ax.set_xlabel('PetalLength')
  ax.set_ylabel('PetalWidth')
  ax.set_zlabel('SepalWidth')
plt.legend() 
plt.show()

"""## Pie Chart"""

slices=[12,2,2,30]
activities=['sleeping','eating','working','playing']
cols=['c','m','r','b']
plt.pie(slices,labels=activities,colors=cols,startangle=90)
plt.title('Pie Pie')
plt.show()

import numpy as np

import matplotlib.pyplot as plt

def f(t):
  return np.exp(-t)*np.cos(2*np.pi*t)
t1=np.arange(0.0,5.0,0.1)
t2=np.arange(0.0,5.0,0.02)

plt.subplot(211)

plt.plot(t1,f(t1),'bo',t2,f(t2))
plt.subplot(212)
plt.plot(t2,np.cos(2*np.pi*t2))
plt.show()

