import os
import sys
import allel
import pandas as pd
import numpy as np
from os import path

samples=['AKR_J','A_J','BALB_cJ','C3H_HeJ','CBA_J','DBA_2J','LP_J']
tools=['VISTA','breakdancer','delly',
'gridss',
'popdel',
'smoove',
'genomestrip',
'manta_diploidSV', 'surv', 'jasmine'
]
cov_list=['32','16','8','4','2','1','0.5']
th_list=['100']
n_list=['1','2','3','4','5','6','7','8','9','10']

df= pd.DataFrame(columns=['strain','length','flag','position','threshold'])
for s in samples:
    print ("---",s,"---")
    for t in tools:
        for th in th_list: 
            for cov in cov_list:
                for n in n_list:
            
                    file='/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_'+cov+'x/'+str(th)+'t/nf_'+str(th)+'t.'+t+'.'+s+'.chr19.'+cov+'p.'+n+'_sorted.modified.vcf'
            
                    if path.exists(file):
                        callset = allel.read_vcf(file,fields='*')
                        if callset!=None:
                            df_current = pd.DataFrame({'tool': t, 'strain': s, 'length': callset['variants/SVLEN'],'flag': callset['variants/FLAG'],'position': callset['variants/POS'],'threshold': th})
                            df_current['cov']=cov
                            df_current['n']=n
                            df = pd.concat([df_current, df],ignore_index=True) 
                            

df_nondel= pd.DataFrame(columns=['strain','length','flag','position','threshold'])


for s in samples:
    print ("---",s,"---")
    for t in tools:
        for th in th_list: 
            for cov in cov_list:
                for n in n_list:
            
            
                    file='/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_'+cov+'x/'+str(th)+'t/nf_'+str(th)+'t.'+t+'.'+s+'.chr19.'+cov+'p.'+n+'_sorted.modified.nondel.vcf'
            
                    if path.exists(file):
                        callset = allel.read_vcf(file,fields='*')
                        if callset!=None:
                            df_current = pd.DataFrame({'tool': t, 'strain': s, 'length': callset['variants/SVLEN'],'flag': callset['variants/FLAG'],'position': callset['variants/POS'],'threshold': th})
                            df_current['cov']=cov
                            df_current['n']=n
                            df_nondel = pd.concat([df_current, df_nondel],ignore_index=True)   
                    else:
                        print (file)
group_data_TP=df[df['flag'] == 'TP'].groupby(['tool','threshold','strain','n','cov'],as_index=False)['flag'].count()
group_data_TP=group_data_TP.rename(columns={"flag": "nTP"})
group_data_TP.to_csv('TP_test.csv')

group_data_TP[pd.isnull(group_data_TP).any(axis=1)]

group_data_FP=df[df['flag'] == 'FP'].groupby(['tool','threshold','strain','n','cov'],as_index=False)['flag'].count()
group_data_FP=group_data_FP.rename(columns={"flag": "nFP"})
group_data_FP.tail()


group_data_FP[pd.isnull(group_data_FP).any(axis=1)]

group_data_TN=df_nondel[df_nondel['flag'] == 'TN'].groupby(['tool','threshold','strain','n','cov'],as_index=False)['flag'].count()
group_data_TN=group_data_TN.rename(columns={"flag": "nTN"})


group_data_TN[pd.isnull(group_data_TN).any(axis=1)]

for s in samples:
    for t in tools:
        for th in th_list:
            for cov in cov_list:
                for n in n_list:
                    if not (((group_data_TP['cov'] == cov) & (group_data_TP['n'] == n) & (group_data_TP['tool'] == t) & (group_data_TP['strain'] == s) & (group_data_TP['threshold'] == th)).any()):
                        group_data_TP = group_data_TP.append({'cov' : cov , 'n' : n , 'tool' : t , 'strain' : s,'threshold' : th,'nTP' : 0.0} , ignore_index=True)
group_data_TP[pd.isnull(group_data_TP).any(axis=1)]

#fill mssing combinations with 0s
for s in samples:
    for t in tools:
        for th in th_list:
            for cov in cov_list:
                for n in n_list:
                    if not (((group_data_FP['cov'] == cov) & (group_data_FP['n'] == n) & (group_data_FP['tool'] == t) & (group_data_FP['strain'] == s) & (group_data_FP['threshold'] == th)).any()):
                        group_data_FP = group_data_FP.append({'cov' : cov , 'n' : n , 'tool' : t , 'strain' : s,'threshold' : th,'nFP' : 0.0} , ignore_index=True)
