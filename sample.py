import numpy as np
import plotly.express as px
import csv


def setup():
    data_path = 'temperature-ice cream.csv'
    dataSource = getDataSource(data_path)
    findCorrealation(dataSource)


def getDataSource(data_path):
    ice_cream_sales = []
    cold_drink_sales = []
    with open(data_path) as csv_files:
        csv_reader = csv.DictReader(csv_files)
        for row in csv_reader:
            ice_cream_sales.append(float(row['Temperature']))
            cold_drink_sales.append(float(row['Ice-cream Sales']))

    return {'x': ice_cream_sales, 'y': cold_drink_sales}

def findCorrealation(dataSource):
    correlation = np.corrcoef(dataSource['x'],dataSource['y'])
    print('Correlation between temp and ice-cream sales is:-  \n',correlation[0,1] )


setup()