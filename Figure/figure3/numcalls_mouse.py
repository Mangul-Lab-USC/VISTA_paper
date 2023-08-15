import pandas as pd
import allel
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from scipy import stats
import math

#Author: Seungmo Lee
df = pd.read_csv("numcalls_mouse.csv")

color_map = {'BioGraph*':'yellowgreen', 'breakdancer':'peru', 'clever':'gold', 'delly':'darkorange', 'delly':'mediumorchid', 
             'gasv':'firebrick', 'gridss':'cornflowerblue', 'indelminer':'forestgreen', 
             'mistrvar':'salmon', 'pindel':'darkorange', 'popdel':'navy', 'rdxplorer':'darkgray', 
             'smoove':'orangered',  'true deletions':'#39FF14',  'crest':'red', 'genomestrip':'pink','manta_diploidSV':'aqua','Tardis':'lime','VISTA': 'black','surv': 'purple','parl':'magenta','jasmine': 'lightblue'}

fig1g=sns.set_style("ticks")
fig1g=sns.set_context("poster",rc={"font.size":30,"axes.titlesize":30,"axes.labelsize":30})

df_number=df.groupby('tool', as_index=False).count()
df_number=df_number.rename(columns={'length': 'n'})

df_number.loc[df_number['tool'] != 'parl', 'n'] = df_number.loc[df_number['tool'] != 'parl', 'n'] / 7
df_number.loc[df_number['tool'] == 'parl', 'n'] = df_number.loc[df_number['tool'] == 'parl', 'n'] / 5

print(df_number)
df_number['n'] = df_number['n'].apply(lambda x: math.log10(x))
print("Log Scale:")
fig1b=sns.set_style('whitegrid')
fig1b=sns.set_context('talk')

# fig_order=["true deletions", "BioGraph*","breakdancer", "clever", "delly", "gasv", "gridss", "indelminer",  "mistrvar", "pindel","popdel","rdxplorer", "smoove", "sniffles"]
fig_order = ['indelminer','genomestrip','popdel','mistrvar','crest','Tardis','surv','smoove','VISTA','BioGraph*','breakdancer','true deletions','manta_diploidSV','delly','gridss','parl','jasmine','clever','rdxplorer','pindel','gasv']

pal = []
for tool in fig_order:
    pal.append(color_map[tool])
    
fig1b = sns.catplot(x='n', y='tool',data=df_number,kind='bar',aspect=1.5, palette=pal, order=fig_order)
fig1b.set(xlabel='Number of average deletions (log n)', ylabel='Tool')



x_ticks = [0,2,4]  
i=0
for val in x_ticks:
    if val != 0:
        x_ticks[i]= f'$10^{val}$'
    i+=1

fig1b.set_xticklabels(x_ticks)

# labels = ['Smoove','GenomeSTRiP','BreakDancer','PopDel','GROM','Survivor','Manta','DELLY','VISTA','Jasmine','True Deletions',
#           'GASV','Octopus','Pindel','CLEVER']
labels    = ["indelMINER","GenomeSTRiP","PopDel","MiStrVar","CREST","Tardis","SURVIVOR*","LUMPY","VISTA*","BioGraph*","BreakDancer","True Deletions","Manta","DELLY","GRIDSS","Parliament2*","Jasmine*","CLEVER","RDXplorer","Pindel","GASV"]

sns.set(font_scale = 2)
fig1b.set_yticklabels(labels)
fig1b=sns.despine()
plt.subplots_adjust(left=0.3, right=0.9, top=1.0, bottom=0.1)
plt.title("Number of deletions detected by callers",fontsize=17)
plt.savefig("num_calls_del_mouse.png", bbox_inches='tight')