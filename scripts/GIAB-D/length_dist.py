import sys
import matplotlib.pyplot as plt
import numpy as np
import vcf
import seaborn as sns

# Author: Seungmo Lee
def extract_lengths(vcf_file):
    lengths = []
    vcf_reader = vcf.Reader(open(vcf_file, 'r'))
    for record in vcf_reader:
        info = record.INFO
        if 'SVLEN' in info:
            svlen = info['SVLEN']
            if isinstance(svlen, list):
                lengths.extend(svlen)
            else:
                lengths.append(svlen)
    return lengths

def plot_boxplots(vcf_files):
    data = []
    labels = []
    for vcf_file in vcf_files:
        lengths = extract_lengths(vcf_file)
        data.append(lengths)
        labels.append(vcf_file)
    
    sns.violinplot(data=data, inner="box")
    plt.xticks(range(len(vcf_files)), [item.split('_')[0] for item in vcf_files])

    
    plt.ylim(0, 1000)

    plt.xlabel('VCF Files')
    plt.ylabel('Length')
    plt.title('Length Distribution of VCF Files')


    plt.savefig('violinplot_ins.png', dpi=300)  # Save as PNG file
    plt.close()

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python length_dist.py vcf1.vcf vcf2.vcf vcf3.vcf ...')
        sys.exit(1)

    vcf_files = sys.argv[1:]
    plot_boxplots(vcf_files)
