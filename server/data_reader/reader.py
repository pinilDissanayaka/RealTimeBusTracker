import os
from uuid import uuid4
import json

def read_data()->dict:
    try:
        with open("test/data/bus1.json", "r") as data_file:
            data =json.load(data_file)
    except FileNotFoundError as e:
        raise e
    return data

def formate_data()-> dict:
    data = read_data()["geometry"]["coordinates"]
    
    formated_data=[]
    
    for _data in data:
        data_point={}
        
        data_point["id"]=str(uuid4())
        data_point["route_num"]="152"
        data_point["lat"]=_data[0]
        data_point["lon"]=data[1]        
        
        formated_data.append(data_point)
        
        
    return formated_data






