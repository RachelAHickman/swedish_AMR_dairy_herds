#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#"""
#Created on Tue Jul 16 13:53:14 2019

#@author: rachi870
#"""

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

Swedish_farm_AMR_data = pd.read_excel (r'Swedish_farm_remodelled_all_data.xlsx') 
non_organic_farms_year_1 = pd.read_excel (r'Swedish_non_organic_farms_year_1_data.xlsx')
non_organic_farms_year_2 = pd.read_excel (r'Swedish_non_organic_farms_year_2_data.xlsx')
organic_farms_year_1 = pd.read_excel (r'Swedish_organic_farms_year_1_data.xlsx')
organic_farms_year_2 = pd.read_excel (r'Swedish_organic_farms_year_2_data.xlsx')


#To generate the average resistance value from all calf samples to each drug
##non_organic_farms_year_1
non_organic_farms_year_1_AMX = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'AMPICILLIN']
non_organic_farms_year_1_CTX = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'CEFOTAXIME']
non_organic_farms_year_1_CAZ = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'CEFTAZIDIME']
non_organic_farms_year_1_CHL = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'CHLORAMPHENICOL']
non_organic_farms_year_1_CIP = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'CIPROFLOXACIN'] 
non_organic_farms_year_1_CST = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'COLISTIN']
non_organic_farms_year_1_FLOR = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'FLORFENICOL']
non_organic_farms_year_1_GEN = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'GENTAMICIN']
non_organic_farms_year_1_NAL = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'NALIDIXIC_ACID']
non_organic_farms_year_1_STR = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'STREPTOMYCIN']
non_organic_farms_year_1_SXT = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'SULFAMETHOXAZOLE']
non_organic_farms_year_1_TET = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'TETRACYCLINE']
non_organic_farms_year_1_TMP = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'TRIMETHOPRIM']
non_organic_farms_year_1_MDR = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'multi_amr'] 
non_organic_farms_year_1_AMR = non_organic_farms_year_1.loc[non_organic_farms_year_1['Resistance_cat'] == 'amr']
#mean
mean_non_organic_farms_year_1_AMX = non_organic_farms_year_1_AMX.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_CTX = non_organic_farms_year_1_CTX.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_CAZ = non_organic_farms_year_1_CAZ.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_CHL = non_organic_farms_year_1_CHL.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_CIP = non_organic_farms_year_1_CIP.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_CST = non_organic_farms_year_1_CST.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_FLOR =non_organic_farms_year_1_FLOR.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_GEN = non_organic_farms_year_1_GEN.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_NAL = non_organic_farms_year_1_NAL.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_STR = non_organic_farms_year_1_STR.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_SXT = non_organic_farms_year_1_SXT.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_TET = non_organic_farms_year_1_TET.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_TMP = non_organic_farms_year_1_TMP.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_MDR = non_organic_farms_year_1_MDR.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_1_AMR = non_organic_farms_year_1_AMR.groupby('Heard_number').mean().reset_index()
#del['Calf_number']
del mean_non_organic_farms_year_1_AMX['Calf_number']
del mean_non_organic_farms_year_1_CTX ['Calf_number']
del mean_non_organic_farms_year_1_CAZ['Calf_number']
del mean_non_organic_farms_year_1_CHL['Calf_number']
del mean_non_organic_farms_year_1_CIP['Calf_number']
del mean_non_organic_farms_year_1_CST['Calf_number']
del mean_non_organic_farms_year_1_FLOR['Calf_number'] 
del mean_non_organic_farms_year_1_GEN['Calf_number']
del mean_non_organic_farms_year_1_NAL['Calf_number']
del mean_non_organic_farms_year_1_STR['Calf_number']
del mean_non_organic_farms_year_1_SXT['Calf_number']
del mean_non_organic_farms_year_1_TET['Calf_number']
del mean_non_organic_farms_year_1_TMP['Calf_number']
del mean_non_organic_farms_year_1_MDR['Calf_number']
del mean_non_organic_farms_year_1_AMR['Calf_number']
#add drug
mean_non_organic_farms_year_1_AMX['Drug'] = 'AMX'
mean_non_organic_farms_year_1_CTX ['Drug'] = 'CTX'
mean_non_organic_farms_year_1_CAZ['Drug'] = 'CAZ'
mean_non_organic_farms_year_1_CHL['Drug'] = 'CHL'
mean_non_organic_farms_year_1_CIP['Drug'] = 'CIP'
mean_non_organic_farms_year_1_CST['Drug'] = 'CST'
mean_non_organic_farms_year_1_FLOR['Drug'] = 'FLOR' 
mean_non_organic_farms_year_1_GEN['Drug'] = 'GEN'
mean_non_organic_farms_year_1_NAL['Drug'] = 'NAL'
mean_non_organic_farms_year_1_STR['Drug'] = 'STR'
mean_non_organic_farms_year_1_SXT['Drug'] = 'SXT'
mean_non_organic_farms_year_1_TET['Drug'] = 'TET'
mean_non_organic_farms_year_1_TMP['Drug'] = 'TMP'
mean_non_organic_farms_year_1_MDR['Resistance_cat'] = 'MDR'
mean_non_organic_farms_year_1_AMR['Resistance_cat']= 'AMR'
#concatimate tables
drug_mean_non_organic_farms_year_1 = pd.concat([mean_non_organic_farms_year_1_AMX, mean_non_organic_farms_year_1_CTX, mean_non_organic_farms_year_1_CAZ, mean_non_organic_farms_year_1_CHL, mean_non_organic_farms_year_1_CIP, mean_non_organic_farms_year_1_CST, mean_non_organic_farms_year_1_FLOR, 
mean_non_organic_farms_year_1_GEN, mean_non_organic_farms_year_1_NAL, mean_non_organic_farms_year_1_STR, mean_non_organic_farms_year_1_SXT, mean_non_organic_farms_year_1_TET, mean_non_organic_farms_year_1_TMP])
resistance_mean_non_organic_farms_year_1 = pd.concat([mean_non_organic_farms_year_1_AMR,mean_non_organic_farms_year_1_MDR])
#make a display inital heatmap
heatmap_drug_mean_non_organic_farms_year_1 = pd.pivot_table (drug_mean_non_organic_farms_year_1, index=['Heard_number'], columns=['Drug'], values=['Resistance_value'])
heatmap_resistance_mean_non_organic_farms_year_1 = pd.pivot_table (resistance_mean_non_organic_farms_year_1, index=['Heard_number'], columns=['Resistance_cat'], values=['Resistance_value'])
cmap = sns.color_palette("coolwarm", 6)
display_drug_heatmap_mean_non_organic_farms_year_1 = sns.heatmap(heatmap_drug_mean_non_organic_farms_year_1, cmap=cmap, vmin=0, vmax=1) 
display_resistance_heatmap_mean_non_organic_farms_year_1 = sns.heatmap(heatmap_resistance_mean_non_organic_farms_year_1, cmap=cmap, vmin=0, vmax=1) 

