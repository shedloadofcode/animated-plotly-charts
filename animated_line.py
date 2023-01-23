"""
Let's plot an animated chart with Python and Plotly

Has this technique ever been used in the wild? Yes.
https://www.gov.uk/government/collections/data-visualisations

We'll cover:
    
    - Creating a simple animated charts
    - Styling the charts
    - Embedding the chart into a live web page 
"""

import plotly.graph_objects as go
import pandas as pd

dates = ["2022-12-03", "2022-12-04", "2022-12-05", "2022-12-06", "2022-12-07", "2022-12-08", "2022-12-09"]
school_a = [86.77, 80.74, 79.48, 76.47, 75.44, 74.49, 70.41]
school_b = [92.77, 91.64, 90.68, 92.37, 92.84, 90.29, 92.71]

df = pd.DataFrame(list(zip(dates, school_a, school_b)),
                  columns=['date', 'school_a', 'school_b'])

fig = go.Figure(
    layout=go.Layout(
        updatemenus=[dict(type="buttons", direction="right", x=0.9, y=1.16), ],
        xaxis=dict(range=["2022-12-02", "2022-12-10"],
                   autorange=False, tickwidth=2,
                   title_text="Time"),
        yaxis=dict(range=[0, 100],
                   autorange=False,
                   title_text="Price")
    ))

# Add traces
i = 1

fig.add_trace(
    go.Scatter(x=df.date[:i],
               y=df.school_a[:i],
               name="School A",
               visible=True,
               line=dict(color="#f47738", dash="dash")))

fig.add_trace(
    go.Scatter(x=df.date[:i],
               y=df.school_b[:i],
               name="School B",
               visible=True,
               line=dict(color="#1d70b8", dash="dash")))

# Animation
fig.update(frames=[
    go.Frame(
        data=[
            go.Scatter(x=df.date[:k], y=df.school_a[:k]),
            go.Scatter(x=df.date[:k], y=df.school_b[:k])]
    )
    for k in range(i, len(df) + 1)])

fig.update_xaxes(ticks="outside", tickwidth=2, tickcolor='white', ticklen=10)
fig.update_yaxes(ticks="outside", tickwidth=2, tickcolor='white', ticklen=1)
fig.update_layout(yaxis_tickformat=',')
fig.update_layout(legend=dict(x=0, y=1.1), legend_orientation="h")

# Buttons
fig.update_layout(title="Attendance % of two schools over time.",
                  xaxis_title="Date",
                  yaxis_title="Attendance %",
                  legend_title="Legend Title",
                  showlegend=False,
                  font=dict(
                      family="Arial",
                      size=14
                  ),
                  paper_bgcolor='rgba(0,0,0,0)',
                  plot_bgcolor='rgba(0,0,0,0)',
                  hovermode="x",
                  updatemenus=[
                        dict(
                            buttons=list([
                                dict(label="Play",
                                     method="animate",
                                     args=[None, {"frame": {"duration": 500}}]),
                                dict(label="School A",
                                     method="update",
                                     args=[{"visible": [False, True]},
                                           {"showlegend": True}]),
                                dict(label="School B",
                                     method="update",
                                     args=[{"visible": [True, False]},
                                          {"showlegend": True}]),
                                dict(label="All",
                                     method="update",
                                     args=[{"visible": [True, True, True]},
                                          {"showlegend": True}]),
                            ]))
                        ]
                    )

fig.write_html("outputs/animated_line.html")