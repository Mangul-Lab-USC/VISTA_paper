import pandas as pd
import os
import sys
import allel
import numpy as np
from os import path

# # Read the input CSV file

csv_name = sys.argv[1]
df_merge = pd.read_csv(csv_name)

# Define the lists
samples = ['AKR_J', 'A_J', 'BALB_cJ', 'C3H_HeJ', 'CBA_J', 'DBA_2J', 'LP_J']
tools = ['breakdancer', 'delly', 'gridss', 'popdel', 'smoove', 'genomestrip', 'manta_diploidSV','VISTA']

df_merge['nFN']=df_merge['n_true']-df_merge['nTP']
df_merge['sensitivity']=df_merge['nTP']/df_merge['n_true']
df_merge['precision']=df_merge['nTP']/(df_merge['nTP']+df_merge['nFP'])
df_merge['specificity']=df_merge['nTN']/(df_merge['nTN']+df_merge['nFP'])
df_merge['f-score']=2*(df_merge['sensitivity']*df_merge['precision'])/(df_merge['sensitivity']+df_merge['precision']+0.00000001)
df_merge = df_merge.replace(np.nan, 0)
df_merge.tail()

df_sum=df_merge.groupby(['tool','threshold','cov','n'],as_index=False)[['nTP','nFP','nFN','nTN']].sum()
df_sum.head()
df_sum.groupby(['tool'],as_index=False).count()

# Already threshold 100 for all of them!

df_merge_mean=df_merge.groupby(['tool','threshold','cov'],as_index=False)[['sensitivity','precision','specificity','f-score']].mean()

print(df_merge_mean)
fig_order = ["indelminer","mistrvar","rdxplorer","popdel","pindel","BioGraph*","breakdancer","smoove","delly","gridss","clever","genomestrip","manta_diploidSV",'surv','jasmine','VISTA']
labels    = ["indelMINER","MiStrVar","RDXplorer","PopDel","Pindel","BioGraph*","BreakDancer","LUMPY","DELLY","GRIDSS","CLEVER","GenomeSTRiP","Manta",'SURVIVOR*','Jasmine*','VISTA*']
df_merge_mean["Tool"] = df_merge_mean["tool"].map(dict(zip(fig_order, labels)))

print(df_merge_mean['cov'].unique())

result = df_merge_mean.pivot(index='Tool', columns='cov', values='f-score')
result = result[[0.5, 1, 2, 4, 8, 16, 32]]
 
import matplotlib.pyplot as plt
import seaborn as sns

fig3a=sns.set_style("white")
fig3a=sns.set_context("talk")
fig3a=sns.heatmap(result, annot=True, cmap='coolwarm',center=0,linewidths=.5,annot_kws={'size':15},fmt=".2f",vmin=0, vmax=1)
fig3a.set(xlabel='Coverage', ylabel='')
plt.title('F-Score', weight='bold')
bottom, top = fig3a.get_ylim()
# print(bottom,top)
fig3a.set_ylim(bottom + 0.5, top - 0.5)
# fig3a.set_ylim(0, 1)
fig3a=sns.despine()
#plt.show(fig3a)
sns.set(font_scale=2)
plt.savefig("coverage_mouse_fscore"+sys.argv[1]+".png",bbox_inches="tight")
