import os 
import pandas as pd 
from ML_introvert.constant import *
from ML_introvert.utils import split
from sklearn.preprocessing import LabelEncoder
import joblib 
from ML_introvert import logger


os.makedirs(RAW_DATA_PATH,exist_ok=True)
logger.info('READING THE DATASET')
df = pd.read_csv(os.path.join(RAW_DATA_PATH,DATA_FILENAME))
logger.info('SPLIT THE FEATURES AND THE TARGET.')
X = df.drop(columns=['id',TARGET])
Y = df[TARGET]

logger.info('ENCODE THE FEATURES AND THE TARGET.')
X = pd.get_dummies(X)

encoder = LabelEncoder()
Y=encoder.fit_transform(Y)
logger.info('SAVE THE ENCODER.')
joblib.dump(encoder,os.path.join(MODELS_PATH,'encoder.pkl'))
logger.info('SAVE THE FEATURES AND THE TARGET.')
X[TARGET]=Y
X.to_csv(os.path.join(PRE_PROCESSED_PATH,'data_pre_processed.csv'),index=False)







