##non_organic_farms_year_2
non_organic_farms_year_2_AMX = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'AMPICILLIN']
non_organic_farms_year_2_CTX = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'CEFOTAXIME']
non_organic_farms_year_2_CAZ = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'CEFTAZIDIME']
non_organic_farms_year_2_CHL = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'CHLORAMPHENICOL']
non_organic_farms_year_2_CIP = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'CIPROFLOXACIN'] 
non_organic_farms_year_2_CST = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'COLISTIN']
non_organic_farms_year_2_FLOR = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'FLORFENICOL']
non_organic_farms_year_2_GEN = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'GENTAMICIN']
non_organic_farms_year_2_NAL = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'NALIDIXIC_ACID']
non_organic_farms_year_2_STR = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'STREPTOMYCIN']
non_organic_farms_year_2_SXT = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'SULFAMETHOXAZOLE']
non_organic_farms_year_2_TET = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'TETRACYCLINE']
non_organic_farms_year_2_TMP = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'TRIMETHOPRIM']
non_organic_farms_year_2_MDR = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'multi_amr'] 
non_organic_farms_year_2_AMR = non_organic_farms_year_2.loc[non_organic_farms_year_2['Resistance_cat'] == 'amr']
#mean
mean_non_organic_farms_year_2_AMX = non_organic_farms_year_2_AMX.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_CTX = non_organic_farms_year_2_CTX.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_CAZ = non_organic_farms_year_2_CAZ.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_CHL = non_organic_farms_year_2_CHL.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_CIP = non_organic_farms_year_2_CIP.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_CST = non_organic_farms_year_2_CST.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_FLOR =non_organic_farms_year_2_FLOR.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_GEN = non_organic_farms_year_2_GEN.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_NAL = non_organic_farms_year_2_NAL.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_STR = non_organic_farms_year_2_STR.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_SXT = non_organic_farms_year_2_SXT.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_TET = non_organic_farms_year_2_TET.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_TMP = non_organic_farms_year_2_TMP.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_MDR = non_organic_farms_year_2_MDR.groupby('Heard_number').mean().reset_index()
mean_non_organic_farms_year_2_AMR = non_organic_farms_year_2_AMR.groupby('Heard_number').mean().reset_index()
#del['Calf_number']
del mean_non_organic_farms_year_2_AMX['Calf_number']
del mean_non_organic_farms_year_2_CTX ['Calf_number']
del mean_non_organic_farms_year_2_CAZ['Calf_number']
del mean_non_organic_farms_year_2_CHL['Calf_number']
del mean_non_organic_farms_year_2_CIP['Calf_number']
del mean_non_organic_farms_year_2_CST['Calf_number']
del mean_non_organic_farms_year_2_FLOR['Calf_number'] 
del mean_non_organic_farms_year_2_GEN['Calf_number']
del mean_non_organic_farms_year_2_NAL['Calf_number']
del mean_non_organic_farms_year_2_STR['Calf_number']
del mean_non_organic_farms_year_2_SXT['Calf_number']
del mean_non_organic_farms_year_2_TET['Calf_number']
del mean_non_organic_farms_year_2_TMP['Calf_number']
del mean_non_organic_farms_year_2_MDR['Calf_number']
del mean_non_organic_farms_year_2_AMR['Calf_number']
#add drug
mean_non_organic_farms_year_2_AMX['Drug'] = 'AMX'
mean_non_organic_farms_year_2_CTX ['Drug'] = 'CTX'
mean_non_organic_farms_year_2_CAZ['Drug'] = 'CAZ'
mean_non_organic_farms_year_2_CHL['Drug'] = 'CHL'
mean_non_organic_farms_year_2_CIP['Drug'] = 'CIP'
mean_non_organic_farms_year_2_CST['Drug'] = 'CST'
mean_non_organic_farms_year_2_FLOR['Drug'] = 'FLOR' 
mean_non_organic_farms_year_2_GEN['Drug'] = 'GEN'
mean_non_organic_farms_year_2_NAL['Drug'] = 'NAL'
mean_non_organic_farms_year_2_STR['Drug'] = 'STR'
mean_non_organic_farms_year_2_SXT['Drug'] = 'SXT'
mean_non_organic_farms_year_2_TET['Drug'] = 'TET'
mean_non_organic_farms_year_2_TMP['Drug'] = 'TMP'
mean_non_organic_farms_year_2_MDR['Resistance_cat'] = 'MDR'
mean_non_organic_farms_year_2_AMR['Resistance_cat']= 'AMR'
#concatimate tables
drug_mean_non_organic_farms_year_2 = pd.concat([mean_non_organic_farms_year_2_AMX, mean_non_organic_farms_year_2_CTX, mean_non_organic_farms_year_2_CAZ, mean_non_organic_farms_year_2_CHL, mean_non_organic_farms_year_2_CIP, mean_non_organic_farms_year_2_CST, mean_non_organic_farms_year_2_FLOR, 
mean_non_organic_farms_year_2_GEN, mean_non_organic_farms_year_2_NAL, mean_non_organic_farms_year_2_STR, mean_non_organic_farms_year_2_SXT, mean_non_organic_farms_year_2_TET, mean_non_organic_farms_year_2_TMP])
resistance_mean_non_organic_farms_year_2 = pd.concat([mean_non_organic_farms_year_2_AMR,mean_non_organic_farms_year_2_MDR])
#make a display inital heatmap
heatmap_drug_mean_non_organic_farms_year_2 = pd.pivot_table (drug_mean_non_organic_farms_year_2, index=['Heard_number'], columns=['Drug'], values=['Resistance_value'])
heatmap_resistance_mean_non_organic_farms_year_2 = pd.pivot_table (resistance_mean_non_organic_farms_year_2, index=['Heard_number'], columns=['Resistance_cat'], values=['Resistance_value'])
cmap = sns.color_palette("coolwarm", 10)
display_drug_heatmap_mean_non_organic_farms_year_2 = sns.heatmap(heatmap_drug_mean_non_organic_farms_year_2, cmap=cmap, vmin=0, vmax=1) 
display_resistance_heatmap_mean_non_organic_farms_year_2 = sns.heatmap(heatmap_resistance_mean_non_organic_farms_year_2, cmap=cmap, vmin=0, vmax=1) 

