# -*- coding: utf-8 -*-
"""LUday01assign1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jd_X35QUNUZLTm-GBQo3MsvMeMnN8Egz
"""

# Commented out IPython magic to ensure Python compatibility.
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
# %matplotlib inline
#print(mpl.__version__)
x=np.arange(0,10)
y=x*x
plt.plot(x,y,'ro--')
plt.xlabel('squares of numbers')
plt.ylabel('numbers')
plt.title('square curve')
plt.show()