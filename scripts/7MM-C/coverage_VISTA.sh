#!/bin/bash

samples=('AKR_J' 'A_J' 'BALB_cJ' 'C3H_HeJ' 'CBA_J' 'DBA_2J' 'LP_J')
coverages=(0.5 1 2 4 8 16 32)
subsamples=(1 2 3 4 5 6 7 8 9 10)
threshold=100

for sample in "${samples[@]}"; do
  for cov in "${coverages[@]}"; do
    for n in "${subsamples[@]}"; do
      
      # Generate the VISTA command
      out_file="nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
      tool1="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.manta_diploidSV.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
      tool2="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.gridss.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
      tool3="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.delly.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
      tool4="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.manta_diploidSV.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"

      command="python coverage_vista_merger.py temp_nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf manta_diploidSV gridss delly manta_diploidSV $tool1 $tool2 $tool3 $tool4"
      
      # Execute the VISTA command
      $command
      echo "Finished VISTA for $sample $cov x subsample $n"
      ref="/u/home/m/mdistler/benchmarking_SV/Data/gold_standard/mouse_vcf/${sample}_reference.vcf"
      python compare_script.py 100 "temp_nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf" $ref $out_file
      rm "temp_nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
      cp "nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf" "/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t"
    done
  done
done


# samples=('AKR_J' 'A_J' 'BALB_cJ' 'C3H_HeJ' 'CBA_J' 'DBA_2J' 'LP_J')
# coverages=(32)
# subsamples=(1 2 3 4 5 6 7 8 9 10)
# threshold=100

# for sample in "${samples[@]}"; do
#   for cov in "${coverages[@]}"; do
#     for n in "${subsamples[@]}"; do
      
#       # Generate the VISTA command
#       out_file="nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
#       tool1="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.manta_diploidSV.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
#       tool2="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.manta_diploidSV.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
#       tool3="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.manta_diploidSV.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
#       tool4="/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t/nf_100t.manta_diploidSV.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"

#       command="python coverage_vista_merger.py temp_nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf manta_diploidSV manta_diploidSV manta_diploidSV manta_diploidSV $tool1 $tool2 $tool3 $tool4"
      
#       # Execute the VISTA command
#       $command
#       echo "Finished VISTA for $sample $cov x subsample $n"
#       ref="/u/home/m/mdistler/benchmarking_SV/Data/gold_standard/mouse_vcf/${sample}_reference.vcf"
#       python compare_script.py 100 "temp_nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf" $ref $out_file
#       rm "temp_nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf"
#       cp "nf_100t.VISTA.$sample.chr19.${cov}p.${n}_sorted.modified.vcf" "/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_${cov}x/100t"
#     done
#   done
# done