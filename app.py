import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

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

import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Group data by 'Import_Export' and calculate total revenue for each
revenue_data = sdset.groupby('Import_Export')['Value'].sum().reset_index()

# Create a donut chart using Plotly
fig = px.pie(
    revenue_data, 
    names='Import_Export',  # Categories (Imports/Exports)
    values='Value',  # Total revenue for each category
    hole=0.4,  # Create the donut hole by setting the value for the hole parameter
    title='Total Revenue from Imports and Exports'
)

# Customize the chart (optional)
fig.update_traces(textinfo='percent+label')  # Show both percentages and labels
fig.update_layout(
    showlegend=True, 
    legend_title_text='Category',  # Legend title
    annotations=[dict(text='Revenue', x=0.5, y=0.5, font_size=20, showarrow=False)]  # Center text
)

# Display the chart in Streamlit
st.plotly_chart(fig)



import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Sidebar filter for Import/Export selection
transaction_type = st.selectbox('Select Transaction Type:', ['Both', 'Import', 'Export'])

# Filter the data based on the selected transaction type
if transaction_type == 'Import':
    filtered_data = sdset[sdset['Import_Export'] == 'Import']
elif transaction_type == 'Export':
    filtered_data = sdset[sdset['Import_Export'] == 'Export']
else:
    filtered_data = sdset

# Group by customer and sum the value for filtered data
top_customers = filtered_data.groupby('Customer')['Value'].sum().reset_index()
top_customers = top_customers.sort_values(by='Value', ascending=False).head(5)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(top_customers['Customer'], top_customers['Value'], color='orange')

ax.set_ylabel('Customer')
ax.set_xlabel('Total Revenue')
ax.set_title(f'Top 5 Customers by Revenue ({transaction_type})')

# Add labels on the bars
for bar in bars:
    xval = bar.get_width()
    ax.text(xval, bar.get_y() + bar.get_height()/2, f'{xval:.0f}', va='center', ha='left')

# Display the plot in Streamlit
st.pyplot(fig)




import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Sidebar filter for country selection
country_options = sdset['Country'].unique()
selected_country = st.selectbox('Select Country:', ['All'] + list(country_options), key='country_selectbox')

# Filter data based on the selected country
if selected_country != 'All':
    filtered_data = sdset[sdset['Country'] == selected_country]
else:
    filtered_data = sdset

# Group by Product Category and sum the revenue (Value)
profitable_category = filtered_data.groupby('Category')['Value'].sum().reset_index()
profitable_category = profitable_category.sort_values(by='Value', ascending=False)

# Create a bar chart using Plotly Express
fig = px.bar(profitable_category, 
             x='Category', 
             y='Value', 
             title=f'Most Profitable Product Categories ({selected_country})', 
             labels={'Value': 'Total Revenue'},
             color='Category',
             color_continuous_scale=px.colors.sequential.Plasma)

# Display the bar chart in Streamlit
st.plotly_chart(fig)


import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Sidebar filter for Import/Export selection (with unique key)
transaction_type = st.selectbox('Select Transaction Type:', 
                                ['Both', 'Import', 'Export'], 
                                key='transaction_type_selectbox')

# Filter the data based on the selected transaction type
if transaction_type == 'Import':
    filtered_data = sdset[sdset['Import_Export'] == 'Import']
elif transaction_type == 'Export':
    filtered_data = sdset[sdset['Import_Export'] == 'Export']
else:
    filtered_data = sdset

# Group by country and sum the revenue (Value)
top_countries = filtered_data.groupby('Country')['Value'].sum().reset_index()
top_countries = top_countries.sort_values(by='Value', ascending=False).head(10)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.barh(top_countries['Country'], top_countries['Value'], color='green')

ax.set_ylabel('Country')
ax.set_xlabel('Total Revenue')
ax.set_title(f'Top 10 Trading Countries by Revenue ({transaction_type})')

# Add labels on the bars
for bar in bars:
    xval = bar.get_width()
    ax.text(xval, bar.get_y() + bar.get_height()/2, f'{xval:.0f}', va='center', ha='left')

# Display the plot in Streamlit
st.pyplot(fig)




import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Group by Shipping Method, Import/Export, and Product Category
shipping_data = sdset.groupby(['Shipping_Method', 'Import_Export', 'Category']).size().reset_index(name='Count')

# Add dropdowns to select filters
import_export_options = shipping_data['Import_Export'].unique()
selected_import_export = st.selectbox('Select Import/Export Category:', ['All'] + list(import_export_options))

product_category_options = shipping_data['Category'].unique()
selected_product_category = st.selectbox('Select Product Category:', ['All'] + list(product_category_options))

# Filter data based on the selected options
filtered_data = shipping_data

if selected_import_export != 'All':
    filtered_data = filtered_data[filtered_data['Import_Export'] == selected_import_export]

if selected_product_category != 'All':
    filtered_data = filtered_data[filtered_data['Category'] == selected_product_category]

# Create a sunburst chart using Plotly Express
fig = px.sunburst(
    filtered_data,
    path=['Import_Export', 'Category', 'Shipping_Method'],  # Path includes both categories and shipping method
    values='Count',
    title='Most Used Shipping Method (By Category)',
    color='Count',
    color_continuous_scale='Blues'
)

# Display the plot in Streamlit
st.plotly_chart(fig)

