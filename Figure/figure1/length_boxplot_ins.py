import pandas as pd
import allel
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from scipy import stats

#Author: Seungmo Lee
df = pd.read_csv("lengths_ins.csv")

color_map = {'BREAKDANCER':'peru', 'clever':'gold','delly':'mediumorchid', 
             'gasv':'firebrick','pindel':'darkorange', 'popdel':'navy',
             'smoove':'orangered','GENOMESTRIP':'pink','manta':'aqua', 'VISTA':'black', 'parl':'magenta', 'transIndel':'gray',
             'gold':'#39FF14'}
fig1g=sns.set_style("ticks")
fig1g=sns.set_context("poster",rc={"font.size":50,"axes.titlesize":30,"axes.labelsize":30})

labels=['transIndel','VISTA*','True Insertions','Parliament2*','DELLY','Manta']
fig_order=['transIndel','VISTA','gold','parl','delly','manta']

df["Tool"] = df["tool"].map(dict(zip(fig_order, labels)))
test=df.groupby("Tool")["length"].median()
ranks = df.groupby("Tool")["length"].median().fillna(0).sort_values()[0::].index
pal = []
for tool in fig_order:
    pal.append(color_map[tool])

fig1g = sns.catplot(x="length", y="Tool", kind='boxen', data=df.sort_values("length"), height=20, aspect=.4, palette=pal, order=labels)

medians = df.groupby("Tool")["length"].median().fillna(0)
for i, median in enumerate(medians[ranks]):
    fig1g.ax.text(100000, i, f'{median:.1f}', color='black', va='center', fontsize=18,fontweight='normal')

fig1g.set(xscale="log")
fig1g.set(ylabel='SV-caller')
fig1g.set(xlabel='Insertion length')
fig1g=sns.despine()
sns.set(font_scale=2)
plt.savefig("boxplot_ins.png", bbox_inches='tight')
