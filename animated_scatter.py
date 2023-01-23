"""
Let's plot an animated chart with Python and Plotly

Has this technique ever been used in the wild? Yes.
https://www.gov.uk/government/collections/data-visualisations

We'll cover:
    
    - Creating a simple animated chart 
    - Styling the chart
    - Embedding the chart into a live web page 
"""

import plotly.express as px


df = px.data.gapminder()


fig = px.scatter(df, 
                 x="gdpPercap", 
                 y="lifeExp", 
                 animation_frame="year", 
                 animation_group="country",
                 size="pop", 
                 color="continent", 
                 hover_name="country",
                 log_x=True,
                 size_max=55, 
                 range_x=[100,100000], 
                 range_y=[25,90])

fig.add_hline(y=72, 
              line_width=2, 
              line_dash='dash', 
              line_color='lightgray',
              annotation_text='',
              annotation_font=dict(
                family="Arial",
                size=15,
                color="lightgray"
               ),
               annotation_font_size=15,
               annotation_position='bottom left',
               fillcolor='lightgray')

fig.add_shape(type="line",
              x0=12000, 
              y0=0, 
              x1=12000, 
              y1=100,
              line_width=2,
              line_color='lightgray',
              line_dash='dash')

fig.add_annotation(x=0.15,
                   xref='paper',
                   yref='paper',
                   xanchor='left',
                   y=0.15,
                   yanchor='top',
                   text="Below average",
                   font=dict(
                        color="black",
                        size=20,
                        family="Arial"
                    ),
                    showarrow=False)

fig.add_annotation(x=0.85,
                   xref='paper',
                   yref='paper',
                   xanchor='left',
                   y=0.95,
                   yanchor='top',
                   text="Above average",
                   font=dict(
                        color="black",
                        size=20,
                        family="Arial"
                    ),
                    showarrow=False)


fig.add_annotation(x=.99,
                   xref='paper',
                   xanchor='right',
                   y=27,
                   yanchor='bottom',
                   text="<b>Data last updated 2008</b>",
                   font=dict(
                       color="gray",
                       size=14
                   ),
                   showarrow=False)


fig.update_layout(
        title="Global life expectancy and GDP per capita over time.",
        xaxis_title="GDP per capita",
        yaxis_title="Life expectancy",
        legend_title="Legend Title",
        showlegend=False,
        font=dict(
            family="Arial",
            size=14
        ),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)')


fig.write_html("outputs/animated_scatter.html")