#importing modules
import pandas as pd
import plotly.figure_factory as ff

#reading the csv
df = pd.read_csv("data.csv")

#creating graph
fig = ff.create_distplot([df["Rating"].tolist()], ["Ratings"], show_hist=False)

#showing the graph
fig.show()