group_data_FP[pd.isnull(group_data_FP).any(axis=1)]

#fill mssing combinations with 0s
for s in samples:
    for t in tools:
        for th in th_list:
            for cov in cov_list:
                for n in n_list:
                    if not (((group_data_TN['cov'] == cov) & (group_data_TN['n'] == n) & (group_data_TN['tool'] == t) & (group_data_TN['strain'] == s) & (group_data_TN['threshold'] == th)).any()):
                        group_data_TN = group_data_TN.append({'cov' : cov , 'n' : n , 'tool' : t , 'strain' : s,'threshold' : th,'nTN' : 0.0} , ignore_index=True)
group_data_TN[pd.isnull(group_data_TN).any(axis=1)]


group_data_TN.head()

#now both TP and FP are the size size and we can merge
df_merge=pd.merge(group_data_TP, group_data_FP,on=['tool','threshold','strain','n','cov'])
df_merge=pd.merge(df_merge, group_data_TN,on=['tool','threshold','strain','n','cov'])
df_merge[pd.isnull(df_merge).any(axis=1)]


#true SVs
df_current = pd.DataFrame(columns=['strain','length'])
df_true = pd.DataFrame(columns=['strain','length'])


for s in samples:
    file='/u/home/m/mdistler/benchmarking_SV/Data/gold_standard/mouse_vcf/'+s+'_reference.vcf'
    callset = allel.read_vcf(file,fields='*')
    
    df_current = pd.DataFrame({'strain': s, 'length': callset['variants/SVLEN']})
    df_true = pd.concat([df_current, df_true],ignore_index=True)
group_data_true = df_true.groupby(['strain'],as_index=False).count()
group_data_true=group_data_true.rename(columns={"length": "n_true"})
group_data_true

df_merge=pd.merge(df_merge, group_data_true)
df_merge.head()

df_merge.to_csv('Figure3_df_merge_compare_testforVISTA.csv')

# import os
# import sys
# import allel
# import pandas as pd
# import numpy as np
# from os import path

# range1 = sys.argv[1]
# # range2 = sys.argv[2]

# samples=['AKR_J','A_J','BALB_cJ','C3H_HeJ','CBA_J','DBA_2J','LP_J']
# tools=['breakdancer','delly',
# 'gridss',
# 'popdel',
# 'smoove',
# 'genomestrip',
# 'manta_diploidSV'
# ]

# cov_list=['32','16','8','4','2','1','0.5','0.1']
# th_list=['100']
# n_list=['1','2','3','4','5','6','7','8','9','10']

# df= pd.DataFrame(columns=['strain','length','flag','position','threshold'])
# for s in samples:
#     print ("---",s,"---")
#     for t in tools:
#         for th in th_list: 
#             for cov in cov_list:
#                 for n in n_list:
            
            
#                     file='/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_'+cov+'x/'+str(th)+'t/nf_'+str(th)+'t.'+t+'.'+s+'.chr19.'+cov+'p.'+n+'_sorted.modified.vcf'
            
#                     if path.exists(file):
#                         callset = allel.read_vcf(file,fields='*')
#                         if callset!=None:
#                             svlen = callset['variants/SVLEN']
#                             mask = (svlen >= int(range1))
                            
#                             df_current = pd.DataFrame({'tool': t, 'strain': s, 'length': svlen[mask], 'flag': callset['variants/FLAG'][mask], 'position': callset['variants/POS'][mask], 'threshold': th})
#                             df_current['cov'] = cov
#                             df_current['n'] = n
#                             df = pd.concat([df_current, df], ignore_index=True) 


# df_nondel= pd.DataFrame(columns=['strain','length','flag','position','threshold'])


# for s in samples:
#     print ("---",s,"---")
#     for t in tools:
#         for th in th_list: 
#             for cov in cov_list:
#                 for n in n_list:
            
            
#                     file='/u/home/m/mdistler/benchmarking_SV/Data/raw_data/mouse/custom_vcf_'+cov+'x/'+str(th)+'t/nf_'+str(th)+'t.'+t+'.'+s+'.chr19.'+cov+'p.'+n+'_sorted.modified.nondel.vcf'
            
