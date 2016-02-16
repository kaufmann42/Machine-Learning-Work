# John Kaufmann
# 3/16/2016
# BME4931
#
# print a confusion matrix given the predicted classifiers, the actual classifiers and the name of the structure

def print_ConfusionMatrix(predicted, actual, name):
    actual = predicted
    total = actual.shape[0]

    one = 0
    two = 0
    three = 0
    four = 0

    #construct confusion matrix
    for i in range(0,total):
        if predicted[i] == 0 and actual[i] == 0:
            one += 1
        elif predicted[i] == 1 and actual[i] == 0:
            two += 1
        elif predicted[i] == 0 and actual[i] == 1:
            three += 1
        elif predicted[i] == 1 and actual[i] == 1:
            four += 1
    #print everythin
    print("***" + name + "***")
    print("\t\t"+"Predicted Negative\t"+"Predicted Positive\t")
    print("Negative Cases\t"+str(one)+"\t\t\t"+str(two)+"\t")
    print("Positive Cases\t"+str(three)+"\t\t\t"+str(four)+"\t")
    print("\n++Statistics++")
    print("The accuracy was: "+"%.2f"%float((one + four)/(one+two+three+four)))
    print("The recall was: "+ "%.2f"%float(four/(four+three)))
    print("The precision was: "+ "%.2f"%float(four/(four+two)))
