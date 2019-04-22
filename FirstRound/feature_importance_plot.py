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
import statsmodels.api as sm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFE
from sklearn.linear_model import RidgeCV, LassoCV, Ridge, Lasso

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

def evaluator(df):
	X = df.drop(['label'], axis = 1)
	y = df['label']
	# Build a forest and compute the feature importances
	forest = ExtraTreesClassifier(n_estimators=250,random_state=0)

	forest.fit(X, y)
	importances = forest.feature_importances_
	std = np.std([tree.feature_importances_ for tree in forest.estimators_],
	             axis=0)
	indices = np.argsort(importances)[::-1]
	return X, y, indices

def feature_importance_plot(X, y, indices):
	# Print the feature ranking
	print("Feature ranking:")

	for f in range(X.shape[1]):
	    print("%d. feature %d (%f)" % (f + 1, indices[f], importances[indices[f]]))

	# Plot the feature importances of the forest
	plt.figure()
	plt.title("Feature importances")
	plt.bar(range(X.shape[1]), importances[indices],
	       color="r", yerr=std[indices], align="center")
	plt.xticks(range(X.shape[1]), indices)
	plt.xlim([-1, X.shape[1]])
	plt.show()

if __name__ == "__main__":
	file_path = 'Data/census-income.csv'
	df = load_dataset(file_path)
	df = encoder(df)
	X, y, indices = evaluator(df)
	feature_importance_plot(X, y, indices)
