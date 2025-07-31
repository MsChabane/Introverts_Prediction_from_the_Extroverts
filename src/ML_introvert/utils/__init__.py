from sklearn.model_selection import train_test_split
import pandas as pd




def split(X,Y,train_size,stratify_Y=False) :
    X_train,X_tmp ,Y_train,Y_tmp = train_test_split(X,Y,train_size=train_size,stratify=Y if stratify_Y else None)
    X_val,X_test,Y_val,Y_test = train_test_split(X_tmp,Y_tmp,test_size=0.5)
    return [(X_train,Y_train),(X_val,Y_val),(X_test,Y_test)]





