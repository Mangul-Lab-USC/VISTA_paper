import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_merge = pd.read_csv('Human_ins.csv')

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
    'VISTA': 'black',
    'Parliament2': 'magenta',
    'transIndel': 'gray'
}

tools = ['manta', 'Parliament2', 'DELLY', 'transIndel', 'VISTA']
labels = ['Manta', 'Parliament2*', 'DELLY', 'transIndel', 'VISTA*']
thresholds = df_merge['threshold'].unique()

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

angles = np.linspace(0, 2 * np.pi, len(tools), endpoint=False)

caller_precision_dict = {}

threshold_colors = plt.cm.RdBu(np.linspace(0, 1, len(thresholds)))

data_10000 = df_merge[df_merge['threshold'] == 10000]
data_10000 = data_10000.sort_values(by='f-score')

labels_sorted = [labels[tools.index(tool)] for tool in data_10000['tool']]

for i, threshold in enumerate(thresholds):
    data = df_merge[df_merge['threshold'] == threshold]
    
    data = data.set_index('tool').loc[data_10000['tool']].reset_index()
    
    caller_precision_dict[threshold] = {caller: precision for caller, precision in zip(labels_sorted, data['f-score'])}
    
    color = threshold_colors[i]
    
    ax.plot(angles, data['f-score'], marker='o', label=f'Threshold: {threshold} (bp)', color=color, linewidth=0.7, markersize=5)

ax.set_xticks(angles)
ax.set_xticklabels([])  # Hide original radial tick labels
# ax.set_yticklabels([0.2, 0.4, 0.6, 0.8, 1])

for angle, label in zip(angles, labels_sorted):
    ax.text(angle, ax.get_ylim()[1] +0.02, label, ha='center', va='center')

ax.legend(loc='upper right', bbox_to_anchor=(1.55, 1))

plt.title('F-Score for Insertion', y= 1.18)
plt.tight_layout()
plt.subplots_adjust(right=0.9)
plt.show()

plt.savefig("circle_HG_ins.png", bbox_inches='tight',dpi=300)