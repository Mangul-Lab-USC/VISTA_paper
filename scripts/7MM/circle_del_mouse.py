import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

df_merge = pd.read_csv('df_merged.csv')

color_map = {'BioGraph*':'yellowgreen', 'breakdancer':'peru', 'clever':'gold', 'delly':'darkorange', 'delly':'mediumorchid', 
             'gasv':'firebrick', 'gridss':'cornflowerblue', 'indelminer':'forestgreen', 
             'mistrvar':'salmon', 'pindel':'darkorange', 'popdel':'navy', 'rdxplorer':'darkgray', 
             'smoove':'orangered',  'true deletions':'black',  'crest':'red', 'genomestrip':'pink','manta_diploidSV':'aqua','Tardis':'lime','VISTA': 'black','surv': 'purple','parl':'magenta','jasmine': 'lightblue'}

tools = ["indelminer","genomestrip","crest","gasv","mistrvar","rdxplorer","popdel","Tardis","pindel","BioGraph*","breakdancer","smoove","delly","gridss","manta_diploidSV","clever","surv","jasmine","parl","VISTA"]
labels    = ["indelMINER","GenomeSTRiP","CREST","GASV","MiStrVar","RDXplorer","PopDel","Tardis","Pindel","BioGraph*","BreakDancer","LUMPY","DELLY","GRIDSS","Manta","CLEVER","SURVIVOR*","Jasmine*","Parliament2*","VISTA*"]
thresholds = df_merge['threshold'].unique()

df_merge_all = df_merge[df_merge['strain'].isin(['A_J', 'AKR_J', 'BALB_CJ', 'CBA_J', 'C3H_HeJ', 'DBA_2J', 'LP_J'])]

fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

# Calculate the angles for the lines in the circular plot
angles = np.linspace(0, 2 * np.pi, len(tools), endpoint=False)

# Create a dictionary to store each caller's precision for each threshold
caller_precision_dict = {}

threshold_colors = plt.cm.RdBu(np.linspace(0, 1, len(thresholds)))

# Sort the data based on precision in ascending order for threshold 10000
data_10000 = df_merge_all[df_merge_all['threshold'] == 10000]
data_10000_avg = data_10000.groupby('tool')['f-score'].mean().reset_index()

data_10000_avg = data_10000_avg.sort_values(by='f-score', ascending=True)

# Update the labels to match the sorted order
labels_sorted = [labels[tools.index(tool)] for tool in data_10000_avg['tool']]

for i, threshold in enumerate(thresholds):
    data = df_merge_all[df_merge_all['threshold'] == threshold]
    data_avg = data.groupby('tool')['f-score'].mean().reset_index()
    # Sort the data based on precision in ascending order of threshold 10000
    data_avg = data_avg.set_index('tool').loc[data_10000_avg['tool']].reset_index()
    
    # Store the caller precision values in the dictionary
    caller_precision_dict[threshold] = {caller: precision for caller, precision in zip(labels_sorted, data['f-score'])}
    
    color = threshold_colors[i]
    
    # Draw lines for each threshold
    ax.plot(angles, data_avg['f-score'], marker='o', label=f'Threshold: {threshold} (bp)', color=color, linewidth=0.7, markersize=5)

# Set the radial ticks and labels
ax.set_xticks(angles)
ax.set_xticklabels([])  # Hide original radial tick labels
# ax.set_yticklabels([0.2, 0.4, 0.6, 0.8, 1])


# Place the tool labels outside the circle
for angle, label in zip(angles, labels_sorted):
    ax.text(angle, ax.get_ylim()[1] + 0.18, label, ha='center', va='center')

# # Add legend outside the circular plot
ax.legend(loc='upper right', bbox_to_anchor=(1.55, 1))

plt.title('F-Score', y= 1.18)
plt.tight_layout()
plt.subplots_adjust(right=0.9)
plt.show()

plt.savefig("circle_mouse_del.png", bbox_inches='tight',dpi=300)
