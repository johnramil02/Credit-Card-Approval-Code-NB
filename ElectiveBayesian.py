from email.utils import decode_rfc2231
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.metrics import accuracy_score, classification_report
from sklearn import metrics

credit_card = pd.read_csv("original dataset clean.csv")
print(credit_card)   

number = LabelEncoder()


features = ["Debt", "BankCustomer", "YearsEmployed", "Employed", "CreditScore", "Income"]
target = ['Approved']

features_train, features_test, target_train, target_test = train_test_split(credit_card[features],
credit_card[target], test_size = 0.30,
   random_state = 20)

# Displaying the split datasets
print('\tTraining Features\n ',features_train)  #3 Print all of these
print('\tTesting Features\n ',features_test)
print('\tTraining Target\n ',target_train)
print('\tTesting Target\n ',target_test)

model = GaussianNB()

model.fit(features_train, target_train)

pred = model.predict(features_test)

accuracy = accuracy_score(target_test, pred)

print(type(target_test))


# Put into CSV file
import csv


with open('pred.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    
    for x in pred:
        if(x == 1):
            writer.writerow("1")
        elif(x == 0):
            writer.writerow("0")


with open('target.csv', 'w', newline="") as f:
    writer = csv.writer(f)
    
    for item in target_test['Approved']:
        if(item == 1):
            writer.writerow("1")
        elif(item == 0):
            writer.writerow("0")

print("Normal Accuracy",accuracy)
print("\nModel Accuracy = ",accuracy*100,"%") 
print(metrics.confusion_matrix(target_test, pred))
print(metrics.classification_report(target_test, pred))



# Function for Naive Bayes model prediction 
def bayesianPrediction(attributes):
    answer = model.predict(attributes)
    if answer == 1:
        print("True")
        return True
    
    elif answer == 0:
        print("False")
        return False