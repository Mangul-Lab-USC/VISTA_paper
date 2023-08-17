import sys
import csv
import vcf

#Author: Seungmo Lee
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

def main():
    vcf_files = sys.argv[1:]
    if not vcf_files:
        print("Please provide one or more VCF files as command line arguments.")
        return
    
    csv_data = []
    for vcf_file in vcf_files:
        lengths = extract_lengths(vcf_file)
        tool = vcf_file.split('_')[0]  # Extract tool name from the file name
        csv_data.extend([(length, tool) for length in lengths])

    csv_filename = 'numcalls_others.csv'
    with open(csv_filename, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['length', 'tool'])
        writer.writerows(csv_data)

    print(f"CSV file '{csv_filename}' has been created.")

if __name__ == '__main__':
    main()
