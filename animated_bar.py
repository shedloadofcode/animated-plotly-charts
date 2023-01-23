"""
Let's plot an animated chart with Python and Plotly

Has this technique ever been used in the wild? Yes.
https://www.gov.uk/government/collections/data-visualisations

We'll cover:
    
    - Creating a simple animated charts
    - Styling the charts
    - Embedding the chart into a live web page 
"""

import plotly.express as px


df = px.data.gapminder()

fig = px.bar(df, 
             x="continent", 
             y="pop", 
             animation_frame="year", 
             animation_group="country", 
             hover_name="country",
             range_y=[0,4000000000],
             color="continent",
             color_discrete_map={
                'Asia': '#1d70b8',
                'Europe': '#f47738',
                'Africa': '#28a197',
                'Americas': '#6f72af',
                'Oceania': '#d53880'
            })

fig.update_layout(
        title="Global population growth over time.",
        xaxis_title="Continent",
        yaxis_title="Population",
        legend_title="Legend Title",
        showlegend=False,
        font=dict(
            family="Arial",
            size=14
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)')

fig.write_html("outputs/animated_bar.html")