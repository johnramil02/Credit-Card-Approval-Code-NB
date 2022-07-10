import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn import metrics

credit_card = pd.read_csv("Clean Dataset Credit Score[NOT FINAL].csv")
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

print(target_test)

print(pred)

print("Normal Accuracy",accuracy)
print("\nModel Accuracy = ",accuracy*100,"%") 

    
def bayesianPrediction(attributes):
    answer = model.predict(attributes)
    if answer == 1:
        print("True")
        return True
    
    elif answer == 0:
        print("False")
        return False
<<<<<<< HEAD

print(metrics.confusion_matrix(target_test, pred))
print(metrics.classification_report(target_test, pred))
=======
    
>>>>>>> 07aaf9022f01754b58ca2595cc1b61cfdeaa52f5
