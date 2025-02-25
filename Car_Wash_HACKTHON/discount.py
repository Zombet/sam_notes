import pandas as pd
import plotly.graph_objects as go

pastel_colors = [
    '#A6CEE3', '#B2DF8A', '#FB9A99', '#FDBF6F', 
    '#CAB2D6', '#FFFF99', '#1F78B4', '#33A02C', 
    '#E31A1C', '#FF7F00', '#6A3D9A', '#B15928'
]

file_path = r"C:\Users\sadiq\OneDrive\Desktop\samsung\sam_notes\Car_Wash_HACKTHON\car_wash_datasetcsv.csv"
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    print("File not found. Please check the file path.")
    exit()


discount_counts = df['Discount (%)'].value_counts().reset_index()
discount_counts.columns = ['Discount (%)', 'Number of People']

# Sort by discount percentage for better visualization
discount_counts = discount_counts.sort_values(by='Discount (%)')

# Create a donut chart
fig = go.Figure(data=[go.Pie(
    labels=discount_counts['Discount (%)'].astype(str) + '%',  # Labels for each slice
    values=discount_counts['Number of People'],  # Size of each slice
    hole=0.6,  # Creates a donut chart
    marker=dict(colors=pastel_colors)  # Use a pastel color palette
)])

# Add title and center text
fig.update_layout(
    title_text="Distribution of Discount Percentages",
    title_font_size=20,
    annotations=[dict(
        text="Discounts",
        x=0.5,
        y=0.5,
        font_size=16,
        font_color='black',
        showarrow=False
    )],
    showlegend=True
)


fig.show()
