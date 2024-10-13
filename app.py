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

# Group by Import_Export column and sum the Value
revenue_data = sdset.groupby('Import_Export')['Value'].sum().reset_index()

# Add a dropdown to filter by Import, Export, or Both
options = ['Both', 'Imports', 'Exports']
selected_option = st.selectbox('Select Category:', options)

# Filter data based on the selection
if selected_option == 'Imports':
    revenue_data = revenue_data[revenue_data['Import_Export'] == 'Import']
elif selected_option == 'Exports':
    revenue_data = revenue_data[revenue_data['Import_Export'] == 'Export']

# Calculate the total revenue and percentage if both categories are selected
if selected_option == 'Both':
    total_revenue = revenue_data['Value'].sum()
    revenue_data['Percentage'] = (revenue_data['Value'] / total_revenue) * 100

# Create a donut chart
fig, ax = plt.subplots(figsize=(7, 7))

if selected_option == 'Both':
    # Plot donut chart for both imports and exports
    wedges, texts, autotexts = ax.pie(
        revenue_data['Value'],
        labels=revenue_data['Import_Export'],
        autopct='%1.1f%%',
        startangle=90,
        colors=['blue', 'green'],
        wedgeprops=dict(width=0.3)
    )
else:
    # Plot donut chart for either imports or exports
    wedges, texts, autotexts = ax.pie(
        revenue_data['Value'],
        labels=[selected_option],
        autopct='%1.1f%%',
        startangle=90,
        colors=['blue'] if selected_option == 'Imports' else ['green'],
        wedgeprops=dict(width=0.3)
    )

# Equal aspect ratio ensures the pie chart is drawn as a circle
ax.axis('equal')

# Set the title dynamically based on the selected option
ax.set_title(f'Total Revenue from {selected_option}')

# Display the plot in Streamlit
st.pyplot(fig)



import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Group by customer and sum the value for all customers
all_customers = sdset.groupby('Customer')['Value'].sum().reset_index()

# Sort customers by revenue in descending order
all_customers = all_customers.sort_values(by='Value', ascending=False)

# Add a slider to select the number of customers to display
num_customers = st.slider('Select number of customers to view:', min_value=1, max_value=len(all_customers), value=10)

# Select the top 'num_customers' customers
filtered_customers = all_customers.head(num_customers)

# Create a horizontal bar chart
fig, ax = plt.subplots(figsize=(10, 8))

# Plot horizontal bars
bars = ax.barh(filtered_customers['Customer'], filtered_customers['Value'], color='skyblue')

# Add labels and title
ax.set_xlabel('Total Revenue')
ax.set_ylabel('Customer')
ax.set_title(f'Top {num_customers} Customers by Revenue')

# Display the revenue values on the bars
for bar in bars:
    ax.text(bar.get_width(), bar.get_y() + bar.get_height()/2, f'{bar.get_width():.0f}', va='center')

# Invert the y-axis so the highest value appears at the top
ax.invert_yaxis()

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



import pandas as pd
import streamlit as st
import plotly.express as px

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Sidebar filter for country selection
country_options = sdset['Country'].unique()
selected_country = st.selectbox('Select Country:', ['All'] + list(country_options))

# Filter data based on the selected country
if selected_country != 'All':
    filtered_data = sdset[sdset['Country'] == selected_country]
else:
    filtered_data = sdset

# Count the payment terms
payment_data = filtered_data['Payment_Terms'].value_counts().reset_index()
payment_data.columns = ['Payment_Terms', 'Count']

# Create a pie chart using Plotly Express
fig = px.pie(payment_data, 
             names='Payment_Terms', 
             values='Count', 
             title=f'Most Preferred Payment Terms ({selected_country})', 
             color_discrete_sequence=px.colors.sequential.Plasma)

# Display the pie chart in Streamlit
st.plotly_chart(fig)


import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('Imports_Exports_Dataset.csv')
sdset = df.sample(n=3001, random_state=55051)

# Group by country and sum the value
country_revenue = sdset.groupby('Country')['Value'].sum().reset_index()

# Sort values to display from highest to lowest revenue
country_revenue = country_revenue.sort_values(by='Value', ascending=False)

# Sidebar: Allow the user to select the number of countries to display, or show all
num_countries = st.sidebar.slider('Select the number of countries to display', 
                                  min_value=5, 
                                  max_value=len(country_revenue), 
                                  value=10, 
                                  step=5)

# Display only the selected number of countries or all of them
selected_countries = country_revenue.head(num_countries)

# Plot the data
fig, ax = plt.subplots(figsize=(12, 6))
bars = ax.bar(selected_countries['Country'], selected_countries['Value'], color='green')

ax.set_xlabel('Country')
ax.set_ylabel('Total Revenue')
ax.set_title(f'Top {num_countries} Trading Countries by Revenue')

# Add labels on top of bars
for bar in bars:
    yval = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, yval, f'{yval:.0f}', ha='center', va='bottom')

# Display the plot
st.pyplot(fig)

# Display the data as a table as well
st.dataframe(country_revenue)


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

