# inputs -> stock DataFrame, initial_investment, transaction_cost, current_step, lookback (imp, default is 1 year),
# state_space = stock_dimension 
# asset_memory -> port_memory, portfolio_return_memory -> reward_memory, date_memory -> date_memory, actions_memory -> action_memory

import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def add_cov_matrix(df):
    # Sort the data and index by date and Ticker
    df=df.sort_values(['Date','Ticker'],ignore_index=True) 
    df.index = df.Date.factorize()[0]
    covariance_list = []
    for i in range(252,len(df.index.unique())):
        data_252 = df.loc[i-252:i,:]
        price_252=data_252.pivot_table(index = 'Date',columns = 'Ticker', values = 'Close')
        return_252 = price_252.pct_change().dropna()
        covariance_1 = return_252.cov().values 
        covariance_1 = covariance_1
        covariance_list.append(covariance_1)  
    df_cov = pd.DataFrame({'Date':df.Date.unique()[252:],'covariance':covariance_list})
    df = df.merge(df_cov, on='Date')
    df = df.sort_values(['Date','Ticker']).reset_index(drop=True)
    
    return df

def env_utils_asset_save(dm, rm):
        dates = dm
        rewards = rm
        account_value = pd.DataFrame({'Date':dates,'daily_return':rewards})
        return account_value









    


            








        


