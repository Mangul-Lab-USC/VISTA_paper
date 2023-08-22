import sys
import re

#AUTHOR: SEUNGMO LEE

def starts_with_number(line):
    pattern = r'^\d'
    return re.match(pattern, line) is not None

def merge_vcfs(input_files, output_file):
    merged_records = []
    header_lines = "##fileformat=VCFv4.2\n\
    ##source=SVPred\n\
    ##INFO=<ID=SVTYPE,Number=1,Type=String,Description=\"Type of structural variant detected\">\n\
    ##INFO=<ID=SVLEN,Number=1,Type=Integer,Description=\"Length of structural variant\">\n\
    ##INFO=<ID=END,Number=1,Type=Integer,Description=\"End position of structural variant\">\n\
    ##CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\tHG002\n"

    for file_name in input_files:
        with open(file_name, 'r') as vcf_file:
            for line in vcf_file:
                if not line.startswith('##') and not line.startswith("#") and starts_with_number(line):
                    merged_records.append(line)

    with open(output_file, 'w') as merged_vcf:
        merged_vcf.write(header_lines)
        for record_line in merged_records:
            merged_vcf.write(record_line)

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python merging.py output_file.vcf vcf1.vcf vcf2.vcf ... vcf10.vcf \n Input more than one")
    else:
        input_files = sys.argv[2:]
        output_file = sys.argv[1]
        merge_vcfs(input_files, output_file)
