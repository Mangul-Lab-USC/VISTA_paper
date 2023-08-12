import vcf

# merged.vcf is missing so mouse jasmine vcfs are
# probably incorrect

# jasmine_del_vcf = "merged.vcf"
jasmine_HG_vcf = "jasmine.hc.vcf"

reference_vcf = "A_J_reference.vcf"
survivor_del_vcf='survivor.vcf'
parl_del_vcf = "parl.vcf"
deep_del_vcf = "deepvariant_modified.vcf"

parl_HG_vcf = "parl.hc.vcf"
ref_HG_vcf = "gold_HG.vcf"
survivor_HG_vcf='surv_HG.vcf'

# fileoutput_50_100 = "jasmine_50_100.vcf"
# fileoutput_100_500 = "jasmine_100_500.vcf"
# fileoutput_500_1000 = "jasmine_500_1000.vcf"
# fileoutput_1000 = "jasmine_1000.vcf"

fileoutput_HG_50_100 = "jasmine_HG_50_100.vcf"
fileoutput_HG_100_500 = "jasmine_HG_100_500.vcf"
fileoutput_HG_500_1000 = "jasmine_HG_500_1000.vcf"
fileoutput_HG_1000 = "jasmine_HG_1000.vcf"

fileoutput_ref_50_100 = "ref_50_100.vcf"
fileoutput_ref_100_500 = "ref_100_500.vcf"
fileoutput_ref_500_1000 = "ref_500_1000.vcf"
fileoutput_ref_1000 = "ref_1000.vcf"

fileoutput_ref_HG_50_100 = "ref_HG_50_100.vcf"
fileoutput_ref_HG_100_500 = "ref_HG_100_500.vcf"
fileoutput_ref_HG_500_1000 = "ref_HG_500_1000.vcf"
fileoutput_ref_HG_1000 = "ref_HG_1000.vcf"

fileoutput_surv_50_100 = "survivor_50_100.vcf"
fileoutput_surv_100_500 = "survivor_100_500.vcf"
fileoutput_surv_500_1000 = "survivor_500_1000.vcf"
fileoutput_surv_1000 = "survivor_1000.vcf"

fileoutput_surv_HG_50_100 = "surv_HG_50_100.vcf"
fileoutput_surv_HG_100_500 = "surv_HG_100_500.vcf"
fileoutput_surv_HG_500_1000 = "surv_HG_500_1000.vcf"
fileoutput_surv_HG_1000 = "surv_HG_1000.vcf"

fileoutput_parl_50_100 = "parl_50_100.vcf"
fileoutput_parl_100_500 = "parl_100_500.vcf"
fileoutput_parl_500_1000 = "parl_500_1000.vcf"
fileoutput_parl_1000 = "parl_1000.vcf"

fileoutput_deep_50_100 = "deep_50_100.vcf"
fileoutput_deep_100_500 = "deep_100_500.vcf"
fileoutput_deep_500_1000 = "deep_500_1000.vcf"
fileoutput_deep_1000 = "deep_1000.vcf"

fileoutput_parl_HG_50_100 = "parl_HG_50_100.vcf"
fileoutput_parl_HG_100_500 = "parl_HG_100_500.vcf"
fileoutput_parl_HG_500_1000 = "parl_HG_500_1000.vcf"
fileoutput_parl_HG_1000 = "parl_HG_1000.vcf"

#VCF readers
# jasmine_del_reader = vcf.Reader(open(jasmine_del_vcf,'r'))
reference_del_reader = vcf.Reader(open(reference_vcf,'r'))
survivor_del_reader = vcf.Reader(open(survivor_del_vcf,'r'))
parl_del_reader = vcf.Reader(open(parl_del_vcf,'r'))
deep_del_reader = vcf.Reader(open(deep_del_vcf,'r'))
parl_HG_reader = vcf.Reader(open(parl_HG_vcf,'r'))
reference_HG_reader = vcf.Reader(open(ref_HG_vcf,'r'))
jasmine_HG_reader = vcf.Reader(open(jasmine_HG_vcf,'r'))
survivor_HG_reader = vcf.Reader(open(survivor_HG_vcf,'r'))





# vcf_writer_50_100 = vcf.Writer(open(fileoutput_50_100,'w'), jasmine_del_reader)
# vcf_writer_100_500 = vcf.Writer(open(fileoutput_100_500,'w'), jasmine_del_reader)
# vcf_writer_500_1000 = vcf.Writer(open(fileoutput_500_1000,'w'), jasmine_del_reader)
# vcf_writer_1000 = vcf.Writer(open(fileoutput_1000,'w'), jasmine_del_reader)

