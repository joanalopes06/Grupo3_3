# -*- coding: utf-8 -*-

from flask import render_template, session 
from classes.tournament import Tournament
from datafile import filename 

import pandas as pd 
from sqlalchemy import create_engine 
import plotly.express as px 

def apps_plotly():
    engine = create_engine("sqlite:///" + filename + "Grupo3.db")
    df_orderproduct = pd.read_sql("Game", con = engine)
    result = df_orderproduct.groupby("tournaments_id")["id"].count()
    p_ids = result.index
    p_names =[]
    print(Tournament.lst)
    print(p_ids)
    print(result.values)
    for p_id in p_ids:
        print('p_id',p_id)
        print(Tournament.obj[p_id])
        p_obj = Tournament.obj[p_id]
        p_names.append(p_obj.tournament_name)
    quantities = result.values 
    print('p_names:',p_names)
    print(quantities)
    fig = px.bar(x=p_names, y=quantities, labels={"x": "Tournament name", "y": "Number of games"}, title="Total of games per Tournament", color_discrete_sequence=["#F1948A"])
    plot_div = fig.to_html(full_html=False, div_id="my-plot")
    return render_template("plotly.html", plot_div=plot_div, ulogin=session.get("user"))
