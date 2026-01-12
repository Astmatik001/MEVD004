import dash
from dash import dcc, html
import plotly.express as px
import pandas as pd

df = pd.read_csv('high_popularity_spotify_data.csv')
data = df.copy()

data['track_album_release_date'] = pd.to_datetime(
    data['track_album_release_date'],
    errors='coerce'
)
data['year'] = data['track_album_release_date'].dt.year
data['duration_min'] = data['duration_ms'] / 60000

fig_genre = px.box(
    data,
    x='playlist_genre',
    y='track_popularity',
    title='Популярность треков по жанрам'
)

fig_energy = px.scatter(
    data,
    x='energy',
    y='track_popularity',
    opacity=0.5,
    title='Связь энергии и популярности'
)

fig_duration = px.scatter(
    data,
    x='duration_min',
    y='track_popularity',
    opacity=0.5,
    title='Связь длины и популярности'
)

app = dash.Dash(__name__)

app.layout = html.Div(
    style={'padding': '20px'},
    children=[
        html.H1('Музыкальные треки и популярность'),

        dcc.Graph(figure=fig_genre),
        dcc.Graph(figure=fig_energy),
        dcc.Graph(figure=fig_duration)
    ]
)

if __name__ == '__main__':
    app.run(debug=True)