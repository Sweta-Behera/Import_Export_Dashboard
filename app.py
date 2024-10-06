import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

df=pd.read_csv('Imports_Exports_Dataset.csv')

sdset = df.sample(n = 3001, random_state = 55051)

# Page configuration
st.set_page_config(
    page_title="Import-Export Dashboard",
    page_icon="📦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Page background color and custom CSS
page_bg_color = """
    <style>
    body {
        background-color: #e8f5e9;
    }
    .metric-container {
        display: flex;
        justify-content: space-between;
    }
    .metric-box {
        padding: 15px;
        margin: 5px;
        border-radius: 10px;
        background-color: #ffffff;
        box-shadow: 2px 2px 8px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    .metric-title {
        font-size: 16px;
        font-weight: bold;
        color: #333333;
    }
    .metric-value {
        font-size: 20px;
        color: #007bff;
    }
    .metric-delta {
        color: #ff6b6b;
    }
    </style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title('📦 Import-Export Dashboard')

# Assuming `sdset` contains your data
revenue_data = sdset.groupby('Import_Export')['Value'].sum().reset_index()
total_revenue = revenue_data['Value'].sum()
revenue_data['Percentage'] = (revenue_data['Value'] / total_revenue) * 100

fig, ax = plt.subplots(figsize=(8, 5))
bars = ax.bar(revenue_data['Import_Export'], revenue_data['Value'], color=['blue', 'green'])
ax.set_xlabel('Category (Imports/Exports)')
ax.set_ylabel('Total Revenue')
ax.set_title('Total Revenue from Imports and Exports')

for bar, percentage in zip(bars, revenue_data['Percentage']):
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{percentage:.1f}%', ha='center', va='bottom')

st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Group by customer and sum the value
top_customers = sdset.groupby('Customer')['Value'].sum().reset_index()
top_customers = top_customers.sort_values(by='Value', ascending=False).head(5)

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(top_customers['Customer'], top_customers['Value'], color='orange')
ax.set_xlabel('Customer')
ax.set_ylabel('Total Revenue')
ax.set_title('Top 5 Customers by Revenue')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.0f}', ha='center', va='bottom')

st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Group by customer and count the occurrences
customer_counts = sdset['Customer'].value_counts()
most_repeated_customer = customer_counts.head(1)
other_customers_count = customer_counts.sum() - most_repeated_customer.values[0]

labels = [most_repeated_customer.index[0], 'Other Customers']
sizes = [most_repeated_customer.values[0], other_customers_count]
colors = ['gold', 'lightcoral']
explode = (0.1, 0)

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
ax.set_title('Most Repeated Customer vs Other Customers')
ax.axis('equal')

st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Assuming `payment_data` contains the payment terms
payment_data = sdset['Payment_Terms'].value_counts().reset_index()
payment_data.columns = ['Payment_Terms', 'Count']

fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(payment_data['Payment_Terms'], payment_data['Count'], color='purple')
ax.set_xlabel('Payment Terms')
ax.set_ylabel('Count')
ax.set_title('Most Preferred Payment Terms')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval}', ha='center', va='bottom')

st.pyplot(fig)

import streamlit as st
import matplotlib.pyplot as plt

# Group by country and sum the value
top_countries = sdset.groupby('Country')['Value'].sum().reset_index()
top_countries = top_countries.sort_values(by='Value', ascending=False).head(10)

fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(top_countries['Country'], top_countries['Value'], color='green')
ax.set_xlabel('Country')
ax.set_ylabel('Total Revenue')
ax.set_title('Top 10 Trading Countries by Revenue')

for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.0f}', ha='center', va='bottom')

st.pyplot(fig)