vcf_writer_HG_50_100 = vcf.Writer(open(fileoutput_HG_50_100,'w'), jasmine_HG_reader)
vcf_writer_HG_100_500 = vcf.Writer(open(fileoutput_HG_100_500,'w'), jasmine_HG_reader)
vcf_writer_HG_500_1000 = vcf.Writer(open(fileoutput_HG_500_1000,'w'), jasmine_HG_reader)
vcf_writer_HG_1000 = vcf.Writer(open(fileoutput_HG_1000,'w'), jasmine_HG_reader)

vcf_writer_surv_50_100 = vcf.Writer(open(fileoutput_surv_50_100,'w'), survivor_del_reader)
vcf_writer_surv_100_500 = vcf.Writer(open(fileoutput_surv_100_500,'w'), survivor_del_reader)
vcf_writer_surv_500_1000 = vcf.Writer(open(fileoutput_surv_500_1000,'w'), survivor_del_reader)
vcf_writer_surv_1000 = vcf.Writer(open(fileoutput_surv_1000,'w'), survivor_del_reader)

vcf_writer_surv_HG_50_100 = vcf.Writer(open(fileoutput_surv_HG_50_100,'w'), survivor_HG_reader)
vcf_writer_surv_HG_100_500 = vcf.Writer(open(fileoutput_surv_HG_100_500,'w'), survivor_HG_reader)
vcf_writer_surv_HG_500_1000 = vcf.Writer(open(fileoutput_surv_HG_500_1000,'w'), survivor_HG_reader)
vcf_writer_surv_HG_1000 = vcf.Writer(open(fileoutput_surv_HG_1000,'w'), survivor_HG_reader)

vcf_writer_ref_50_100 = vcf.Writer(open(fileoutput_ref_50_100,'w'), reference_del_reader)
vcf_writer_ref_100_500 = vcf.Writer(open(fileoutput_ref_100_500,'w'), reference_del_reader)
vcf_writer_ref_500_1000 = vcf.Writer(open(fileoutput_ref_500_1000,'w'), reference_del_reader)
vcf_writer_ref_1000 = vcf.Writer(open(fileoutput_ref_1000,'w'), reference_del_reader)

vcf_writer_ref_HG_50_100 = vcf.Writer(open(fileoutput_ref_HG_50_100,'w'), reference_HG_reader)
vcf_writer_ref_HG_100_500 = vcf.Writer(open(fileoutput_ref_HG_100_500,'w'), reference_HG_reader)
vcf_writer_ref_HG_500_1000 = vcf.Writer(open(fileoutput_ref_HG_500_1000,'w'), reference_HG_reader)
vcf_writer_ref_HG_1000 = vcf.Writer(open(fileoutput_ref_HG_1000,'w'), reference_HG_reader)

vcf_writer_parl_50_100 = vcf.Writer(open(fileoutput_parl_50_100,'w'), parl_del_reader)
vcf_writer_parl_100_500 = vcf.Writer(open(fileoutput_parl_100_500,'w'), parl_del_reader)
vcf_writer_parl_500_1000 = vcf.Writer(open(fileoutput_parl_500_1000,'w'), parl_del_reader)
vcf_writer_parl_1000 = vcf.Writer(open(fileoutput_parl_1000,'w'), parl_del_reader)

vcf_writer_deep_50_100 = vcf.Writer(open(fileoutput_deep_50_100,'w'), deep_del_reader)
vcf_writer_deep_100_500 = vcf.Writer(open(fileoutput_deep_100_500,'w'), deep_del_reader)
vcf_writer_deep_500_1000 = vcf.Writer(open(fileoutput_deep_500_1000,'w'), deep_del_reader)
vcf_writer_deep_1000 = vcf.Writer(open(fileoutput_deep_1000,'w'), deep_del_reader)

vcf_writer_parl_HG_50_100 = vcf.Writer(open(fileoutput_parl_HG_50_100,'w'), parl_HG_reader)
vcf_writer_parl_HG_100_500 = vcf.Writer(open(fileoutput_parl_HG_100_500,'w'), parl_HG_reader)
vcf_writer_parl_HG_500_1000 = vcf.Writer(open(fileoutput_parl_HG_500_1000,'w'), parl_HG_reader)
vcf_writer_parl_HG_1000 = vcf.Writer(open(fileoutput_parl_HG_1000,'w'), parl_HG_reader)


