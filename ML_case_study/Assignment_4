#There is one data set of advertisement agency.assnt-4
# import all modules
from sklearn import preprocessing
import pandas as pd
from sklearn import tree
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

#step-1,Get Data

def MarevllouesAdevertising():
    
    data=pd.read_csv("Advertising.csv")
    print("size of dataset is :",len(data))
    #drop unwanted column
    data.drop(data.filter(regex="Unnamed"),axis=1, inplace=True)
    print(data.head())
    print(data.info())
    
    #Step 2:Clean, Prepare and Manipulate data
    #initialise thevariavble dependent or independent
    X=data.drop(['sales'],axis=1)
    y=data['sales'].values.reshape(-1,1)
    
    #step3:train the dataset
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
    #fit the data
    Lr=LinearRegression()
    Lr.fit(X_train,y_train)
    
    #predict the data
    y_pred=Lr.predict(X_test)
    print("predict value is:",y_pred)
    
    #calculate coeficent and intercept
    cof=Lr.coef_
    print("coeficent is :",cof) 
    intr=Lr.intercept_
    print("intercept value is :",intr)
    
    #finde the r-sqaure value
    r_sqr=r2_score(y_test,y_pred)
    print("value of R-square :",r_sqr)
    # graphical reresent dataset

def main():
    MarevllouesAdevertising()

if __name__=="__main__":
    main()


