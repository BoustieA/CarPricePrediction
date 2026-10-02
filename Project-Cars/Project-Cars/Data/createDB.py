# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 09:49:20 2024

@author: adrie
"""
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
import os
import seaborn as sns
from orm import *
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import numpy as np

def open_file():
    folder_path = os.getcwd()
    file_path="/car_fused_filled.csv"
    return pd.read_csv(folder_path+file_path)

def getSession():
    engine = create_engine('sqlite:///database.sqlite')
    # Création de la base de données
    Base.metadata.create_all(engine)

    # Création d'une session
    return Session(bind=engine)

def create_database():
    session=getSession()
    
    mapping_model,mapping_energie,mapping_marque,mapping_btv,mapping_type={},{},{},{},{}
    
    energies=df.Energie.unique()
    for i in range(energies.shape[0]):
        mapping_energie[energies[i]]=i
        g=Energie(name=energies[i],id=i)
        session.add(g)
    
    
    marques=df.Marque.unique()
    for i in range(marques.shape[0]):
        mapping_marque[marques[i]]=i
        m=Marque(name=marques[i],id=i)
        session.add(m) 
        
    types=df.type.unique()
    for i in range(types.shape[0]):
        mapping_type[types[i]]=i
        m=Type(name=types[i],id=i)
        session.add(m) 


    btv=df[["Boites de vitesse"]].drop_duplicates().values.ravel()
    for i in range(btv.shape[0]):
        mapping_btv[btv[i]]=i
        g=BoiteVitesse(id=i,name=btv[i])
        session.add(g)
    

        
    df_marque_model=df[["Marque","Modele"]].drop_duplicates()
    #model=df_marque_model.Modele.values
    for i,row in df_marque_model.iterrows():

        model=row.Modele
        mapping_model[model]=i
        m=Modele(row,mapping_marque)

        session.add(m)



    
    
    
    for _,row in df.iterrows():
        v=Voiture(row,mapping_btv,mapping_model,mapping_energie, mapping_marque, mapping_type)
        session.add(v)

    session.commit()
    session.close()
if __name__=="__main__":
    file=open_file()
    
    
    
    df=open_file()
    
    create_database()


    