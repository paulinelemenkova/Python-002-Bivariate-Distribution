#!/usr/bin/env python
# coding: utf-8
import os
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

sb.set_style('white')
sb.set_context('paper')

os.chdir('/Users/pauline/Documents/Python')
dfM = pd.read_csv("Tab-Morph.csv")

sb.jointplot(x='igneous_volc', y='sedim_thick', data=dfM)

plt.tight_layout()
plt.savefig('plot_BivarDistr.png', dpi=300)
plt.show()
