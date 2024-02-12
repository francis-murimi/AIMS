import dash
from dash import dcc, html
from django_plotly_dash import DjangoDash
import plotly.express as px

from django_pandas.io import read_frame

from farm.models import Farm

# Preparing your data for usage *******************************************
farm_qs = Farm.objects.all()
farm_df = read_frame(farm_qs, fieldnames=['code', 'location__name','location__ward__name','size',
                                          'water_source__name','water_source__water_type','water_source__water_source_type',
                                          'water_source__is_seasonal','water_source__water_capacity','water_source__is_shared',
                                          'water_source__is_dry','soil__texture','soil__color','soil__depth','soil__structure',
                                          'soil__porosity','soil__stone_content','soil__acidity_level','slope'])

def get_farm_df():
    farm_qs = Farm.objects.all()
    farm_df = read_frame(farm_qs, fieldnames=['code', 'location__name','location__ward__name','size',
                                          'water_source__name','water_source__water_type','water_source__water_source_type',
                                          'water_source__is_seasonal','water_source__water_capacity','water_source__is_shared',
                                          'water_source__is_dry','soil__texture','soil__color','soil__depth','soil__structure',
                                          'soil__porosity','soil__stone_content','soil__acidity_level','slope'])
    return farm_df

stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = DjangoDash('FarmDash')


app.layout = html.Div([
    html.H1(children="Farm Analytics", className="row", style={"textAlign": "center"}),
    
    # Dropdown menu
    html.Div([
        html.Div(dcc.Dropdown(
            id="ward-farm-size",
            multi=True,
            options=[
                {"label": x, "value": x}
                for x in sorted(farm_df["location__ward__name"].unique())
            ],
            #value=["HR",],
        ), className="four columns"),  
    ], className="row"),
    
    # Graph
    html.Div(dcc.Graph(id="ward-farm-size-chart", figure={}), className="row"),
], style={'padding': '20px', 'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#f0f0f0'})

# App Callbacks **************************************************************
@app.callback(
    dash.dependencies.Output(component_id="ward-farm-size-chart", component_property="figure"),
    [dash.dependencies.Input(component_id="ward-farm-size", component_property="value")], 
)
def update_ward_farm_size_chart(chosen_value):
    farm_df = get_farm_df()
    farm_df = farm_df.groupby('location__ward__name')['size'].sum().reset_index()


    if len(chosen_value) == 0:
        return {}
    else:
        farm_df_filtered = farm_df[farm_df["location__ward__name"].apply(lambda x: x in chosen_value)]

        fig = px.bar(
            data_frame=farm_df_filtered,
            x="location__ward__name",
            y="size",
            color="location__ward__name",
            log_y=True,
            labels={
                "location__ward__name": "Ward",
                "size": "Size",
            },
            hover_data=["size"],
        )
        return fig

@app.callback(
    dash.dependencies.Output(component_id="ward-farm-size", component_property="options"),
    [dash.dependencies.Input(component_id="ward-farm-size", component_property="value")], 
)
def update_dropdown_options(n):
    farm_df = get_farm_df()
    options = [{"label": x, "value": x} for x in sorted(farm_df["location__ward__name"].unique())]
    return options