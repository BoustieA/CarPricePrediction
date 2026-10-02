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
#from models_ import Genre,Sales,Games,Publisher, Platform, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


def open_file():
    folder_path = os.path.realpath(__file__)#[:-32]
    print(folder_path)
    return
    file_path="Data/autosphere_nomissing.csv"
    return pd.read_csv(folder_path+file_path)

def getSession():
    engine = create_engine('sqlite:///database.sqlite')
    # Création de la base de données
    Base.metadata.create_all(engine)

    # Création d'une session
    return Session(bind=engine)

open_file()
def create_database():
    return
    session=getSession()
    
    mapping_platform={}
    mapping_genre={}
    mapping_publisher={}
    mapping_game={}
    
    genres=df.Genre.unique()
    for i in range(genres.shape[0]):
        mapping_genre[genres[i]]=i
        g=Genre(name=genres[i],id=i)
        session.add(g)
    
    publisher=df.Publisher.unique()
    for i in range(publisher.shape[0]):
        mapping_publisher[publisher[i]]=i
        g=Publisher(name=publisher[i],id=i)
        session.add(g)

    platform=df.Platform.unique()
    for i in range(platform.shape[0]):
        mapping_platform[platform[i]]=i
        g=Platform(id=i,name=platform[i])
        session.add(g)
    
    games=df.Name.unique()
    for i in range(games.shape[0]):
        genre=df.loc[df.Name==games[i],"Genre"].values[0]
        mapping_game[games[i]]=i
        g=Games(id=i,genre_id=mapping_genre[genre],name=games[i])
        session.add(g)
    
    
    for _,row in df.iterrows():
        sale=Sales(row,mapping_game,mapping_publisher,mapping_platform)
        session.add(sale)
    session.commit()

if __name__=="__main__":
    file=open_file()
    
    
    
    df=open_file()
    df=preprocessing(df)
    
    create_database()


    