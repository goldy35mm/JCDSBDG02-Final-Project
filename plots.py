import plotly
import plotly.graph_objects as go
from cleaning_data import data_loans, new_data_loans
import json
import plotly.express as px

def graph1():
    ff = data_loans()
    fig = px.scatter(ff, x="Annual Income", y="Monthly Debt", color="Monthly Debt", hover_data=['Current Loan Amount'], size='Monthly Debt')
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def graph2():
    ff = data_loans()
    fig = px.pie(ff, values="Credit Score", names="Purpose")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json

def graph3():
    ff = data_loans()

    
    p = ff['Purpose'].unique()
    c = ff['Credit Score'].value_counts()
    a = ff['Annual Income']

    fig = go.Figure()
    fig.add_trace(go.Bar(
        x= p,
        y= c,
        name='Credit Score',
        marker_color='indianred'
    ))
    fig.add_trace(go.Bar(
        x=p,
        y=a,
        name='Annual Income',
        marker_color='lightsalmon'
    ))

    # Here we modify the tickangle of the xaxis, resulting in rotated labels.
    fig.update_layout(barmode='group', xaxis_tickangle=-45)




    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json



def graph4():
    ff = data_loans()
    fig = px.pie(ff, values="Credit Score", names="Home Ownership")
    fig_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return fig_json