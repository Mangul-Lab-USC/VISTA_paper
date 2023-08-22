import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df_merge = pd.read_csv('df_merged.csv')

color_map = {'BioGraph*':'yellowgreen', 'breakdancer':'peru', 'clever':'gold', 'delly':'darkorange', 'delly':'mediumorchid', 
             'gasv':'firebrick', 'gridss':'cornflowerblue', 'indelminer':'forestgreen', 
             'mistrvar':'salmon', 'pindel':'darkorange', 'popdel':'navy', 'rdxplorer':'darkgray', 
             'smoove':'orangered',  'true deletions':'black',  'crest':'red', 'genomestrip':'pink','manta_diploidSV':'aqua','Tardis':'lime','VISTA': 'black','surv': 'purple','parl':'magenta','jasmine': 'lightblue'}

tools = ["indelminer","genomestrip","crest","gasv","mistrvar","rdxplorer","popdel","Tardis","pindel","BioGraph*","breakdancer","smoove","delly","gridss","manta_diploidSV","clever","surv","jasmine","parl","VISTA"]
labels    = ["indelMINER","GenomeSTRiP","CREST","GASV","MiStrVar","RDXplorer","PopDel","Tardis","Pindel","BioGraph*","BreakDancer","LUMPY","DELLY","GRIDSS","Manta","CLEVER","SURVIVOR*","Jasmine*","Parliament2*","VISTA*"]
thresholds = df_merge['threshold'].unique()

# # This is for computing plots for each individual strain
# df_merge = df_merge[df_merge['strain'] == 'DBA_2J']

# fig, axes = plt.subplots(1, len(thresholds), figsize=(5*len(thresholds), 5), sharey=True)

# for i, threshold in enumerate(thresholds):
#     data = df_merge[df_merge['threshold'] == threshold]
    
#     data = data.sort_values(by='f-score', ascending=True)
    
#     # Create a bar plot
#     sns.barplot(x="tool", y="f-score", data=data, ax=axes[i], palette=color_map)
    
#     axes[i].set_title(f'Threshold: {threshold} (bp)')
#     axes[i].set_xlabel('Tool')
#     axes[i].set_ylabel('F-Score')

# for ax in axes:
#     ax.set_xticklabels([])

# sns.despine()
# plt.legend(handles=[plt.Rectangle((0,0),1,1, color=color_map[tool]) for tool in tools], labels=labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
# plt.tight_layout()
# plt.show()

# plt.savefig("fig1_del_mouse_fscore_DBA_2J", bbox_inches='tight')

df_merge_all = df_merge[df_merge['strain'].isin(['A_J', 'AKR_J', 'BALB_CJ', 'CBA_J', 'C3H_HeJ', 'DBA_2J', 'LP_J'])]

fig, axes = plt.subplots(1, len(thresholds), figsize=(5*len(thresholds), 5), sharey=True)

for i, threshold in enumerate(thresholds):
    data = df_merge_all[df_merge_all['threshold'] == threshold]

    data_avg = data.groupby('tool')['f-score'].mean().reset_index()
    data_avg = data_avg.sort_values(by='f-score', ascending=True)
    print(data_avg)
    # Create a bar plot
    sns.barplot(x="tool", y="f-score", data=data_avg, ax=axes[i], palette=color_map)
    
    axes[i].set_title(f'Threshold: {threshold} (bp)')
    axes[i].set_xlabel('Tool')
    axes[i].set_ylabel('F-Score')

for ax in axes:
    ax.set_xticklabels([])

sns.despine()
plt.legend(handles=[plt.Rectangle((0,0),1,1, color=color_map[tool]) for tool in tools], labels=labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.show()

plt.savefig("fig1_del_mouse_fscore_average", bbox_inches='tight')