##organic_farms_year_1
organic_farms_year_1_AMX = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'AMPICILLIN']
organic_farms_year_1_CTX = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'CEFOTAXIME']
organic_farms_year_1_CAZ = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'CEFTAZIDIME']
organic_farms_year_1_CHL = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'CHLORAMPHENICOL']
organic_farms_year_1_CIP = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'CIPROFLOXACIN'] 
organic_farms_year_1_CST = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'COLISTIN']
organic_farms_year_1_FLOR = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'FLORFENICOL']
organic_farms_year_1_GEN = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'GENTAMICIN']
organic_farms_year_1_NAL = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'NALIDIXIC_ACID']
organic_farms_year_1_STR = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'STREPTOMYCIN']
organic_farms_year_1_SXT = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'SULFAMETHOXAZOLE']
organic_farms_year_1_TET = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'TETRACYCLINE']
organic_farms_year_1_TMP = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'TRIMETHOPRIM']
organic_farms_year_1_MDR = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'multi_amr'] 
organic_farms_year_1_AMR = organic_farms_year_1.loc[organic_farms_year_1['Resistance_cat'] == 'amr']
#mean
mean_organic_farms_year_1_AMX = organic_farms_year_1_AMX.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_CTX = organic_farms_year_1_CTX.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_CAZ = organic_farms_year_1_CAZ.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_CHL = organic_farms_year_1_CHL.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_CIP = organic_farms_year_1_CIP.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_CST = organic_farms_year_1_CST.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_FLOR =organic_farms_year_1_FLOR.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_GEN = organic_farms_year_1_GEN.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_NAL = organic_farms_year_1_NAL.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_STR = organic_farms_year_1_STR.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_SXT = organic_farms_year_1_SXT.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_TET = organic_farms_year_1_TET.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_TMP = organic_farms_year_1_TMP.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_MDR = organic_farms_year_1_MDR.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_1_AMR = organic_farms_year_1_AMR.groupby('Heard_number').mean().reset_index()
#del['Calf_number']
del mean_organic_farms_year_1_AMX['Calf_number']
del mean_organic_farms_year_1_CTX ['Calf_number']
del mean_organic_farms_year_1_CAZ['Calf_number']
del mean_organic_farms_year_1_CHL['Calf_number']
del mean_organic_farms_year_1_CIP['Calf_number']
del mean_organic_farms_year_1_CST['Calf_number']
del mean_organic_farms_year_1_FLOR['Calf_number'] 
del mean_organic_farms_year_1_GEN['Calf_number']
del mean_organic_farms_year_1_NAL['Calf_number']
del mean_organic_farms_year_1_STR['Calf_number']
del mean_organic_farms_year_1_SXT['Calf_number']
del mean_organic_farms_year_1_TET['Calf_number']
del mean_organic_farms_year_1_TMP['Calf_number']
del mean_organic_farms_year_1_MDR['Calf_number']
del mean_organic_farms_year_1_AMR['Calf_number']
#add drug
mean_organic_farms_year_1_AMX['Drug'] = 'AMX'
mean_organic_farms_year_1_CTX ['Drug'] = 'CTX'
mean_organic_farms_year_1_CAZ['Drug'] = 'CAZ'
mean_organic_farms_year_1_CHL['Drug'] = 'CHL'
mean_organic_farms_year_1_CIP['Drug'] = 'CIP'
mean_organic_farms_year_1_CST['Drug'] = 'CST'
mean_organic_farms_year_1_FLOR['Drug'] = 'FLOR' 
mean_organic_farms_year_1_GEN['Drug'] = 'GEN'
mean_organic_farms_year_1_NAL['Drug'] = 'NAL'
mean_organic_farms_year_1_STR['Drug'] = 'STR'
mean_organic_farms_year_1_SXT['Drug'] = 'SXT'
mean_organic_farms_year_1_TET['Drug'] = 'TET'
mean_organic_farms_year_1_TMP['Drug'] = 'TMP'
mean_organic_farms_year_1_MDR['Resistance_cat'] = 'MDR'
mean_organic_farms_year_1_AMR['Resistance_cat']= 'AMR'
#concatimate tables
drug_mean_organic_farms_year_1 = pd.concat([mean_organic_farms_year_1_AMX, mean_organic_farms_year_1_CTX, mean_organic_farms_year_1_CAZ, mean_organic_farms_year_1_CHL, mean_organic_farms_year_1_CIP, mean_organic_farms_year_1_CST, mean_organic_farms_year_1_FLOR, 
mean_organic_farms_year_1_GEN, mean_organic_farms_year_1_NAL, mean_organic_farms_year_1_STR, mean_organic_farms_year_1_SXT, mean_organic_farms_year_1_TET, mean_organic_farms_year_1_TMP])
resistance_mean_organic_farms_year_1 = pd.concat([mean_organic_farms_year_1_AMR,mean_organic_farms_year_1_MDR])
#make a display inital heatmap
heatmap_drug_mean_organic_farms_year_1 = pd.pivot_table (drug_mean_organic_farms_year_1, index=['Heard_number'], columns=['Drug'], values=['Resistance_value'])
heatmap_resistance_mean_organic_farms_year_1 = pd.pivot_table (resistance_mean_organic_farms_year_1, index=['Heard_number'], columns=['Resistance_cat'], values=['Resistance_value'])
cmap = sns.color_palette("coolwarm", 8)
display_drug_heatmap_mean_organic_farms_year_1 = sns.heatmap(heatmap_drug_mean_organic_farms_year_1, cmap=cmap, vmin=0, vmax=1) 
display_resistance_heatmap_mean_organic_farms_year_1 = sns.heatmap(heatmap_resistance_mean_organic_farms_year_1, cmap=cmap, vmin=0, vmax=1) 

