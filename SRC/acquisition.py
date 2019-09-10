# First we import the modules needed for acquisition

import requests
from bs4 import BeautifulSoup
import pandas as pd

def acquisition():
    data = data = pd.read_csv("../data-analysis-pipeline/input/renfe.csv", encoding="latin")
    res = requests.get("https://madridguia.com/como-llegar/distancias-a-madrid/gmx-niv163.htm")
    data_web = res.text
    soup = BeautifulSoup(data_web, 'html.parser')
    distances = soup.select('table td strong font')
    cities = ["VALENCIA","SEVILLA","BARCELONA"]
    list_distances = {"destination":[distances[i].text for i in range(len(distances)) if distances[i].text in cities],"distance_km":[((distances[i+1].text).split(" "))[0] for i in range(len(distances)) if distances[i].text in cities]}
    data_distances = pd.DataFrame(list_distances)
    data = pd.merge(data, data_distances, on='destination')
    return data
