import pandas as pd

netflix_titles = pd.read_csv('dataset/netflix_titles.csv')

filtro_filme = (netflix_titles['release_year'] >= 2000) & (netflix_titles['type'] == 'Movie')

df_filtrado = netflix_titles[filtro_filme]

df_filtrado['director'] = df_filtrado['director'].fillna("")

print(df_filtrado)

print(df_filtrado.count().T)