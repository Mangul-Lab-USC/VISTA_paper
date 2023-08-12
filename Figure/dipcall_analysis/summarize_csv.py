import os
import sys
import vcf
import re

#AUTHOR: SEUNGMO LEE
input = open(sys.argv[1], "r")
gold = open(sys.argv[2], "r")
reader = vcf.Reader(input)
reader_ref = vcf.Reader(gold)
output = open(sys.argv[3], "a+")

tool_name = sys.argv[1].split("_")[1]
sample_name = sys.argv[1].split("_")[2]
threshold = sys.argv[1].split("_")[3].replace(".vcf","")

ref_50_100 = 0
ref_100_500 = 0
ref_500_1000 = 0
ref_1000 = 0
ref = 0

for line in reader_ref:
    svlen = int(line.INFO['SVLEN'])
    ref += 1
    if svlen >= 50 and svlen <= 100:
        ref_50_100 += 1
    if svlen >= 100 and svlen <= 500:
        ref_100_500 += 1
    if svlen >= 500 and svlen <= 1000:
        ref_500_1000 += 1
    if svlen >= 1000:
        ref_1000 += 1

tp = "TP"
fp = "FP"
tpCount = 0
fpCount = 0

for line in reader:
    svlen = int(line.INFO['SVLEN'])
    if tp in line.INFO['FLAG']:
        tpCount += 1
    if fp in line.INFO['FLAG']:
        fpCount += 1


prec = tpCount / (tpCount + fpCount)

sensitivity = tpCount / ref

with output as f:
        sys.stdout = f
        # print(sys.argv[1]+"\n")
        # print("f score: ", (2 * prec * sensitivity) / (prec + sensitivity))
        # print("Precision: ", prec)
        # print("Sensitivity: ", sensitivity)
        # print("\n")
        print(tool_name,",",threshold,",",sample_name,",",sensitivity,",",prec,",",((2 * prec * sensitivity) / (prec + sensitivity)))
