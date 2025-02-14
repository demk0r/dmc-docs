from dash import callback, Input, Output
import dash_mantine_components as dmc
from .data import data

component = dmc.Group(
    [
        dmc.BarChart(
            id="figure-barchart",
            h=300,
            dataKey="month",
            data=data,
            type="stacked",
            series=[
                {"name": "Smartphones", "color": "violet.6"},
                {"name": "Laptops", "color": "blue.6"},
                {"name": "Tablets", "color": "teal.6"},
            ],
            withLegend=True,
            withTooltip=False,
        ),
        dmc.Text(id="clickdata-barchart1"),
        dmc.Text(id="clickdata-barchart2"),
    ]
)

@callback(
    Output("clickdata-barchart1", "children"),
    Output("clickdata-barchart2", "children"),
    Input("figure-barchart", "clickData"),
    Input("figure-barchart", "clickSeriesName"),
)
def update(data, name):
    return f"clickData:  {data}", f"clickSeriesName: {name}"

