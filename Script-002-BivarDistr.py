#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sb
from matplotlib import pyplot as plt
import pandas as pd
import os
os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")
dfM.head(5)
sb.jointplot(x='igneous_volc',y='sedim_thick',data=dfM)
plt.show()


# In[ ]:




import seaborn as sb
