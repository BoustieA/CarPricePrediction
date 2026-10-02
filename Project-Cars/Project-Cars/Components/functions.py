import pickle
from xgboost import XGBRegressor
import pandas as pd
import numpy as np

def load_model():
    """
    fonction de chargement du modèle de ML et de la pipeline de preprocessing fitted
    output : model, Pipeline
    modele de
    """
    model = XGBRegressor()
    model.load_model('Models/model_prediction_car_price.json')

    with open('Models/Preprocessor.pkl', 'rb') as f:
            P=pickle.load(f)
    return model,P

def format_dict(jumeau_numerique):
    """
    input : dictionnary of features
    
    return :dataframe for preidction
    """
    return pd.DataFrame({k:[jumeau_numerique[k]] for k in jumeau_numerique})

def predict_price(model,P,jumeau_numerique_df):
    """
    fonction qui prends en arguments le modèle de ML, la pipeline, l'échantillon et retourne la prédiction du modèle
    input : -model de ML
            -Pipeline sklearn
            -dataframe de l'échantillon 
    output:
            -prediction de la valeur de regression
    """
    data=P.transform(jumeau_numerique_df)[:,1:]
    prediction=model.predict(data)
    return model.predict(data)

def pipeline_prediction(dic_jumeau_numerique):
    """
    input : dictionnary of features

    return prediction
    
    this function :
    -take a dictionnary with cars features, 
    -convert it into a dataframe
    -preprocess it through sklearn a trained pipeline
    -predict a price with trained model

    """
    df_jumeau_numerique=format_dict(dic_jumeau_numerique)
    model,P=load_model()
    return int(np.round(predict_price(model,P,df_jumeau_numerique)[0]))
       
      