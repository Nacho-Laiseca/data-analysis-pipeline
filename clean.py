# Second step, we clean and organise the data. For this we import some more libraries and the file acquisition.

import datetime
import pandas as pd
from acquisition import acquisition



def clean_data():
    
    data = acquisition()

    # we get rid of rows with no price
    data = data.dropna(subset=["price"])
    
    # we want to analyse AVE prices so this is the only type of train we keep
    # data["train_type"].value_counts()
    data = data[data["train_type"] == "AVE"]

    # As we want the Turista solo plaza H class is for people with a disability we delte all this rows as we want to analyse ordinary tickets to get a more realistic cost for the avg person
    # data["train_class"].value_counts()
    data = data[data["train_class"] != "TuristaSÃ³lo plaza H"]

    # we are going to keep only the promo and flexible tickets, the most common type of fares
    list_values = ["COD.PROMOCIONAL","Mesa","Promo +","Grupos Ida","4x100"]
    for col in list_values:
        data = data[data["fare"]!=col]

    # As we have decided to analyze only trips with origin in Madrid we drop the rest
    data = data[data["origin"]=="MADRID"]

    # data["destination"].value_counts()

    return data

def manipulation():
    data = clean_data()

    # we begin by getting the start_date in datetime format as it will be needed for our analysis
    data['date'] = [datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') for x in data["start_date"]]

    # we create all the time frames we want
    data["year"] = [x.year for x in data["date"]]
    data["month"] = [x.month for x in data["date"]]
    data["hour"] = [x.hour for x in data["date"]]
    data["week"] = [x.week for x in data["date"]]
    data["day"] = [x.day for x in data["date"]]
    data["weekday"] = [x.weekday() for x in data["date"]]
    daytime_labels = ['early-morning', 'morning', 'noon', 'afternoon', 'evening']
    cutoffs = [0,9,11,14,20,23]
    data["daytime"] = pd.cut(data["hour"],cutoffs, labels=daytime_labels)
    days_labels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday','Saturday','Sunday']
    cutoffs = [0,1,2,3,4,5,6,7]
    data["weekdays"] = pd.cut(data["weekday"],cutoffs, labels=days_labels)

    # Choose columns for our dataframe
    data = data[['origin', 'destination','start_date','year','month','week','day','weekdays','hour','daytime','train_class','price','distance_km']]

    # we cast the necessary columns to the appropiate type so we can calculate the final column needed for our analysis
    convert_dict = {'distance_km': int, 'price': float} 
    data = data.astype(convert_dict)
    data["avg_price_per_km"] = round(data["price"]/data["distance_km"],2)

    return data