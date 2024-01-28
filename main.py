import sqlite3

import pandas as pd
import numpy as np

calendario=pd.read_csv('/Users/delfina/Desktop/nuclioproyecto/TMF-Delfina/Data/daily_calendar_with_events.csv')
precios=pd.read_csv('/Users/delfina/Desktop/nuclioproyecto/TMF-Delfina/Data/item_prices.csv')
ventas=pd.read_csv('/Users/delfina/Desktop/nuclioproyecto/TMF-Delfina/Data/item_sales.csv')

calendario.head()

