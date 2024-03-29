#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests


# In[2]:


def make_graph(data, title):
    plt.figure(figsize=(10, 6))
    plt.plot(data['Date'], data['Close'], label='Close Price', color='blue')
    plt.title(title)
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()


# In[3]:


# Question 1: Use yfinance to Extract Tesla Stock Data
tesla_data = yf.download('TSLA', start='2022-01-01', end='2022-12-31')
tesla_data.reset_index(inplace=True)
print(tesla_data.head())


# In[5]:


# Question 2: Use Webscraping to Extract Tesla Revenue Data
def scrape_tesla_revenue():
    url = 'https://example.com/tesla-revenue-data'  # Replace this URL with the actual URL of Tesla revenue data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Use BeautifulSoup to parse the HTML and extract revenue data
    # Store the revenue data into a DataFrame called tesla_revenue
    # Here's a dummy example of creating tesla_revenue DataFrame
    tesla_revenue = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                                  'Revenue': [1000000, 1500000, 2000000]})
    return tesla_revenue


# In[6]:


tesla_revenue = scrape_tesla_revenue()
print(tesla_revenue.tail())


# In[7]:


# Question 3: Use yfinance to Extract GameStop Stock Data
gme_data = yf.download('GME', start='2022-01-01', end='2022-12-31')
gme_data.reset_index(inplace=True)
print(gme_data.head())


# In[8]:


# Question 4: Use Webscraping to Extract GME Revenue Data
def scrape_gme_revenue():
    url = 'https://example.com/gme-revenue-data'  # Replace this URL with the actual URL of GME revenue data
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Use BeautifulSoup to parse the HTML and extract revenue data
    # Store the revenue data into a DataFrame called gme_revenue
    # Here's a dummy example of creating gme_revenue DataFrame
    gme_revenue = pd.DataFrame({'Date': ['2022-01-01', '2022-01-02', '2022-01-03'],
                                'Revenue': [500000, 600000, 700000]})
    return gme_revenue

gme_revenue = scrape_gme_revenue()
print(gme_revenue.tail())


# In[9]:


# Question 5: Plot Tesla Stock Graph
make_graph(tesla_data, title='Tesla Stock Prices')


# In[10]:


# Question 6: Plot GameStop Stock Graph
make_graph(gme_data, title='GameStop Stock Prices')


# In[ ]:




