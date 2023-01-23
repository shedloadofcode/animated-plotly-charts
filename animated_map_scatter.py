"""
Let's plot an animated map with Python and Plotly

We'll cover:
    
    - Creating a simple animated charts
    - Styling the charts
    - Embedding the chart into a live web page 
"""

import pandas as pd
import plotly.express as px
import numpy as np
import json


df = pd.read_csv('clean_crime_records.csv', 
                 parse_dates={'Date':['YEAR', 'MONTH']}, 
                 keep_date_col=True)

df = df[(df['LATITUDE'] != 0) & (df['LONGTITUDE'] != 0)]

sample_df = df.sample(2000, random_state = 42)
    
token = 'pk.eyJ1IjoibHJzcGVuY2VyIiwiYSI6ImNqeWhseHc5dDAweWMzY3FqZGJrdWJnZ2YifQ.TnjuDuRB6KfCreibBqnBaw'
px.set_mapbox_access_token(token)

time_col = 'YEAR'

fig = px.scatter_mapbox(sample_df,
          lat="LATITUDE" ,
          lon="LONGTITUDE",
          hover_name="TYPE",
          color="TYPE",
          animation_frame=time_col,
          mapbox_style='carto-positron',
          category_orders={
              time_col:list(np.sort(sample_df[time_col].unique()))
          },                  
          zoom=10)


fig.write_html("animation.html")