##organic_farms_year_2
organic_farms_year_2_AMX = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'AMPICILLIN']
organic_farms_year_2_CTX = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'CEFOTAXIME']
organic_farms_year_2_CAZ = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'CEFTAZIDIME']
organic_farms_year_2_CHL = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'CHLORAMPHENICOL']
organic_farms_year_2_CIP = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'CIPROFLOXACIN'] 
organic_farms_year_2_CST = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'COLISTIN']
organic_farms_year_2_FLOR = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'FLORFENICOL']
organic_farms_year_2_GEN = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'GENTAMICIN']
organic_farms_year_2_NAL = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'NALIDIXIC_ACID']
organic_farms_year_2_STR = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'STREPTOMYCIN']
organic_farms_year_2_SXT = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'SULFAMETHOXAZOLE']
organic_farms_year_2_TET = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'TETRACYCLINE']
organic_farms_year_2_TMP = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'TRIMETHOPRIM']
organic_farms_year_2_MDR = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'multi_amr'] 
organic_farms_year_2_AMR = organic_farms_year_2.loc[organic_farms_year_2['Resistance_cat'] == 'amr']
#mean
mean_organic_farms_year_2_AMX = organic_farms_year_2_AMX.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_CTX = organic_farms_year_2_CTX.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_CAZ = organic_farms_year_2_CAZ.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_CHL = organic_farms_year_2_CHL.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_CIP = organic_farms_year_2_CIP.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_CST = organic_farms_year_2_CST.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_FLOR =organic_farms_year_2_FLOR.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_GEN = organic_farms_year_2_GEN.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_NAL = organic_farms_year_2_NAL.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_STR = organic_farms_year_2_STR.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_SXT = organic_farms_year_2_SXT.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_TET = organic_farms_year_2_TET.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_TMP = organic_farms_year_2_TMP.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_MDR = organic_farms_year_2_MDR.groupby('Heard_number').mean().reset_index()
mean_organic_farms_year_2_AMR = organic_farms_year_2_AMR.groupby('Heard_number').mean().reset_index()
#del['Calf_number']
del mean_organic_farms_year_2_AMX['Calf_number']
del mean_organic_farms_year_2_CTX ['Calf_number']
del mean_organic_farms_year_2_CAZ['Calf_number']
del mean_organic_farms_year_2_CHL['Calf_number']
del mean_organic_farms_year_2_CIP['Calf_number']
del mean_organic_farms_year_2_CST['Calf_number']
del mean_organic_farms_year_2_FLOR['Calf_number'] 
del mean_organic_farms_year_2_GEN['Calf_number']
del mean_organic_farms_year_2_NAL['Calf_number']
del mean_organic_farms_year_2_STR['Calf_number']
del mean_organic_farms_year_2_SXT['Calf_number']
del mean_organic_farms_year_2_TET['Calf_number']
del mean_organic_farms_year_2_TMP['Calf_number']
del mean_organic_farms_year_2_MDR['Calf_number']
del mean_organic_farms_year_2_AMR['Calf_number']
#add drug
mean_organic_farms_year_2_AMX['Drug'] = 'AMX'
mean_organic_farms_year_2_CTX ['Drug'] = 'CTX'
mean_organic_farms_year_2_CAZ['Drug'] = 'CAZ'
mean_organic_farms_year_2_CHL['Drug'] = 'CHL'
mean_organic_farms_year_2_CIP['Drug'] = 'CIP'
mean_organic_farms_year_2_CST['Drug'] = 'CST'
mean_organic_farms_year_2_FLOR['Drug'] = 'FLOR' 
mean_organic_farms_year_2_GEN['Drug'] = 'GEN'
mean_organic_farms_year_2_NAL['Drug'] = 'NAL'
mean_organic_farms_year_2_STR['Drug'] = 'STR'
mean_organic_farms_year_2_SXT['Drug'] = 'SXT'
mean_organic_farms_year_2_TET['Drug'] = 'TET'
mean_organic_farms_year_2_TMP['Drug'] = 'TMP'
mean_organic_farms_year_2_MDR['Resistance_cat'] = 'MDR'
mean_organic_farms_year_2_AMR['Resistance_cat']= 'AMR'
#concatinate tables
drug_mean_organic_farms_year_2 = pd.concat([mean_organic_farms_year_2_AMX, mean_organic_farms_year_2_CTX, mean_organic_farms_year_2_CAZ, mean_organic_farms_year_2_CHL, mean_organic_farms_year_2_CIP, mean_organic_farms_year_2_CST, mean_organic_farms_year_2_FLOR, 
mean_organic_farms_year_2_GEN, mean_organic_farms_year_2_NAL, mean_organic_farms_year_2_STR, mean_organic_farms_year_2_SXT, mean_organic_farms_year_2_TET, mean_organic_farms_year_2_TMP])
resistance_mean_organic_farms_year_2 = pd.concat([mean_organic_farms_year_2_AMR,mean_organic_farms_year_2_MDR])
#make a display inital heatmap
heatmap_drug_mean_organic_farms_year_2 = pd.pivot_table (drug_mean_organic_farms_year_2, index=['Heard_number'], columns=['Drug'], values=['Resistance_value'])
heatmap_resistance_mean_organic_farms_year_2 = pd.pivot_table (resistance_mean_organic_farms_year_2, index=['Heard_number'], columns=['Resistance_cat'], values=['Resistance_value'])
cmap = sns.color_palette("coolwarm", 7)
display_drug_heatmap_mean_organic_farms_year_2 = sns.heatmap(heatmap_drug_mean_organic_farms_year_2, cmap=cmap, vmin=0, vmax=1) 
display_resistance_heatmap_mean_organic_farms_year_2 = sns.heatmap(heatmap_resistance_mean_organic_farms_year_2, cmap=cmap, vmin=0, vmax=1) 

