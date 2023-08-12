import matplotlib.pyplot as plt
import vcf
import sys
from matplotlib_venn import venn3, venn3_circles

# Input VCF files
input_vcf1 = sys.argv[1]
input_vcf2 = sys.argv[2]
input_vcf3 = sys.argv[3]

threshold = 100

def is_overlap(variant1, variant2):
    start1, end1 = variant1
    start2, end2 = variant2
    return abs(start1 - start2) <= threshold and abs(end1 - end2) <= threshold

# Function to categorize the variants into different subsets
def categorize_variants(vcf1_variants, vcf2_variants, vcf3_variants):
    overlap_1_2_3 = []
    overlap_1_2_not_3 = []
    overlap_1_3_not_2 = []
    overlap_2_3_not_1 = []
    only1_no_overlap = []
    only2_no_overlap = []
    only3_no_overlap = []

    for variant1 in vcf1_variants:
        overlap_1_2 = False
        overlap_1_3 = False

        for variant2 in vcf2_variants:
            if is_overlap(variant1, variant2):
                overlap_1_2 = True
                vcf2_variants.remove(variant2)
                break

        for variant3 in vcf3_variants:
            if is_overlap(variant1, variant3):
                overlap_1_3 = True
                vcf3_variants.remove(variant3)
                break

        if overlap_1_2 and overlap_1_3:
            overlap_1_2_3.append(variant1)
        elif overlap_1_2 and not overlap_1_3:
            overlap_1_2_not_3.append(variant1)
        elif overlap_1_3 and not overlap_1_2:
            overlap_1_3_not_2.append(variant1)
        else:
            only1_no_overlap.append(variant1)

    for variant2 in vcf2_variants:
        overlap_2_3 = False

        for variant3 in vcf3_variants:
            if is_overlap(variant2, variant3):
                overlap_2_3 = True
                break

        if overlap_2_3 and variant2 not in overlap_1_2_3 and variant2 not in overlap_1_2_not_3:
            overlap_2_3_not_1.append(variant2)
        elif variant2 not in overlap_1_2_3 and variant2 not in overlap_1_2_not_3 and variant2 not in overlap_1_3_not_2:
            only2_no_overlap.append(variant2)

    for variant3 in vcf3_variants:
        if variant3 not in overlap_1_2_3 and variant3 not in overlap_1_3_not_2 and variant3 not in overlap_2_3_not_1:
            only3_no_overlap.append(variant3)

    return overlap_1_2_3, overlap_1_2_not_3, overlap_1_3_not_2, overlap_2_3_not_1, only1_no_overlap, only2_no_overlap, only3_no_overlap

# Set the overlap threshold
threshold = 100

def get_contig_19_variants(file_path):
    contig_19_variants = set()
    vcf_reader = vcf.Reader(filename=file_path)
    for record in vcf_reader:
        if record.CHROM == '19':
            contig_19_variants.add((record.POS,record.INFO["END"]))
    return contig_19_variants

vcf1_variants = get_contig_19_variants(sys.argv[1])
vcf2_variants = get_contig_19_variants(sys.argv[2])
vcf3_variants = get_contig_19_variants(sys.argv[3])

print(len(vcf1_variants))

overlap_1_2_3, overlap_1_2_not_3, overlap_1_3_not_2, overlap_2_3_not_1, only1_no_overlap, only2_no_overlap, only3_no_overlap = categorize_variants(
    vcf1_variants, vcf2_variants, vcf3_variants
)

venn_labels = ("GIAB Truth", "SURVIVOR*", "VISTA*")
venn_subsets = (len(only1_no_overlap),len(only2_no_overlap),len(overlap_1_2_not_3),len(only3_no_overlap),len(overlap_1_3_not_2),len(overlap_2_3_not_1),len(overlap_1_2_3))

venn = venn3(subsets=venn_subsets, set_labels=venn_labels)
venn_circles = venn3_circles(subsets=venn_subsets, linewidth=1)

venn.get_patch_by_id('100').set_facecolor('white')
venn.get_patch_by_id('010').set_facecolor('white')
venn.get_patch_by_id('001').set_facecolor('white')
# venn.get_patch_by_id('110').set_facecolor('white')
# venn.get_patch_by_id('101').set_facecolor('white')
# venn.get_patch_by_id('011').set_facecolor('white')
# venn.get_patch_by_id('111').set_facecolor('white')
venn.get_patch_by_id('100').set_edgecolor('red')
venn.get_patch_by_id('010').set_edgecolor('blue')
venn.get_patch_by_id('001').set_edgecolor('green')
# Save the diagram to a file
output_file = 'venn_surv_HG.png'
plt.savefig(output_file)
