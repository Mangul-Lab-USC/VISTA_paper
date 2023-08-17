import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df_merge = pd.read_csv('Human_del_Sens_Opt.csv')

# Define the color map
color_map = {
    'BREAKDANCER': 'peru',
    'clever': 'gold',
    'grom': 'forestgreen',
    'DELLY': 'mediumorchid',
    'gasv': 'firebrick',
    'tardis': 'lime',
    'popdel': 'navy',
    'rdxplorer': 'darkgray',
    'smoove': 'orangered',
    'crest': 'red',
    'GENOMESTRIP': 'pink',
    'manta': 'aqua',
    'deepvariant': 'rosybrown',
    'octopus': 'coral',
    'svpred': 'black',
    'surv': 'purple',
    'jasmine': 'lightblue',
    'parl': 'magenta'
}

tools = ['crest','gasv','smoove','GENOMESTRIP','BREAKDANCER','tardis','rdxplorer','popdel','clever',
       'grom','deepvariant','octopus','DELLY','manta','jasmine','surv','parl','svpred']
labels = ['CREST','GASV','LUMPY','GenomeSTRiP','BreakDancer','Tardis','RDXplorer','PopDel','CLEVER',
          'GROM','Deepvariant','Octopus','DELLY','Manta','Jasmine*','SURVIVOR*','Parliament2*','VISTA*']

thresholds = df_merge['threshold'].unique()

fig, axes = plt.subplots(1, len(thresholds), figsize=(5*len(thresholds), 5), sharey=True)

for i, threshold in enumerate(thresholds):
    data = df_merge[df_merge['threshold'] == threshold]
    
    data = data.sort_values(by='sensitivity', ascending=True)
    
    # Create a bar plot
    sns.barplot(x="tool", y="sensitivity", data=data, ax=axes[i], palette=color_map)
    
    axes[i].set_title(f'Threshold: {threshold} (bp)')
    axes[i].set_xlabel('Tool')
    axes[i].set_ylabel('Sensitivity')

for ax in axes:
    ax.set_xticklabels([])

sns.despine()
plt.legend(handles=[plt.Rectangle((0,0),1,1, color=color_map[tool]) for tool in tools], labels=labels, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.tight_layout()
plt.show()

plt.savefig("fig1_del_recall_sensitivity_opt_HG.png", bbox_inches='tight',dpi=300)
