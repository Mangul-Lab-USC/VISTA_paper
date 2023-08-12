import matplotlib.pyplot as plt
from matplotlib_venn import venn3
import vcf

def get_contig_19_variants(file_path):
    contig_19_variants = set()
    vcf_reader = vcf.Reader(filename=file_path)
    for record in vcf_reader:
        if record.CHROM == '19':
            contig_19_variants.add(record.POS)
    return contig_19_variants

def create_venn_diagram(vcf_files):
    contig_19_variants = [get_contig_19_variants(file) for file in vcf_files]
    venn_labels = [set(map(str, variants)) for variants in contig_19_variants]
    venn = venn3(venn_labels, ("GIAB Truth", "SURVIVOR", "VISTA"))
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
    
    plt.savefig('venn_mouse.png')
    plt.show()


if len(sys.argv) != 4:
    print("Needs Three Plz. First should be always gold")
    sys.exit(1)

vcf_files = sys.argv[1:]
create_venn_diagram(vcf_files)