##FIGURE A - To generate on heatmap figure with all drug info with non organic on top and organic underneath
fig = plt.figure(figsize = (30,60)) # width x height
ax1 = fig.add_subplot(2, 2, 1) # row, column, position
ax2 = fig.add_subplot(2, 2, 2)
ax3 = fig.add_subplot(2, 2, 3)
ax4 = fig.add_subplot(2, 2, 4)
sns.heatmap(data=heatmap_drug_mean_non_organic_farms_year_1, ax=ax1, cmap = cmap, cbar_kws={'shrink': .3})
ax1.set_title('Conventional Farms - Year 1',fontsize=14)
ax1.set_xlabel('Anitmicrobial Drug')
ax1.set_ylabel('Heard number', fontsize=12)
ax1.set_xticklabels(['ÁMX', 'CAZ', 'CHL', 'CIP','CST','CTX','FLOR', 'GEN', 'NAL', 'STR', 'SXT', 'TET', 'TMP'],
                   rotation=0, fontsize=10)
ax1.set_yticklabels(['1', '2', '3', '5', '10', '12', '14', '15', '16', '17', '20', '21', '23', '26', '28', '29', '33', '34', '40', '41', '42', 
                     '43', '45', '47', '48', '49', '53', '54', '58', '59'],rotation=0, fontsize=10)
