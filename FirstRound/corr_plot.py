#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 14:25:30 2019

@author: Magnus Xu
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

def load_dataset(dataset_path):
	df = pd.read_csv()
	df.columns = columns = ['age','workclass','fnlwgt','education','education_num',
	    'marital_status','occupation','relationship','race',
	    'sex','capital_gain','capital_loss','hours_per_week','native_country','label']
	return df

def encoder(df):
	'''
		Before we use OneHotEncoder, we need to transform the 
		original data from string into numeric types for the 
		reason that OneHotEncoder only accepts numeric 
		objects.
	'''
	le = LabelEncoder()
	encode_label = le.transform(df[['workclass','education','marital_status','occupation','relationship','race','sex','native_country']])
	ohe = OneHotEncoder(sparse = False).fit(label.reshape(-1, 1))
	df[['workclass','education','marital_status','occupation','relationship','race','sex','native_country']] = ohe.fit_transform(encode_label, reshape(-1, 1))
	return df

def corr_plot(df):
	plt.figure(figsize = (16, 12))
	cor = df.corr()
	sns.heatmap(cor, annot = True, cmap = plt.cm.Reds) 
	plt.show()

if __name__ == "__main__":
	file_path = 'Data/census-income.csv'
	df = load_dataset(file_path)
	df = encoder(df)
	corr_plot(df)
