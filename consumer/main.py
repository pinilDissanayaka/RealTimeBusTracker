from data_reader import formate_data
from kafka import preduce_data



data = formate_data()


for _data in data:
    preduce_data(data=_data)