sns.heatmap(data=heatmap_drug_mean_non_organic_farms_year_2, ax=ax2, cmap = cmap, cbar_kws={'shrink': .3}) 
ax2.set_title('Conventional Farms - Year 2',fontsize=14)
ax2.set_xlabel('Anitmicrobial Drug', fontsize=12)
ax2.set_ylabel('Heard number', fontsize=12)
ax2.set_xticklabels(['ÁMX', 'CAZ', 'CHL', 'CIP','CST','CTX','FLOR', 'GEN', 'NAL', 'STR', 'SXT', 'TET', 'TMP'],
                   rotation=0, fontsize=10)
ax2.set_yticklabels(['1', '2','5', '10', '12', '14', '15', '16', '17', '20', '21', '23', '26', '29', '33', '34', '41', '42', 
                     '43', '45', '47', '48', '49', '53', '54', '58', '59'],rotation=0, fontsize=10)
sns.heatmap(heatmap_drug_mean_organic_farms_year_1, ax=ax3, cmap = cmap, cbar_kws={'shrink': .3})
ax3.set_title('Organic Farms - Year 1',fontsize=14)
ax3.set_xlabel('Anitmicrobial Drug', fontsize=12)
ax3.set_ylabel('Heard number', fontsize=12)
ax3.set_xticklabels(['ÁMX', 'CAZ', 'CHL', 'CIP','CST','CTX','FLOR', 'GEN', 'NAL', 'STR', 'SXT', 'TET', 'TMP'],
                   rotation=0, fontsize=10)