#                     if path.exists(file):
#                         callset = allel.read_vcf(file,fields='*')
#                         if callset!=None:
#                             svlen = callset['variants/SVLEN']
#                             mask = (svlen >= int(range1))
#                             df_current = pd.DataFrame({'tool': t, 'strain': s, 'length': svlen[mask], 'flag': callset['variants/FLAG'][mask], 'position': callset['variants/POS'][mask], 'threshold': th})
#                             df_current['cov']=cov
#                             df_current['n']=n
#                             df_nondel = pd.concat([df_current, df_nondel],ignore_index=True)   
#                     else:
#                         print (file)
# group_data_TP=df[df['flag'] == 'TP'].groupby(['tool','threshold','strain','n','cov'],as_index=False)['flag'].count()
# group_data_TP=group_data_TP.rename(columns={"flag": "nTP"})


# group_data_TP[pd.isnull(group_data_TP).any(axis=1)]

# group_data_FP=df[df['flag'] == 'FP'].groupby(['tool','threshold','strain','n','cov'],as_index=False)['flag'].count()
# group_data_FP=group_data_FP.rename(columns={"flag": "nFP"})
# group_data_FP.tail()


# group_data_FP[pd.isnull(group_data_FP).any(axis=1)]

# group_data_TN=df_nondel[df_nondel['flag'] == 'TN'].groupby(['tool','threshold','strain','n','cov'],as_index=False)['flag'].count()
# group_data_TN=group_data_TN.rename(columns={"flag": "nTN"})


# group_data_TN[pd.isnull(group_data_TN).any(axis=1)]

# for s in samples:
#     for t in tools:
#         for th in th_list:
#             for cov in cov_list:
#                 for n in n_list:
#                     if not (((group_data_TP['cov'] == cov) & (group_data_TP['n'] == n) & (group_data_TP['tool'] == t) & (group_data_TP['strain'] == s) & (group_data_TP['threshold'] == th)).any()):
#                         group_data_TP = group_data_TP.append({'cov' : cov , 'n' : n , 'tool' : t , 'strain' : s,'threshold' : th,'nTP' : 0.0} , ignore_index=True)
# group_data_TP[pd.isnull(group_data_TP).any(axis=1)]

# #fill mssing combinations with 0s
# for s in samples:
#     for t in tools:
#         for th in th_list:
#             for cov in cov_list:
#                 for n in n_list:
#                     if not (((group_data_FP['cov'] == cov) & (group_data_FP['n'] == n) & (group_data_FP['tool'] == t) & (group_data_FP['strain'] == s) & (group_data_FP['threshold'] == th)).any()):
#                         group_data_FP = group_data_FP.append({'cov' : cov , 'n' : n , 'tool' : t , 'strain' : s,'threshold' : th,'nFP' : 0.0} , ignore_index=True)
# group_data_FP[pd.isnull(group_data_FP).any(axis=1)]

# #fill mssing combinations with 0s
# for s in samples:
#     for t in tools:
#         for th in th_list:
#             for cov in cov_list:
#                 for n in n_list:
#                     if not (((group_data_TN['cov'] == cov) & (group_data_TN['n'] == n) & (group_data_TN['tool'] == t) & (group_data_TN['strain'] == s) & (group_data_TN['threshold'] == th)).any()):
#                         group_data_TN = group_data_TN.append({'cov' : cov , 'n' : n , 'tool' : t , 'strain' : s,'threshold' : th,'nTN' : 0.0} , ignore_index=True)
# group_data_TN[pd.isnull(group_data_TN).any(axis=1)]


# group_data_TN.head()

# #now both TP and FP are the size size and we can merge
# df_merge=pd.merge(group_data_TP, group_data_FP,on=['tool','threshold','strain','n','cov'])
# df_merge=pd.merge(df_merge, group_data_TN,on=['tool','threshold','strain','n','cov'])
# df_merge[pd.isnull(df_merge).any(axis=1)]


# #true SVs
# df_current = pd.DataFrame(columns=['strain','length'])
# df_true = pd.DataFrame(columns=['strain','length'])


# for s in samples:
#     file='/u/home/m/mdistler/benchmarking_SV/Data/gold_standard/mouse_vcf/'+s+'_reference.vcf'
#     callset = allel.read_vcf(file,fields='*')
    
#     df_current = pd.DataFrame({'strain': s, 'length': callset['variants/SVLEN']})
#     df_true = pd.concat([df_current, df_true],ignore_index=True)
# group_data_true = df_true.groupby(['strain'],as_index=False).count()
# group_data_true=group_data_true.rename(columns={"length": "n_true"})
# group_data_true

# df_merge=pd.merge(df_merge, group_data_true)
# df_merge.head()

# csv_name = 'Figure3_df_merge_compare'+ range1+'.csv'
# df_merge.to_csv(csv_name)

