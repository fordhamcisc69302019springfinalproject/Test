from CISC6930_preprocessing import *
import pandas as np
import numpy as np
import matplotlib.pyplot as plt
from sklearn.grid_search import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
from sklearn.svm import SVC

def getData():
	columns = ['age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation',
	           'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country',
	           'label']
	df = load_data("data/census-income.data.csv", columns)
	df = get_dummy(df, False)
	X = df.drop(['label'], axis = 1)
	y = df['label']
	return X, y

def RandomForestTune():
	X, y = getData()
	rfc = RandomForestClassifier(n_jobs=-1,max_features= 'sqrt' ,n_estimators=50, oob_score = True) 

	param_grid = { 
	    'n_estimators': [200, 700],
	    'max_depth':[1:20],
	    'max_features': ['auto', 'sqrt', 'log2']
	}

	clf = GridSearchCV(estimator=rfc, param_grid=param_grid, cv= 5)
	clf.fit(X, y)
	# print(clf.best_params_)
	return clf.best_params_

	def LogisticRegressionTune():
	X, y = getData()
	pipe = Pipeline([('classifier' , RandomForestClassifier())])

	param_grid = [
	    {'classifier' : [LogisticRegression()],
	     'classifier__penalty' : ['l1', 'l2'],
	    'classifier__C' : np.logspace(-4, 4, 20),
	    'classifier__solver' : ['liblinear']},
	    {'classifier' : [RandomForestClassifier()],
	    'classifier__n_estimators' : list(range(10,101,10)),
	    'classifier__max_features' : list(range(6,32,5))}
	]
	clf = GridSearchCV(pipe, param_grid = param_grid, cv = 5, verbose=True, n_jobs=-1)
	clf.fit(X, y)
	# print(clf.best_params_)
	return clf.best_params_

def SVMTune():
	X, y = getData()
	X_train, X_test, y_train, y_test = train_test_split(
	    X, y, test_size=0.5, random_state=0)

	# Set the parameters by cross-validation
	tuned_parameters = [{'kernel': ['rbf'], 'gamma': [1e-3, 1e-4],
	                     'C': [1, 10, 100, 1000]},
	                    {'kernel': ['linear'], 'C': [1, 10, 100, 1000]}]

	scores = ['precision', 'recall']

	for score in scores:
	    print("# Tuning hyper-parameters for %s" % score)
	    print()

	    clf = GridSearchCV(SVC(), tuned_parameters, cv=5,
	                       scoring='%s_macro' % score)
	    clf.fit(X_train, y_train)

	    print("Best parameters set found on development set:\n")
	    print(clf.best_params_)
	    print("\nGrid scores on development set:\n")
	    means = clf.cv_results_['mean_test_score']
	    stds = clf.cv_results_['std_test_score']
	    for mean, std, params in zip(means, stds, clf.cv_results_['params']):
	        print("%0.3f (+/-%0.03f) for %r"
	              % (mean, std * 2, params))

	    print("\nDetailed classification report:\n")
	    print("The model is trained on the full development set.")
	    print("The scores are computed on the full evaluation set.\n")
	    y_true, y_pred = y_test, clf.predict(X_test)
	    print(classification_report(y_true, y_pred))
