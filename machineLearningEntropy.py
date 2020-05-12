#######################################
#######################################
# -*- coding: utf-8 -*-

#######################################
#######################################

import pandas as pd
import warnings
import numpy as np
import argparse
import sys
warnings.filterwarnings("ignore")
from catboost import *
from sklearn.model_selection import cross_val_predict
from catboost import CatBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_validate
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.linear_model import SGDClassifier
from sklearn import tree
from sklearn import svm
from sklearn.linear_model import SGDClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler 
from sklearn.preprocessing import Normalizer
from sklearn.linear_model import Perceptron
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier
from sklearn import metrics
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedShuffleSplit
from sklearn.model_selection import GridSearchCV
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import matthews_corrcoef
from sklearn import preprocessing
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import StratifiedKFold


def header(foutput):
	file = open(foutput, 'a')
	file.write("Classifier,ACC,std_ACC,SE,std_SE,F1,std_F1,AUC,std_AUC")
	file.write("\n")
	return
	
	
def save_measures(classifier, foutput, scores):
	file = open(foutput, 'a')
	file.write("%s,%0.4f,%0.2f,%0.4f,%0.2f,%0.4f,%0.2f,%0.4f,%0.2f" % (classifier, scores['test_accuracy'].mean(), 
	+ scores['test_accuracy'].std(), scores['test_recall'].mean(), scores['test_recall'].std(), 
	+ scores['test_f1'].mean(), scores['test_f1'].std(), 
	+ scores['test_roc_auc'].mean(), scores['test_roc_auc'].std()))
	file.write("\n")
	return


def evaluate_model_cross(classifier, model, finput):
  df = pd.read_csv(finput)	
  x = df[df.columns[1:(len(df.columns) - 1)]]
  y = df['label']
  sc = MinMaxScaler(feature_range=(0, 1))
  # sc = StandardScaler()
  X = sc.fit_transform(x)
  clf = model
  scoring = ['accuracy', 'recall', 'f1', 'roc_auc']
  scores = cross_validate(clf, X, y, cv = 10, scoring = scoring)
  # y_pred = cross_val_predict(clf, x, y, cv=10)
  # conf_mat = confusion_matrix(y, y_pred)
  # print(conf_mat)
  save_measures(classifier, foutput, scores)
  return


if __name__ == "__main__":
	print("\n")
	print("###################################################################################")
	print("#####################     Arguments: -i input -o output     #######################")
	print("##########               Author: Robson Parmezan Bonidia                ###########")
	print("###################################################################################")
	print("\n")
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--input', help='csv format file, E.g., dataset.csv')
	parser.add_argument('-o', '--output', help='CSV format file, E.g., test.csv')
	args = parser.parse_args()
	finput = str(args.input)
	foutput = str(args.output)
	experiments = { 
		"GaussianNB" : GaussianNB(),
		"GradientBoosting" : GradientBoostingClassifier(n_estimators=400, learning_rate=3.0, max_depth=1, random_state=63),
		"RandomForest" : RandomForestClassifier(random_state=63, n_estimators=100),
		# "LinearRegression" : LinearRegression(),
		# "SVM" : svm.SVC(gamma = 'scale', kernel = 'poly', degree = 5, coef0 = 0.1, random_state = 63),
		"Bagging" : BaggingClassifier(random_state = 63),
		"Adaboost" : AdaBoostClassifier(random_state = 63),
		"MLP" : MLPClassifier(solver='lbfgs', alpha=1e-5, hidden_layer_sizes=(100, 2), learning_rate_init=0.001, random_state=63),
		"Catboost" : CatBoostClassifier(iterations=100, random_seed=63, logging_level = 'Silent')
		}
	header(foutput)
	for classifier, model in experiments.items():
		print(classifier)
		# print(model)
		evaluate_model_cross(classifier, model, finput)