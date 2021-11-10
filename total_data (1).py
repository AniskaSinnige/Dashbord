#!/usr/bin/env python
# coding: utf-8




# In[2]:


import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
import json
import requests
import streamlit as st
from PIL import Image




# In[4]:


China = pd.read_csv('China.csv')
Bangladesh = pd.read_csv('Bangladesh.csv')
Brazil = pd.read_csv('Brazil.csv')
DRCongo = pd.read_csv('DR Congo.csv')
Egypt = pd.read_csv('Egypt.csv')
Ethiopia = pd.read_csv('Ethiopia.csv')
France = pd.read_csv('France.csv')
Germany = pd.read_csv('Germany.csv')
India = pd.read_csv('India.csv')
Indonasia = pd.read_csv('Indonasia.csv')
Iran = pd.read_csv('Iran.csv')
Italy = pd.read_csv('Italy.csv')
Japan = pd.read_csv('Japan.csv')
Mexico = pd.read_csv('Mexico.csv')
Nigeria = pd.read_csv('Nigeria.csv')
Pakistan = pd.read_csv('Pakistan.csv')
Philippines = pd.read_csv('Philippines.csv')
Russia = pd.read_csv('Russia.csv')
SouthAfrica = pd.read_csv('South Africa.csv')
Tanzania = pd.read_csv('Tanzania.csv')
Thailand = pd.read_csv('Thailand.csv')
Turkey = pd.read_csv('Turkey.csv')
UnitedKingdom = pd.read_csv('United Kingdom.csv')
USA = pd.read_csv('USA.csv')
Vietnam = pd.read_csv('Vietnam.csv')


# In[5]:


#sidebar info
st.set_page_config(layout='wide')
rad = st.sidebar.radio(options=('Home', 'Population', 'Density (P/Km²)', 'Migrants', 'Age', 'map'), label='Select Categorie')
st.sidebar.markdown('#')
st.sidebar.markdown('#')
st.sidebar.subheader('Gemaakt Door:')
st.sidebar.write('• Karlijn Huissen 500889478')
st.sidebar.write('• Aniska Sinnige 500823214')


# In[6]:


if rad =='Home':
    st.title('Dashboard Population Worldwide')
    img = Image.open("foto.png")
    st.image(img, width=800)


# In[7]:


if rad =='Population':
    st.header('Population')
    st.markdown('#')
    st.subheader('Population of different countries')
    'Onderstaande afbeelding geeft de populatie van een aantal landen weer de jaren 1980, 2000, 2020.'
    
    population800020 = pd.read_csv('PopulationWorld20.00.80.csv')
    
    fig=go.Figure(data=[
    go.Bar(name='1980', x=population800020['ADMIN'], y=population800020['population1980'], marker_color=px.colors.qualitative.Light24[9]),
    go.Bar(name='2000', x=population800020['ADMIN'], y=population800020['populuation2000'], marker_color=px.colors.qualitative.Light24[17]),
    go.Bar(name='2020', x=population800020['ADMIN'], y=population800020['population2020'], marker_color=px.colors.qualitative.Light24[5])])
    
    fig.update_layout(barmode='group', title='Population per Country in 1980,2000,2020',
                  xaxis_title='Country', 
                  yaxis_title='Population number',
                  legend_title='Year')
    st.plotly_chart(fig)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Brazil')
    
    Brazil1=Brazil[['Year', 'Population']]
    fig1 = px.histogram(Brazil1, x='Year', y='Population', nbins=100, title='Population growth of Brazil per year', color_discrete_sequence=['#EEA6FB'])
    st.plotly_chart(fig1)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('China')
    
    China1= China[['Year', 'Population']]
    fig2 = px.histogram(China1, x='Year', y='Population', nbins=100, title='Population growth of China per year', color_discrete_sequence=['#22FFA7'])
    st.plotly_chart(fig2)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Germany')
    
    Germany1= Germany[['Year', 'Population']]
    fig3 = px.histogram(Germany1, x='Year', y='Population', nbins=100, title='Population growth of Germany per year', color_discrete_sequence=['#DC587D'])
    st.plotly_chart(fig3)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Mexico')
    
    Mexico1=Mexico[['Year', 'Population']]
    fig4 = px.histogram(Mexico1, x='Year', y='Population', nbins=100, title='Population growth of Mexico per year', color_discrete_sequence=['#FF9616'])
    st.plotly_chart(fig4)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('South Africa')
    
    SouthAfrica1= SouthAfrica[['Year', 'Population']]
    fig5 = px.histogram(SouthAfrica1, x='Year', y='Population', nbins=100, title='Population growth of South Africa per year', color_discrete_sequence=['#0DF9FF'])
    st.plotly_chart(fig5)


# In[8]:


if rad =='Density (P/Km²)':
    st.header('Density (P/Km²)')
    st.markdown('#')
    'Onderstaande afbeelding geeft de het aantal mensen per vierkante kilometer weer.'
    
    Boxplot_long = pd.read_csv('Boxplot_long.csv')
    
    Country_color_map = {'Brazil': '#EEA6FB', 'China':'#22FFA7', 'Germany':'#DC587D', 'Mexico':'#FF9616', 'South Africa':'#0DF9FF'}
    fig6 = px.box(Boxplot_long, x='Country', y='Density (P/Km²)', color='Country', color_discrete_map=Country_color_map)
    fig6.update_layout(title='Density per Country')
    st.plotly_chart(fig6)


