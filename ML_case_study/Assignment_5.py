#import all libraris and modules save in one file
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from warnings import simplefilter
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report


def marvellousDecisionTree():
#step-1 load the data 
    dataset=pd.read_csv("diabetes.csv")
#step2-data preprocessing
    dataset_new = dataset
    # Dataset dimensions - (rows, columns)
    dataset.shape
    # Features data-type
    dataset.info()
    # Feature scaling using MinMaxScaler
    sc = MinMaxScaler(feature_range = (0, 1))
    dataset_scaled = sc.fit_transform(dataset_new)
    dataset_scaled = pd.DataFrame(dataset_scaled)
    
    # Selecting features - [Glucose, Insulin, BMI, Age]
    X = dataset_scaled.iloc[:, [1, 4, 5, 7]].values
    Y = dataset_scaled.iloc[:, 8].values
    
#step-3 Splitting X and Y
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.20, random_state = 42, stratify = dataset_new['Outcome'])   
    # Checking dimensions
    print("checking dimensions:")
    print("X_train shape:", X_train.shape)
    print("X_test shape:", X_test.shape)
    print("Y_train shape:", Y_train.shape)
    print("Y_test shape:", Y_test.shape)
#step-4 Data modeling
    # Logistic Regression Algorithm
    logreg = LogisticRegression(random_state = 42)
    logreg.fit(X_train, Y_train)
    
    #plot graph knn
    X_axis = list(range(1, 31))
    acc = pd.Series()
    x = range(1,31)
    for i in list(range(1, 31)):
        knn_model = KNeighborsClassifier(n_neighbors = i) 
        knn_model.fit(X_train, Y_train)
        prediction = knn_model.predict(X_test)
        acc = acc.append(pd.Series(metrics.accuracy_score(prediction, Y_test)))
    plt.plot(X_axis, acc)
    plt.xticks(x)
    plt.title("Finding best value for n_estimators")
    plt.xlabel("n_estimators")
    plt.ylabel("Accuracy")
    plt.grid()
    plt.show()
    print('Highest value: ',acc.values.max())
    
    # K nearest neighbors Algorithm
    knn = KNeighborsClassifier(n_neighbors = 24, metric = 'minkowski', p = 2)
    knn.fit(X_train, Y_train)
    
    # Decision tree Algorithm
    dectree = DecisionTreeClassifier(criterion = 'entropy', random_state = 42)
    dectree.fit(X_train, Y_train)
        
    # Random forest Algorithm
    ranfor = RandomForestClassifier(n_estimators = 11, criterion = 'entropy', random_state = 42)
    ranfor.fit(X_train, Y_train)
    
    # Making predictions on test dataset
    Y_pred_logreg = logreg.predict(X_test)
    Y_pred_knn = knn.predict(X_test)
    Y_pred_dectree = dectree.predict(X_test)
    Y_pred_ranfor = ranfor.predict(X_test)
    
#step5  model evaluation 
     # Evaluating using accuracy_score metric
    accuracy_logreg = accuracy_score(Y_test, Y_pred_logreg)
    accuracy_knn = accuracy_score(Y_test, Y_pred_knn)
    accuracy_dectree = accuracy_score(Y_test, Y_pred_dectree)
    accuracy_ranfor = accuracy_score(Y_test, Y_pred_ranfor)
    # Accuracy on test set
    print("Accuracy of all algorithms:")
    print("Logistic Regression: " + str(accuracy_logreg * 100))
    print("K Nearest neighbors: " + str(accuracy_knn * 100))
    print("Decision tree: " + str(accuracy_dectree * 100))
    print("Random Forest: " + str(accuracy_ranfor * 100))
    #From the above comparison, we can observe that K Nearest neighbors gets the highest accuracy of 78.57 %
    # Confusion matrix
    print("Confusion matrix is:")
    cm = confusion_matrix(Y_test, Y_pred_knn)
    print(cm)
        
#step 6:Classification report
    print("Classification report is:")
    print(classification_report(Y_test, Y_pred_knn))
    # Heatmap of Confusion matrix
    print("Heatmap for confusion matrix:")
    sns.heatmap(pd.DataFrame(cm), annot=True) 
    
def main():
    marvellousDecisionTree()  
    
if __name__=="__main__":
    main()
