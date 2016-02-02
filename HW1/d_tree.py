from sklearn import tree
import pandas as pd

mydata = pd.read_csv('data.csv')
target = mydata["att1"]  #provided your csv has header row, and the label column is named "Label"

#select all but the last column as data
data = mydata.ix[:,:-1]

clf = tree.DecisionTreeClassifier()
clf = clf.fit(data, target)

predicted = clf.predict(data)
actual = mydata.ix[:,22:].values
total = actual.shape[0]

one = 0
two = 0
three = 0
four = 0

for i in range(0,total):
    if predicted[i] == 0 and actual[i] == 0:
        one += 1
    elif predicted[i] == 1 and actual[i] == 0:
        two += 1
    elif predicted[i] == 0 and actual[i] == 1:
        three += 1
    elif predicted[i] == 1 and actual[i] == 1:
        four += 1
print("***Decision Tree***")
print("\t\t"+"Predicted Negative\t"+"Predicted Positive\t")
print("Negative Cases\t"+str(one)+"\t\t\t"+str(two)+"\t")
print("Positive Cases\t"+str(three)+"\t\t\t"+str(four)+"\t")
print("\n++Statistics++")
print("The accuracy was: "+"%.2f"%float((one + four)/(one+two+three+four)))
print("The recall was: "+ "%.2f"%float(four/(four+three)))
print("The precision was: "+ "%.2f"%float(four/(four+two)))

from sklearn.neighbors import KNeighborsClassifier
neigh = KNeighborsClassifier()
neigh.fit(data, target)

predicted = neigh.predict(data)
actual = mydata.ix[:,22:].values
total = actual.shape[0]

one = 0
two = 0
three = 0
four = 0

for i in range(0,total):
    if predicted[i] == 0 and actual[i] == 0:
        one += 1
    elif predicted[i] == 1 and actual[i] == 0:
        two += 1
    elif predicted[i] == 0 and actual[i] == 1:
        three += 1
    elif predicted[i] == 1 and actual[i] == 1:
        four += 1
print("\n***kNN***")
print("\t\t"+"Predicted Negative\t"+"Predicted Positive\t")
print("Negative Cases\t"+str(one)+"\t\t\t"+str(two)+"\t")
print("Positive Cases\t"+str(three)+"\t\t\t"+str(four)+"\t")
print("\n++Statistics++")
print("The accuracy was: "+"%.2f"%float((one + four)/(one+two+three+four)))
print("The recall was: "+ "%.2f"%float(four/(four+three)))
print("The precision was: "+ "%.2f"%float(four/(four+two)))
