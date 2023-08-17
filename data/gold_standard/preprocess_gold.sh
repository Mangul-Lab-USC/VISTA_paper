#!/bin/bash

zcat HG002_SVs_Tier1_v0.6.vcf.gz | grep -v ^# | grep "SVTYPE=DEL" | grep -v "^X" | grep -v "^Y"| awk -F '[\t]' '{f=$10; split(f,gt,":"); if (gt[1] == "0/1" || gt[1] == "1/1") print $0}' | sed 's/;/\t/g' | cut -f 1,2,36 | sed 's;END=;;g' | awk '{if($3 - $2 >= 50){print $0}}' | sort -u -n -k1,1 -k2,2 -k3,3 > truth.bed

bedtools intersect -wa -u -f 1 -a truth.bed -b HG002_SVs_Tier1_v0.6.bed > truth_highConf.bed

# For insertions, just filtered SVTYPE=INS using .py script