import pandas as pd
import plotly.express as px

file_path = r"C:\Users\sadiq\OneDrive\Desktop\samsung\sam_notes\Car_Wash_HACKTHON\car_wash_datasetcsv.csv"
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()

rev= df.groupby('Service')['Revenue'].sum().reset_index()

rev = rev.sort_values(by='Revenue', ascending=False)

fig = px.bar(
    rev,
    x='Service',
    y='Revenue',
    title="Total Revenue by Service Type",
    labels={'Service': 'Service Type', 'Revenue': 'Total Revenue'},
    text='Revenue',  
    color='Service', 
    color_discrete_sequence=px.colors.qualitative.Pastel  
)

fig.update_traces(texttemplate='%{text:.2f}', textposition='outside')  
fig.update_layout(
    xaxis_title="Service Type",
    yaxis_title="Total Revenue",
    showlegend=False, 
    template="plotly_white",  
    title_font_size=20,
    title_x=0.5 
)


fig.show()