# for record in jasmine_del_reader:
#                 svlen = int(record.INFO['SVLEN'])
#                 if svlen >= 50 and svlen <= 100:
#                         vcf_writer_50_100.write_record(record)
#                 if svlen >= 100 and svlen <= 500:
#                         vcf_writer_100_500.write_record(record)
#                 if svlen >= 500 and svlen <= 1000:
#                         vcf_writer_500_1000.write_record(record)
#                 if svlen >= 1000:
#                         vcf_writer_1000.write_record(record)

for record in jasmine_HG_reader:
                svlen = int(record.INFO['SVLEN'])
                if svlen >= 50 and svlen <= 100:
                        vcf_writer_HG_50_100.write_record(record)
                if svlen >= 100 and svlen <= 500:
                        vcf_writer_HG_100_500.write_record(record)
                if svlen >= 500 and svlen <= 1000:
                        vcf_writer_HG_500_1000.write_record(record)
                if svlen >= 1000:
                        vcf_writer_HG_1000.write_record(record)

for record in survivor_del_reader:
                svlen = int(record.INFO['SVLEN'])
                if svlen >= 50 and svlen <= 100:
                        vcf_writer_surv_50_100.write_record(record)
                if svlen >= 100 and svlen <= 500:
                        vcf_writer_surv_100_500.write_record(record)
                if svlen >= 500 and svlen <= 1000:
                        vcf_writer_surv_500_1000.write_record(record)
                if svlen >= 1000:
                        vcf_writer_surv_1000.write_record(record)

for record in survivor_HG_reader:
                svlen = int(record.INFO['SVLEN'])
                if svlen >= 50 and svlen <= 100:
                        vcf_writer_surv_HG_50_100.write_record(record)
                if svlen >= 100 and svlen <= 500:
                        vcf_writer_surv_HG_100_500.write_record(record)
                if svlen >= 500 and svlen <= 1000:
                        vcf_writer_surv_HG_500_1000.write_record(record)
                if svlen >= 1000:
                        vcf_writer_surv_HG_1000.write_record(record)

for record in reference_del_reader:
        svlen = int(record.INFO['SVLEN'])
        if svlen >= 50 and svlen <= 100:
                        vcf_writer_ref_50_100.write_record(record)
        if svlen >= 100 and svlen <= 500:
                        vcf_writer_ref_100_500.write_record(record)
        if svlen >= 500 and svlen <= 1000:
                        vcf_writer_ref_500_1000.write_record(record)
        if svlen >= 1000:
                        vcf_writer_ref_1000.write_record(record)

for record in reference_HG_reader:
        svlen = int(record.INFO['SVLEN'])
        if svlen >= 50 and svlen <= 100:
                        vcf_writer_ref_HG_50_100.write_record(record)
        if svlen >= 100 and svlen <= 500:
                        vcf_writer_ref_HG_100_500.write_record(record)
        if svlen >= 500 and svlen <= 1000:
                        vcf_writer_ref_HG_500_1000.write_record(record)
        if svlen >= 1000:
                        vcf_writer_ref_HG_1000.write_record(record)

for record in parl_del_reader:
                svlen = int(record.INFO['SVLEN'])
                if svlen >= 50 and svlen <= 100:
                        vcf_writer_parl_50_100.write_record(record)
                if svlen >= 100 and svlen <= 500:
                        vcf_writer_parl_100_500.write_record(record)
                if svlen >= 500 and svlen <= 1000:
                        vcf_writer_parl_500_1000.write_record(record)
                if svlen >= 1000:
                        vcf_writer_parl_1000.write_record(record)

for record in deep_del_reader:
                svlen = int(record.INFO['SVLEN'])
                if svlen >= 50 and svlen <= 100:
                        vcf_writer_deep_50_100.write_record(record)
                if svlen >= 100 and svlen <= 500:
                        vcf_writer_deep_100_500.write_record(record)
                if svlen >= 500 and svlen <= 1000:
                        vcf_writer_deep_500_1000.write_record(record)
                if svlen >= 1000:
                        vcf_writer_deep_1000.write_record(record)

for record in parl_HG_reader:
                svlen = int(record.INFO['SVLEN'])
                if svlen >= 50 and svlen <= 100:
                        vcf_writer_parl_HG_50_100.write_record(record)
                if svlen >= 100 and svlen <= 500:
                        vcf_writer_parl_HG_100_500.write_record(record)
                if svlen >= 500 and svlen <= 1000:
                        vcf_writer_parl_HG_500_1000.write_record(record)
                if svlen >= 1000:
                        vcf_writer_parl_HG_1000.write_record(record)

                