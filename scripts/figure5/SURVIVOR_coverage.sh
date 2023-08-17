#!/bin/bash

# Set the required variables
samples=('AKR_J' 'A_J' 'BALB_cJ' 'C3H_HeJ' 'CBA_J' 'DBA_2J' 'LP_J')
coverages=(0.5 1 2 4 8 16 32)
tools=('manta_diploidSV' 'delly' 'smoove')
subsamples=(1 2 3 4 5 6 7 8 9 10)
threshold=100

# Iterate over the combinations of variables
for sample in "${samples[@]}"; do
  for cov in "${coverages[@]}"; do
    for n in "${subsamples[@]}"; do
      # Generate the sample.txt file name
      txt_file="sample_${sample}_${cov}x_${n}.txt"
      
      for tool in "${tools[@]}"; do
        vcf_file="/u/project/zarlab/seichang/benchmarking_SV_publication/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.$tool.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
        echo "$vcf_file" >> "$txt_file"
      done
      
      command="./SURVIVOR merge $txt_file 1000 2 1 1 0 50 nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.temp_modified.vcf"
      
      python fix_space.py "nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.temp_modified.vcf" "temp_nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"

      rm "nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.temp_modified.vcf"
      ref="/u/project/zarlab/seichang/benchmarking_SV_publication/Data/gold_standard/mouse_vcf/${sample}_reference.vcf"

      python compare_script.py 100 "temp_nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.modified.vcf" $ref "nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"

      rm "temp_nf_100t.surv.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"

      # Execute the SURVIVOR command
      echo "Executing: $command"
      $command
      
      echo "Finished SURVIVOR for $sample $cov x subsample $n"
    done
  done
done
