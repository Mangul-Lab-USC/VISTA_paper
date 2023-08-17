#!/bin/bash

wget ftp://ftp-trace.ncbi.nlm.nih.gov/giab/ftp/data/AshkenazimTrio/HG002_NA24385_son/NIST_Illumina_2x250bps/novoalign_bams/HG002.hs37d5.2x250.bam

module load samtools

samtools addreplacerg -r ID:RG_ALL -r PL:ILLUMINA -r SM:HG002 HG002.hs37d5.2x250.bam -o HG002.hs37d5_withRG.bam -@4

samtools sort HG002.hs37d5_withRG.bam -o HG002.hs37d5.2x250_withRG_sorted.bam -@4

module load picard

picard MarkDuplicates I=HG002.hs37d5.2x250_withRG_sorted.bam O=HG002.hs37d5.2x250_withRG_sorted_dupMark.bam M=markDup_metrics.txt


