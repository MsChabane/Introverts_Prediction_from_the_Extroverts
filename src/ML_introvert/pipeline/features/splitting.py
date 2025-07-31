import pandas as pd 
from ML_introvert import logger
from ML_introvert.utils import split 
from ML_introvert.constant import *
import os 



df = pd.read_csv(os.path.join(PRE_PROCESSED_PATH,'data_pre_processed.csv'))

 
columns = df.columns.to_list().remove(TARGET)



splits = split(df[columns],df[TARGET],train_size=0.7,stratify_Y=True)














