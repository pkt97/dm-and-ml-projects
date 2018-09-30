#import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
#from sklearn import tree
from sklearn.metrics import classification_report
#from sklearn.preprocessing import LabelEncoder
def read_data():
    data=pd.read_csv('adult.csv',sep=',')
    """for column in data.columns:
        if data[column].dtype == type(object):
            le = LabelEncoder()
            data[column] = le.fit_transform(data[column])"""

    #to print the headers of dataset
    print("First five observations in dataset are:")
    print(data.head())
    return data

#function to split the data from target variable and also for training and splitting
def split_data(data):
    a=data.values[:,0:13] #'a' is input variable  
    b=data.values[:,14] #'b' is output variable

    #splitting the dataset into training and testing
    a_train,a_test,b_train,b_test=train_test_split(a,b,test_size=0.2,random_state=100)
    return a,b,a_train,a_test,b_train,b_test

#function to train the dataset
def train_data(a_train,a_test,b_train):
    #training the dataset using entropy
    classify=DecisionTreeClassifier(criterion="entropy",random_state=100,max_depth=10,min_samples_leaf=5)
    classify.fit(a_train,b_train)        
    return classify

#function for predicting whether income is >$50K or not
def pred_data(a_test,classify):
    #predicting the labels
    b_predict=classify.predict(a_test)
    print("Predicted values for income are:")
    print(b_predict)

#function for calculating accuracy and classification report of the algorithm
def calculate(b_test,b_predict):
    #calculate the accuracy
    print("Accuracy is:",accuracy_score(b_test,b_predict)*100)

    #print the classification report
    #print("Classification report:",classification_report(b_test,b_predict))

#driver function    
def main(): 
    data1=read_data()
    a,b,a_train,a_test,b_train,b_test=split_data(data1)
    class_entropy=train_data(a_train,a_test,b_train)
    predict=pred_data(a_test,class_entropy)
    cal=calculate(b_test,predict)

#calling the main function    
if __name__=="__main__":
    main()    
