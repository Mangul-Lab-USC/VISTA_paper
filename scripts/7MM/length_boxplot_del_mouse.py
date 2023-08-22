import pandas as pd
import allel
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
from scipy import stats

#Author: Seungmo Lee
# df = pd.read_csv("lengths.csv")
df = pd.read_csv("numcalls_mouse.csv")                          

fig1g=sns.set_style("ticks")
fig1g=sns.set_context("poster",rc={"font.size":30,"axes.titlesize":30,"axes.labelsize":30})

color_map = {'BioGraph*':'yellowgreen', 'breakdancer':'peru', 'clever':'gold', 'delly':'darkorange', 'delly':'mediumorchid', 
             'gasv':'firebrick', 'gridss':'cornflowerblue', 'indelminer':'forestgreen', 
             'mistrvar':'salmon', 'pindel':'darkorange', 'popdel':'navy', 'rdxplorer':'darkgray', 
             'smoove':'orangered',  'true deletions':'#39FF14',  'crest':'red', 'genomestrip':'pink','manta_diploidSV':'aqua','Tardis':'lime','VISTA': 'black','surv': 'purple','parl':'magenta','jasmine': 'lightblue'}

# fig_order = ["indelminer", "pindel","mistrvar", "gridss","jasmine","delly","clever","parl","BioGraph*","manta_diploidSV","VISTA","breakdancer","smoove","Tardis","surv","crest","rdxplorer","popdel","gasv","genomestrip","true deletions"]
fig_order = ['pindel','jasmine',"clever","mistrvar","parl","indelminer","BioGraph*","manta_diploidSV","VISTA","gridss","breakdancer",
             "true deletions","smoove","delly","Tardis","surv","crest","rdxplorer","popdel","gasv","genomestrip"]

labels = ['Pindel', 'Jasmine*', 'CLEVER', 'MiStrVar', 'Parliament2*',
       'indelMINER', 'BioGraph*', 'Manta', 'VISTA*', 'GRIDSS', 'BreakDancer',
       'True Deletions', 'LUMPY', 'DELLY', 'Tardis', 'SURVIVOR*', 'CREST',
       'RDXplorer', 'PopDel', 'GASV', 'GenomeSTRiP']

df["Tool"] = df["tool"].map(dict(zip(fig_order, labels)))
test=df.groupby("Tool")["length"].median()
ranks = df.groupby("Tool")["length"].median().fillna(0).sort_values()[0::].index
print(test)
print(ranks)
pal = []
for tool in fig_order:
    pal.append(color_map[tool])

fig1g = sns.catplot(x="length", y="Tool", kind='boxen', data=df.sort_values("length"), height=20, aspect=.4, palette=pal, order=labels)

medians = df.groupby("Tool")["length"].median().fillna(0)
for i, median in enumerate(medians[ranks]):
    fig1g.ax.text(10000000000, i, f'{median:.0f}', color='black', va='center', fontsize=12,fontweight='normal')

x_bracket = 1.2  # x-coordinate for the bracket
y_start = 0.3  # Starting y-coordinate for the bracket
y_end = len(ranks) - 0.7  # Ending y-coordinate for the bracket

fig1g.ax.annotate('', xy=(x_bracket, y_start), xytext=(x_bracket, y_end),
                   arrowprops=dict(arrowstyle='-', lw=3),
                   annotation_clip=False)
fig1g.set(xscale="log")
fig1g.set(ylabel='SV-caller')
fig1g.set(xlabel='Deletion length')
fig1g=sns.despine()
sns.set(font_scale=2)
plt.savefig("boxplot_del_mouse.png", bbox_inches='tight')
