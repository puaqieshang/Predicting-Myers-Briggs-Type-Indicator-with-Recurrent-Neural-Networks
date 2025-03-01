#!/usr/bin/env python

import random
import collections
import numpy as np
import pandas as pd
import csv


raw_data_path = "/content/gdrive/MyDrive/AI Startup/Models/Myer-Briggs/mbti_1.csv" # Change this
df = pd.read_csv(raw_data_path)

types = ('ISTJ', 'ISFJ', 'INFJ', 'INTJ', \
		 'ISTP', 'ISFP', 'INFP', 'INTP', \
		 'ESTP', 'ESFP', 'ENFP', 'ENTP', \
		 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ')

gen_pop = {'ISTJ': 0.11, 'ISFJ': 0.09, 'INFJ': 0.04, 'INTJ': 0.05, \
		   'ISTP': 0.05, 'ISFP': 0.05, 'INFP': 0.06, 'INTP': 0.06, \
		   'ESTP': 0.04, 'ESFP': 0.04, 'ENFP': 0.08, 'ENTP': 0.06, \
		   'ESTJ': 0.08, 'ESFJ': 0.09, 'ENFJ': 0.05, 'ENTJ': 0.05}

n, ___ = df.shape

counts = collections.defaultdict(int)
for mbti in df['type']:
	counts[mbti] += 1

limiting_type = None
min_size = float('infinity')
for mbti in counts.keys():
	size = counts[mbti]/gen_pop[mbti]
	if size < min_size:
		min_size = size
		limiting_type = mbti

dic = collections.defaultdict(list)
for row in df.iterrows():
	dic[row[1]['type']].append(row)

unclean_list = []

with open('mbti_clean.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['type', 'posts'])
	
	for mbti in gen_pop.keys():
		list1 = dic[mbti]
		for x in range(0, int(round(min_size*gen_pop[mbti]))):
			writer.writerow(list1[x][1])	
		unclean_list.append(list1[int(round(min_size*gen_pop[mbti])) : len(list1)])
					
with open('mbti_unclean.csv', 'w') as f:
	writer = csv.writer(f)
	writer.writerow(['type', 'posts'])
	for mbti in unclean_list:
		for x in mbti:
			writer.writerow(x[1])
