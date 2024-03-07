# import joblib


# from sklearn.preprocessing import MinMaxScaler
# import numpy as np

# # Your original array
# last_row_features = df.drop(columns=['Target']).iloc[-1]
# last_row_features_array = np.array(last_row_features)

# # Reshape the array to a 2D array (required by MinMaxScaler)
# last_row_features_array = last_row_features_array.reshape(-1, 1)

# # Create the MinMaxScaler
# scaler = MinMaxScaler()

# # Fit and transform the data
# features_scaled_array = scaler.fit_transform(last_row_features_array)
# features_scaled_array_reshaped = features_scaled_array.reshape(1, -1)


# model_save = joblib.load('deep_model')
# model_save.predict()

import pandas as pd
import yfinance as yf 
from datetime import datetime
def data_collect(symbol , start_date):
    end_date = datetime.today().strftime('%Y-%m-%d')
    df = yf.download(symbol ,start=start_date , end= end_date)
    return df
data_collect('PAYTM.BO' , '2023-01-25')
