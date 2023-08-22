#!/bin/bash

TOOLNAME=$1
CSVOUTPUTFILE=$2

HUMAN_SAMPLES=($(ls ${TOOLNAME}_*.vcf | awk -F'_' '{print $2}' | awk -F'.' '{print $1}'))

for sample_name in "${HUMAN_SAMPLES[@]}"; do
  echo "Detected $sample_name"
done

for SAMPLE_NAME in "${HUMAN_SAMPLES[@]}"; do
    echo "Running $SAMPLE_NAME"
    for THRESHOLD in 10 100 1000 10000; do
        python compare_script.py $THRESHOLD ${TOOLNAME}_${SAMPLE_NAME}.vcf ${SAMPLE_NAME}_reference.vcf modified_${TOOLNAME}_${SAMPLE_NAME}_${THRESHOLD}.vcf

        python summarize_csv.py modified_${TOOLNAME}_${SAMPLE_NAME}_${THRESHOLD}.vcf ${SAMPLE_NAME}_reference.vcf $CSVOUTPUTFILE
    done
done