ax3.set_yticklabels(['4', '6', '7', '8', '9', '11', '13', '18', '19', '22', '24', '25', '27', '30', '31', '32', '35', '36', '37', '38', '39', 
                     '44', '46', '50', '51', '52', '55', '56', '57', '60'],rotation=0, fontsize=10)
sns.heatmap(heatmap_drug_mean_organic_farms_year_2, ax=ax4, cmap = cmap, cbar_kws={'shrink': .3})
ax4.set_title('Organic Farms - Year 2',fontsize=14)
ax4.set_xlabel('Anitmicrobial Drug', fontsize=12)
ax4.set_ylabel('Heard number', fontsize=12)
ax4.set_xticklabels(['ÁMX', 'CAZ', 'CHL', 'CIP','CST','CTX','FLOR', 'GEN', 'NAL', 'STR', 'SXT', 'TET', 'TMP'],
                   rotation=0, fontsize=10)
ax4.set_yticklabels(['4', '6', '8', '9', '11', '18', '19', '22', '24', '25', '27', '30',  '32', '35', '36', '37', '38', '39', 
                     '44', '46', '50', '51', '52', '55', '56', '57', '60'],rotation=0, fontsize=10)
plt.savefig('Swedish_farm_drug_mean_heatmap', dpi=400)

