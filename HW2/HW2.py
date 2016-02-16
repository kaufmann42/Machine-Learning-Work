#import statements
from sklearn import svm
import numpy as np
import pandas as pd
import cm

#import the database
raw_data = pd.read_csv('data.csv')

training_data = raw_data.ix[0:300,:-1]
target = raw_data.ix[0:300,-1]

clf = svm.SVC()
clf.fit(training_data, target)

predicting_data = raw_data.ix[301:400,:-1]
predicting_target = raw_data.ix[301:400,-1]

cm.print_ConfusionMatrix(clf.predict(predicting_data), predicting_target, "SVM")
