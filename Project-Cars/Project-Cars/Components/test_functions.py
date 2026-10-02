
import sys
import os
import pytest

[pytest]
pythonpath = "." "../Models/" "../.."

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))


from functions import format_dict, load_model, predict_price#pytest seems to need parent directory


import pandas as pd
import pickle
from xgboost import XGBRegressor
import numpy as np
import json

@pytest.fixture
def my_car():
    return {"Kilometre":140000,"Annee":2014,"Marque":'HYUNDAI',"Energie":"Diesel","PrixNeuf":22000,"Boites de vitesse":"Manuelle",
        "Chevaux":75,"bluetooth":True,"cam_recul":False,"clim_auto":True,"feux_led":True,"gps":False,
        "inte_cuir":False,"isofix":True,"jantes_alliage":True,"regulateur_vitesse":True,"tete_haute":False,
        "toit_ouvrant":True,"toit_panoramique":True,"trois_siege_indiv":False,"radar_recul":True,"type":"berline","Modele":"","Prix":10000}


def test_prediction(my_car):
    df_jumeau_numerique=format_dict(my_car)
    assert type(df_jumeau_numerique)==pd.core.frame.DataFrame
    model,P=load_model()
    price=int(np.round(predict_price(model,P,df_jumeau_numerique)[0]))
    assert type(price)==int
