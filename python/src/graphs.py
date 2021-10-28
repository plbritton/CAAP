import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

data = pd.read_csv('') #filename goes here
data.head()

data = pd.DataFrame(data)
data.info()
print(data)

sns.set()

barprofit = sns.countplot(x='time',dat=data) #put parameter label within ''
plt.show()

#to make bar graph
plt.figure(figsize = (20, 20))
sns.set()
bar = sns.countplot(y='net profit',dat=data) #put parameter label within ''
plt.show()

#to make a bar graph with another parameter
plt.figure(figsize = (10, 15))
sns.set()
bar = sns.countplot(y='',dat=data) #put parameter label within ''
plt.show()

#to make a Facet Grid
fg = sns.FacetGrid(dat=data,col='type')
fg.map(plt.hist,'') #put parameter label within ''

#to make a lineplot
line = sns.lineplot(dat=data)
sns.lineplot(dat= data, x='', y='')



# https://matplotlib.org/stable/tutorials/introductory/pyplot.html
#linear and log stuff if there's both data on a lower end and higher end

np.random.seed(167249)

#put data info here

plt.figure()

# linear
plt.subplot(200)
plt.plot(i, j)
plt.yscale('linear') #if log is desired then change 'linear' to 'log'
plt.title('linear graph')
plt.grid(True)




