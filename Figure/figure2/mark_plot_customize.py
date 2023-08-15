import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import sys

df = pd.read_csv('Human_mark.csv')

df_100 = df[df['threshold'] == 100]

y = sys.argv[1]

tools = df_100['tool'].unique()
fig, ax = plt.subplots(figsize=(12, 8))

colors = {'smoove':'orangered','genomestrip':'pink','manta':'aqua', 'VISTA':'black','parl':'magenta','surv':'purple','jasmine':'lightblue',
          'octopus':'coral','delly':'darkorange'}


label_mapping = {
    'jasmine': 'Jasmine*',
    'octopus': 'Octopus',
    'VISTA': 'VISTA*',
    'parl': 'Parliament2*',
    'delly': 'DELLY',
    'surv': 'SURVIVOR*',
    'smoove': 'Smoove',
    'manta': 'Manta'
}

for i, tool in enumerate(tools):
    tool_df = df_100[df_100['tool'] == tool]
    if y == "f-score":
        ax.plot(tool_df['strain'], tool_df['f-score'], color=colors[tool.replace(" ","")], label=tool)
        ax.scatter(tool_df['strain'], tool_df['f-score'], color=colors[tool.replace(" ","")], s=10)
    if y == "sensitivity": 
        ax.plot(tool_df['strain'], tool_df['sensitivity'], color=colors[tool.replace(" ","")], linestyle='dashed')
        ax.scatter(tool_df['strain'], tool_df['sensitivity'], color=colors[tool.replace(" ","")], s=10)

    if y == "precision" :
        ax.plot(tool_df['strain'], tool_df['precision'], color=colors[tool.replace(" ","")], linestyle='dotted')
        ax.scatter(tool_df['strain'], tool_df['precision'], color=colors[tool.replace(" ","")], s=10)

ax.set_xlabel('Human strains')
y = y.capitalize()
ax.set_ylabel(str(y))

ax.set_ylim(0, 1)

tool_legend_elements = [Line2D([0], [0], color=colors[tool.replace(" ","")], label=label_mapping[tool.replace(" ","")]) for i, tool in enumerate(tools)]
line_legend_elements = [
    Line2D([0], [0], color='black', label='F-Score'),
    Line2D([0], [0], color='black', linestyle='dashed', label='Sensitivity'),
    Line2D([0], [0], color='black', linestyle='dotted', label='Precision')
]

# Create a separate legend box for the tool names
tool_legend = ax.legend(handles=tool_legend_elements, loc='upper left', bbox_to_anchor=(1, 0.5))

# Create a separate legend box for F-score, Precision, and Sensitivity
line_legend = ax.legend(handles=line_legend_elements, loc='lower center', bbox_to_anchor=(0.5, -0.2), ncol=3)

# Add the line legend and tool legend back to the plot
ax.add_artist(tool_legend)
ax.add_artist(line_legend)

plt.xticks(rotation=45)

plt.tight_layout()

# Show the plot
plt.show()
plt.savefig("mark_plot_"+ sys.argv[1]+".png", bbox_inches='tight')
