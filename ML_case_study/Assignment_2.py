#There is one data set of wine which classify the wines according to its contents into three classes.
from sklearn import metrics
import pandas as pd
from sklearn import datasets
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler


def  marvellousWinePredictor():
        wine=datasets.load_wine()
    
        #clean prepear and mainpulate data
        # features and labels(targets)
        print(wine.feature_names)
        print(wine.target_names) #(class_0,class_1,class_2)
       
        # print top 5 records
        print(wine.data[0:5])

        # print wine labels(0:class_0,1:class_1,2:class-2)
        print(wine.target)
       # Split dataset into training set and test set
        X_train, X_test, y_train, y_test = train_test_split(wine.data,wine.target, test_size=0.3) # 70% training and 30% test
        print(X_train.shape)
        print(X_test.shape)
        
      
        #Create KNN Classifier fit the model
        classifier = KNeighborsClassifier(n_neighbors=3)
        model=classifier.fit(X_train,y_train)
        
        #Predict the response for test dataset
        y_pred =classifier.predict(X_test) #class
        print(y_pred)
        
        # Model Accuracy, how often is the classifier correct
        print("Accuracy of the model is :",metrics.accuracy_score(y_test,y_pred))
        
def main():
    marvellousWinePredictor()
    print(".......ML application of wine predictor.........")
    
    
if __name__=="__main__":
    main()

