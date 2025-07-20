import requests
import streamlit  as st
import pandas as pd
import plotly.graph_objects as go
from client import STOCK_API



#  give page title

st.set_page_config(page_title= "STOCK MARKET DATA PLOTING" , layout= "wide")

# Add title
st.title("Stock Market App")

# add subheader 

st.subheader("By varsha Mhetre")


# create  function fetch data


@st.cache_resource(ttl= 3600)
def fetch_data():
    return STOCK_API(api_key= st.secrets['API_KEY'])

stock_api  =  fetch_data()


# take input from user for company

company  =  st.text_input("Enter Company Name here")


# create function for symbol search

@st.cache_data(ttl= 3600)
def  get_symbol(company_name):
    return stock_api.symbol_search(company_name)


# create function for daily time series data
def  get_plot(symbol):
    df  =  stock_api.Time_series_daily(symbol)
    fig  =  stock_api.Chart(df)
    return  fig



if company:
    company_data  =   get_symbol(company)

    if company_data:
        symbols  =  list(company_data.keys())
        option =  st.selectbox("Enter symbol here" , symbols)
        company_info  =  company_data[option]
        st.success(f"**Compnay Name:** ,  {company_info[0]}")
        st.success(f"**Compnay Region:** ,  {company_info[1]}")
        st.success(f"**Compnay Currency:** ,  {company_info[2]}")

        # create one button 
        submit  =  st.button("Plot" ,  type  = "primary")

        if  submit :
            fig  =  get_plot(option)
            st.plotly_chart(fig)

    else:
        st.subheader("Company Not found")


