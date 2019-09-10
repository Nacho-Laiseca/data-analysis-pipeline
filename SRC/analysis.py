# Finally, we analysis our data and come up with some conclusion for our report

import pandas as pd
import matplotlib.pyplot as plt
from clean import manipulation


def report(destination,period):
    data = manipulation()

    # First we need to get our data for our choosen city and establish the time period
    data_city = data[data["destination"]==destination]
    period = period

    # we make 3 dataframe, one for each class
    data_preferente = data_city[data_city['train_class']=="Preferente"]
    data_turistaplus = data_city[data_city['train_class']=="Turista Plus"]
    data_turista = data_city[data_city['train_class']=="Turista"]

    # Here we get the avg price per km for each class, we take from the whole year as we want a general overview
    dt_preferente = data_preferente.groupby(["year"]).agg({'avg_price_per_km':'mean'}).values
    dt_turistaplus = data_turistaplus.groupby(["year"]).agg({'avg_price_per_km':'mean'}).values
    dt_turista = data_turista.groupby(["year"]).agg({'avg_price_per_km':'mean'}).values

    # we prepare everything to create our graphs

    ax = plt.gca()

    data_preferente.groupby([period]).agg({'price':'mean'}).plot(color="red",ax=ax,title="Avg. price of train tickets per {} from MADRID to {}".format(period,destination))
    data_turistaplus.groupby([period]).agg({'price':'mean'}).plot(color="blue",ax=ax)
    data_turista.groupby([period]).agg({'price':'mean'}).plot(color="green",ax=ax)
    ax.legend(["Preferente", "Turista+","Turista"])

    # Finally we have our data for the report

    return print("During this year 2019, the avg. price per km from MADRID to {} in the three diferents class categories have been: {}€/km for Preferente, {}€/km for Turista Plus and {}€/km for Turista.".format(destination,round(dt_preferente[0][0],2),round(dt_turistaplus[0][0],2),round(dt_turista[0][0],2))), plt.show()

