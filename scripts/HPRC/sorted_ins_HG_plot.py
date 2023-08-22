import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df_merge = pd.read_csv('Human_ins_50_500.csv')

# Define the color map
color_map = {
             'BREAKDANCER':'peru', 
             'clever':'gold', 
             'grom':'forestgreen', 
             'DELLY':'mediumorchid', 
             'gasv':'firebrick', 
             'tardis':'lime',
             'popdel':'navy', 
             'rdxplorer':'darkgray', 
             'smoove':'orangered',  
             'crest':'red', 
             'GENOMESTRIP':'pink',
             'manta':'aqua',
            'deepvariant':'rosybrown',
            'octopus':'coral',
             'VISTA':'black',
             'Parliament2':'magenta',
             'transIndel':'gray'}

tools=['manta','Parliament2','DELLY','transIndel','VISTA']
labels=['Manta','Parliament2*','DELLY','transIndel','VISTA*']

thresholds = df_merge['threshold'].unique()

fig, axes = plt.subplots(1, len(thresholds), figsize=(5*len(thresholds), 5), sharey=True)

for i, threshold in enumerate(thresholds):
    data = df_merge[df_merge['threshold'] == threshold]
    
    data = data.sort_values(by='sensitivity', ascending=True)
    
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

plt.savefig("fig1_ins_recall_50_500.png", bbox_inches='tight')
