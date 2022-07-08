import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

print("hi")

credit_card = pd.read_csv("Final Dataset Credit Score.csv")
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

print("OKAY")
print(target_test)
print("OKAY")
print(pred)

print("Normal Accuracy",accuracy)
print("\nModel Accuracy = ",accuracy*100,"%") 

answer = model.predict([[35,0,8,1,50,35]]) 
if answer == 1:
    print("\nApproved")
elif answer == 0:
    print("\nNot Approved")


