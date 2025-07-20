import requests
import streamlit  as st
import pandas as pd
import plotly.graph_objects as go
class STOCK_API:
    def __init__(self , api_key):
        self.api_key  = api_key
        self.url  =  "https://alpha-vantage.p.rapidapi.com/query"
        self.headers = {"x-rapidapi-key": api_key,
                        "x-rapidapi-host": "alpha-vantage.p.rapidapi.com"}
    

    # create method  =
    def symbol_search(self,  keyword) : 
        querystring = {"datatype":"json",
                       "keywords":keyword,
                       "function":"SYMBOL_SEARCH"}
        response = requests.get(self.url, headers=self.headers, params=querystring)
        data  = (response.json())
        dict1  =  {}
        for i  in  data['bestMatches']:
            symbols  =  i['1. symbol']
            dict1[symbols] = [i['2. name'] ,  i['4. region'] , i['8. currency']]
        return dict1  
    

    # craete method for daily time series data

    def  Time_series_daily(self ,  symbol):
        querystring = {"function":"TIME_SERIES_DAILY",
                       "symbol":symbol,
                       "outputsize":"compact","datatype":"json"}
        response = requests.get(self.url, headers=self.headers, params=querystring)
        data1  =  response.json()
        df  =  pd.DataFrame(data1['Time Series (Daily)']).T
    # change data type
        df  =  df.astype("float")

        # change index data type
        df.index  =  pd.to_datetime(df.index)

        # add name to index

        df.index.name  =  "Date"
        return df


# create function for plot
    def Chart(self  , df):
        fig = go.Figure(data=[go.Candlestick(x=df.index,
                open=df['1. open'],
                high=df['2. high'],
                low=df['3. low'],
                close=df['4. close'])])
     
        fig.update_layout(title  = "Chandelstick chart",  xaxis_title  = "Date" )
        return  fig

        
        
      
  

        
        

    