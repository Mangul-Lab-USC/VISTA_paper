import pandas as pd
import allel
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from scipy import stats
import math

#Author: Seungmo Lee
df = pd.read_csv("mark.csv")
color_map = {'BREAKDANCER':'peru', 'clever':'gold', 'delly':'darkorange', 'delly':'mediumorchid', 
             'gasv':'firebrick','pindel':'darkorange', 'popdel':'navy',
             'smoove':'orangered','GENOMESTRIP':'pink','manta':'aqua', 'VISTA':'black','parl':'magenta','surv':'purple','jasmine':'lightblue',
             'true deletions':'#39FF14','GROM':'forestgreen','octopus':'coral'}

fig1g=sns.set_style("ticks")
fig1g=sns.set_context("poster",rc={"font.size":30,"axes.titlesize":30,"axes.labelsize":30})

fig_order=["smoove","surv",'manta','VISTA','parl','true deletions','delly','jasmine',"octopus"]
labels=["Smoove","SURVIVOR*",'Manta','VISTA*','Parliament2*','True Deletions','DELLY','Jasmine*',"Octopus"]

df_number=df.groupby('tool', as_index=False).count()
df_number=df_number.rename(columns={'length': 'n'})

print(df_number)
df_number['n'] = df_number['n'].apply(lambda x: math.log10(x))
print("Log Scale:")
print(df_number)
fig1b=sns.set_style('whitegrid')
fig1b=sns.set_context('talk')


pal = []
for tool in fig_order:
    pal.append(color_map[tool])
    
fig1b = sns.catplot(x='n', y='tool',data=df_number,kind='bar',aspect=1.5, palette=pal, order=fig_order)
fig1b.set(xlabel='Number of deletions (Log n)', ylabel='Tool')



x_ticks = [0,2,4,6,8]  
i=0
for val in x_ticks:
    if val != 0:
        x_ticks[i]= f'$10^{val}$'
    i+=1
    
fig1b.set_xticklabels(x_ticks)
sns.set(font_scale = 2)
fig1b.set_yticklabels(labels)
fig1b=sns.despine()
plt.title("Number of deletions detected by callers",fontsize=17)
plt.savefig("num_calls_del_mark.png", bbox_inches='tight',dpi=300)