##FIGURE B - To generate on two clustermap figures with all MDR info for organic and non organic farms
MDR_non_organic_data = pd.read_excel (r'/Users/rachi870/Desktop/Non_organic_MDR_data.xlsx')
MDR_non_organic_data = MDR_non_organic_data.pivot('Heard number', 'Year', 'MDR_Farm_Resistance_value')
MDR_non_organic_data = MDR_non_organic_data.drop([3, 28,40])
cmap = sns.color_palette("coolwarm", 6)
cluster_non_organic = sns.clustermap(MDR_non_organic_data,cmap =cmap)
plt.title('                                                                                                                                           Conventional Farms',fontsize=15)
plt.xlabel('Mean Farm MDR Resistance Value', fontsize=9)
plt.savefig('Swedish_Farm_non_organic_clustermap.png', dpi=400, bbox_inches = 'tight')
MDR_organic_data = pd.read_excel (r'/Users/rachi870/Desktop/Organic_MDR_data.xlsx')
MDR_organic_data = MDR_organic_data.pivot('Heard number', 'Year', 'MDR_Farm_Resistance_value')
MDR_organic_data = MDR_organic_data.drop([4,7,13,31])
cluster_organic = sns.clustermap(MDR_organic_data,cmap =cmap)
plt.title('                                                                                                                                           Organic Farms',fontsize=15)
plt.xlabel('Mean Farm MDR Resistance Value', fontsize=9)
plt.savefig('Swedish_Farm_organic_clustermap.png', dpi=400,bbox_inches = 'tight')

#Statistical tabels for analysis in prism
stat1_drug_mean_non_organic_farms_year1 = drug_mean_non_organic_farms_year_1.groupby('Drug').mean().reset_index()
stat2_drug_mean_non_organic_farms_year1 = drug_mean_non_organic_farms_year_1.groupby('Drug').std().reset_index()
stat1_drug_mean_non_organic_farms_year2 = drug_mean_non_organic_farms_year_2.groupby('Drug').mean().reset_index()
stat2_drug_mean_non_organic_farms_year2 = drug_mean_non_organic_farms_year_2.groupby('Drug').std().reset_index()
stat1_drug_mean_organic_farms_year1 = drug_mean_organic_farms_year_1.groupby('Drug').mean().reset_index()
stat2_drug_mean_organic_farms_year1 = drug_mean_organic_farms_year_1.groupby('Drug').std().reset_index()
stat1_drug_mean_organic_farms_year2 = drug_mean_organic_farms_year_2.groupby('Drug').mean().reset_index()
stat2_drug_mean_organic_farms_year2 = drug_mean_organic_farms_year_2.groupby('Drug').std().reset_index()