# In[9]:


if rad == 'Migrants':
    st.header('Migrants per country')
    st.markdown('#')
    st.subheader('Brazil')
    
    fig7= px.scatter(Brazil, x='Year', y='Migrants (net)', color_discrete_sequence=['#EEA6FB'], title='Migrants in Brazil', trendline="ols")
    st.plotly_chart(fig7)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('China')
    
    fig8= px.scatter(China, x='Year', y='Migrants (net)', color_discrete_sequence=['#22FFA7'], title='Migrants in China', trendline="ols")
    st.plotly_chart(fig8)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Germany')
    
    fig9= px.scatter(Germany, x='Year', y='Migrants (net)', color_discrete_sequence=['#DC587D'], title='Migrants in Germany', trendline="ols")
    st.plotly_chart(fig9)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Mexico')
    
    fig10= px.scatter(Mexico, x='Year', y='Migrants (net)', color_discrete_sequence=['#FF9616'], title='Migrants in Mexico', trendline="ols")
    st.plotly_chart(fig10)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('South Africa')
    
    fig11= px.scatter(SouthAfrica, x='Year', y='Migrants (net)', color_discrete_sequence=['#0DF9FF'], title='Migrants in South Africa', trendline="ols")
    st.plotly_chart(fig11)


# In[10]:


if rad == 'Age':
    st.header('Average age per country')
    st.markdown('#')
    st.subheader('Brazil')
    
    fig12 = px.scatter(Brazil, x="Year", y="Median Age", trendline="ols", title=' Average age per year in Brazil', color_discrete_sequence=['#EEA6FB'])
    fig12.add_annotation(x=1990, y=24.2, text='R^2 = 0.94')
    st.plotly_chart(fig12)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('China')
    
    fig13 = px.scatter(China, x="Year", y="Median Age", trendline="ols", title=' Average age per year in China', color_discrete_sequence=['#22FFA7'])
    fig13.add_annotation(x=1990, y=27.5, text='R^2 = 0.91')
    st.plotly_chart(fig13)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Germany')
    
    fig14 = px.scatter(Germany, x="Year", y="Median Age", trendline="ols", title=' Average age per year in Germany', color_discrete_sequence=['#DC587D'])
    fig14.add_annotation(x=1990, y=39.5, text='R^2 = 0.93')
    st.plotly_chart(fig14)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('Mexico')
    
    fig15 = px.scatter(Mexico, x="Year", y="Median Age", trendline="ols", title=' Average age per year in Mexico', color_discrete_sequence=['#FF9616'])
    fig15.add_annotation(x=1990, y=21.7, text='R^2 = 0.91')
    st.plotly_chart(fig15)
    ##############################################################################################################
    st.markdown('#')
    st.subheader('South Africa')
    
    fig16 = px.scatter(SouthAfrica, x="Year", y="Median Age", trendline="ols", title=' Average age per year in South Africa', color_discrete_sequence=['#0DF9FF'])
    fig16.add_annotation(x=1990, y=22.2, text='R^2 = 0.81')
    st.plotly_chart(fig16)


# In[11]:


if rad == 'Map':
    st.header('Overview population worldwide')
    st.markdown('#')

    df1= pd.read_csv('PopulationWorld20.00.80.csv')
    df1.rename(columns={'ADMIN':'Country'}, inplace=True)

    df2= gpd.read_file('countries.geojson')
    df2.rename(columns={'ADMIN':'Country'}, inplace=True)

    base_url = 'https://countriesnow.space/api/v0.1/countries/positions'
    response = requests.get(base_url)
    j = response.json()

    df3 = pd.DataFrame(j)
    df4=df3['data'].apply(pd.Series)
    df4.rename(columns={'name':'Country'}, inplace=True)

    df5 = df1.merge(df4, on='Country', how='inner')
    df6 = df5.assign(location=df5[['lat','long']].values.tolist())
    df6.rename(columns={'ADMIN':'Country'}, inplace=True)
    df6.rename(columns={'population1980':'population'}, inplace=True)
    
    fig17 = px.choropleth_mapbox(df6, geojson=df2, color='population', locations='Country', center={"lat": 0, "lon":0 },
                           mapbox_style="carto-positron", zoom=0, featureidkey="properties.Country", hover_name='Country', 
                           hover_data=['long', 'lat'])


    button1 =  dict(method = "update",
                args = [{'z': [ df6['population']]}, {'visible': [ True, False, False]}],
                label = "Population1980")
    button2 =  dict(method = "update",
                args = [{'z': [ df6['populuation2000']]}, {'visible': [ False, True, False]}],
                label = "Population 2000")
    button3 =  dict(method = "update",
                args = [{'z': [ df6['population2020']]}, {'visible': [ False, False, True]}],
                label = "Population 2020")

    fig17.update_layout(margin={"r":0,"t":0,"l":0,"b":0})


    fig17.update_layout({'updatemenus':[{'type': 'dropdown', 'showactive': True, 'active': 0,
                                   'buttons': [button1, button2, button3]}]})

    st.plotly_chart(fig17)

