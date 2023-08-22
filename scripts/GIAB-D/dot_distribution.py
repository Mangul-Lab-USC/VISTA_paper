import sys
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

color_map = {
    'BREAKDANCER': 'peru',
    'clever': 'gold',
    'DELLY': 'darkorange',
    'DELLY': 'mediumorchid',
    'gasv': 'firebrick',
    'pindel': 'darkorange',
    'popdel': 'navy',
    'smoove': 'orangered',
    'GENOMESTRIP': 'pink',
    'manta': 'aqua',
    'VISTA': 'black',
    'parl': 'magenta',
    'surv': 'purple',
    'jasmine': 'lightblue',
    'true deletions': '#39FF14',
    'octopus': 'coral'
}

labels = [
    'Octopus', 'Pindel', 'Manta', 'True Deletions', 'VISTA*', 'CLEVER',
    'Jasmine*', 'Survivor*', 'DELLY', 'PopDel', 'Parliament2*',
    'BreakDancer', 'GASV', 'smoove', 'GenomeSTRiP'
]

fig_order = [
    'octopus', 'pindel', 'manta', 'true deletions', 'VISTA', 'clever',
    'jasmine', 'surv', 'DELLY', 'popdel', 'parl', 'BREAKDANCER', 'gasv',
    'smoove', 'GENOMESTRIP'
]


def read_data(csv_file):
    data = pd.read_csv(csv_file)
    lengths = data['length'].values
    tools = data['tool'].values
    return lengths, tools

def plot_violinplot(csv_file):
    lengths, tools = read_data(csv_file)
    data = []
    for tool in fig_order:
        tool_lengths = lengths[tools == tool]
        data.append(tool_lengths)

    sns.set_style("whitegrid")
    fig, ax = plt.subplots(figsize=(10, 8))

    for i, tool_data in enumerate(data):
        x = np.random.normal(i + 1, 0.04, len(tool_data))
        color = color_map[fig_order[i]]

        if fig_order[i] == 'true deletions':
            median_true_deletions = np.median(tool_data)
            ax.axhline(y=median_true_deletions, linestyle='dashed', color=color, label='True Deletions')

        ax.plot(x, tool_data, marker='o', linestyle='', markersize=5, color=color, alpha=0.6)
        
    # Add median and IQR boxes
    boxprops = dict(facecolor='white', color='black', linewidth=0.5)
    whiskerprops = dict(color='gray', linewidth=0.5)
    medianprops = dict(color='gray', linewidth=0.5)
    capprops = dict(color='gray', linewidth=0.5)
    bp = ax.boxplot(data, patch_artist=True, showfliers=False, medianprops=medianprops,
                    boxprops=boxprops, whiskerprops=whiskerprops, capprops=capprops)

    for box, color in zip(bp['boxes'], [color_map[tool] for tool in fig_order]):
        box.set(alpha=0.5)

    plt.xticks(range(1, len(fig_order) + 1), labels, rotation=45, ha='right', fontsize=12)
    plt.yscale('log')
    # plt.ylim(0, 100000)

    plt.xlabel('Tools', fontsize=14, labelpad=10)
    plt.ylabel('Length (bp)', fontsize=14, labelpad=10)
    plt.title('Length Distribution of Tools', fontsize=16, pad=20)

    sns.despine()

    ax.set_facecolor('white')
    ax.grid(color='white', linestyle='-', linewidth=0.5)

    plt.savefig('dot_distribution_plot+prac.png', dpi=300, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: python length_dist.py numcalls.csv')
        sys.exit(1)

    csv_file = sys.argv[1]
    plot_violinplot(csv_file)