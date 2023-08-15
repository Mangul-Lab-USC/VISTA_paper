#!/bin/bash

#Author: Seungmo Lee

output_folder="/u/home/m/mdistler/project-zarlab/figure/markdata"
main_manta_folder="/u/home/m/mdistler/project-zarlab/figure/markdata/results/manta"

main_delly_folder="/u/home/m/mdistler/project-zarlab/figure/markdata/results/delly"

main_smoove_folder="/u/home/m/mdistler/project-zarlab/figure/markdata/results/smoove"

main_octopus_folder="/u/home/m/mdistler/project-zarlab/figure/markdata/results/octopus"
manta_to_vcf_script="/u/home/m/mdistler/project-zarlab/MANTAtoVCF.py"
delly_to_vcf_script="/u/home/m/mdistler/project-zarlab/figure/DELLYtoVCF.py"
smoove_to_vcf_script="/u/home/m/mdistler/project-zarlab/figure/LUMPYtoVCF.py"
octopus_to_vcf_script="/u/home/m/mdistler/project-zarlab/figure/markdata/OCTOPUStoVCF.py"

subfolders=$(find "$main_manta_folder" -mindepth 1 -type d)

for folder in $subfolders; do
    genome_name=$(basename "$folder")
    
    vcf_file="$folder/diploidSV.vcf"
    
    python "$manta_to_vcf_script" "$vcf_file" "$folder/manta_$genome_name.vcf"
    
    mv "$folder/manta_$genome_name.vcf" "$output_folder/manta_$genome_name.vcf"
done

# __________________________
# DELLY

subfolders=$(find "$main_delly_folder" -mindepth 1 -type d)

for folder in $subfolders; do
    genome_name=$(basename "$folder")
    
    vcf_file="$folder/sv.bcf"

    module load bcftools

    bcftools view "$vcf_file" -Ov -o "$folder/sv.vcf"
    
    vcf_file="$folder/sv.vcf"

    python "$delly_to_vcf_script" "$vcf_file" "$folder/delly_$genome_name.vcf"
    
    cp "$folder/delly_$genome_name.vcf" "$output_folder/delly_$genome_name.vcf"
done

#________________
#Smoove

vcf_files=$(find "$main_smoove_folder" -name "HG*-smoove.genotyped.vcf")

for vcf_file in $vcf_files; do
    genome_name=$(basename "$vcf_file" -smoove.genotyped.vcf)
    
    python "$smoove_to_vcf_script" "$vcf_file" "$main_smoove_folder/smoove_$genome_name.vcf"
    
    cp "$main_smoove_folder/smoove_$genome_name.vcf" "$output_folder/smoove_$genome_name.vcf"
done

#_____________
#Parl:

parl_to_vcf_script="/u/home/m/mdistler/project-zarlab/figure/markdata/PARLtoVCF.py"
main_parl_folder="/u/home/m/mdistler/project-zarlab/figure/markdata/results/parliament2"

output_folder="/u/home/m/mdistler/project-zarlab/figure/markdata"

subfolders=$(find "$main_parl_folder" -mindepth 1 -type d)

for folder in $subfolders; do
    genome_name=$(basename "$folder")
    
    vcf_file="$folder/input.combined.genotyped.vcf"
    
    python "$parl_to_vcf_script" "$vcf_file" "$folder/parl_$genome_name.vcf"
    
    mv "$folder/parl_$genome_name.vcf" "$output_folder/parl_$genome_name.vcf"
done


__________
Octopus


subfolders=$(find "$main_octopus_folder" -mindepth 1 -type d)

for folder in $subfolders; do
    genome_name=$(basename "$folder")
    
    vcf_file="$folder/octopus.vcf"

    python "$octopus_to_vcf_script" "$vcf_file" "$folder/octopus_$genome_name.vcf"
    
    mv "$folder/octopus_$genome_name.vcf" "$output_folder/octopus_$genome_name.vcf"
done


________________
VISTA

folder_path="/u/home/m/mdistler/project-zarlab/figure/markdata"

for file in "$folder_path"/manta_*.vcf; do
  sample_name=$(basename "$file" | sed 's/^manta_\(.*\)\.vcf$/\1/')
  echo "Processing sample: $sample_name"
  python vista_merger.py "VISTA_$sample_name.vcf" "octopus_$sample_name.vcf" "manta_$sample_name.vcf" "delly_$sample_name.vcf" "manta_$sample_name.vcf"
done







