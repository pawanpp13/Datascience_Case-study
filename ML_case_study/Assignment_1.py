#KNN Algorithm implementation in Python

from sklearn import preprocessing
import pandas as pd
from sklearn import tree
from scipy.spatial import distance
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
        
        
def Marvellous():
    
    data=pd.read_csv("MarvellousInfosystems_PlayPredictor.csv",index_col=0)
    print("size of dataset is :",len(data))
    
    #clean prepear and mainpulate data
    
    features_name=['Wether','Temperature']
    print("name of features is :",features_name)
    
    wether=data.Wether
    temperature=data.Temperature
    play=data.Play
    
     # Converting string labels into numbers.
    le = preprocessing.LabelEncoder()
    
    # Encode labels in column 'wether'. 
    wether_encodded=le.fit_transform(wether)
    print(wether_encodded)
    
    #encode labels in column 'temperature'
    temp_encodded=le.fit_transform(temperature)
    label=le.fit_transform(play)
    print(temp_encodded)
   
    
    #combinig weather and temp into single listof tuples
    features=list(zip(wether_encodded,temp_encodded))
    
    #drop unwanted column
    data.drop(data.filter(regex="Unnamed"),axis=1, inplace=True)
    print(data.head())
    
    #train data
    model=KNeighborsClassifier(n_neighbors=3)
    #model using training sets
    model.fit(features,label)
    
    #test data
    predicted=model.predict([[0,2]]) #0=overcast,2=mild
    print(predicted)
    
    if predicted==1:
        print("you can play")
    else:
        print("Dont play")
        
def main():     
    Marvellous()
    print("Machine learinig application")
    print("play predict application used for KNN")


if __name__=="__main__":
    main()



