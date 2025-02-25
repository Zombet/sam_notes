import pandas as pd
import plotly.graph_objects as go


file_path = r"C:\Users\sadiq\OneDrive\Desktop\samsung\sam_notes\Car_Wash_HACKTHON\car_wash_datasetcsv.csv"
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

df['Visit Date'] = pd.to_datetime(df['Visit Date'])


df['Visit Date Only'] = df['Visit Date'].dt.date

revpd = df.groupby('Visit Date Only')['Revenue'].sum()


df['Month'] = df['Visit Date'].dt.to_period('M').astype(str)
revpm = df.groupby('Month')['Revenue'].sum()

df['Year'] = df['Visit Date'].dt.to_period('Y').astype(str)
revpy = df.groupby('Year')['Revenue'].sum()

trace_day = go.Bar(
    x=revpd.index,
    y=revpd.values,
    name="Revenue Per Day",
    marker=dict(color='light steel blue'),
    visible=True 
)

trace_month = go.Bar(
    x=revpm.index,
    y=revpm.values,
    name="Revenue Per Month",
    marker=dict(color='powderblue'),
    visible=False 
)

trace_year = go.Bar(
    x=revpy.index,
    y=revpy.values,
    name="Revenue Per Year",
    marker=dict(color='skyblue'),
    visible=False 
)

layout = go.Layout(
    title="Revenue Analysis Over Time",
    xaxis=dict(title="Time Period"),
    yaxis=dict(title="Revenue"),
    updatemenus=[
        dict(
            type="buttons",
            x=0.1,
            y=1.15,
            buttons=[
                dict(
                    label="Day",
                    method="update",
                    args=[{"visible": [True, False, False]}, {"xaxis.title.text": "Date"}]
                ),
                dict(
                    label="Month",
                    method="update",
                    args=[{"visible": [False, True, False]}, {"xaxis.title.text": "Month"}]
                ),
                dict(
                    label="Year",
                    method="update",
                    args=[{"visible": [False, False, True]}, {"xaxis.title.text": "Year"}]
                )
            ]
        )
    ],
    showlegend=True
)

fig = go.Figure(data=[trace_day, trace_month, trace_year], layout=layout)
fig.show()
