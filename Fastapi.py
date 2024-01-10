
import pandas as pd

# Lectura y preprocesamiento de steam_games
steam_games = pd.read_csv("D:\\Users\\Cesar\\Desktop\\Proyecto_individial_1\\Data_ingeneria\\ETL\\steam_games_ETL")
steam_games.replace({None: pd.NA}, inplace=True)
steam_games.to_csv("steam_games.csv", index=False)

# Lectura y preprocesamiento de users_reviews
users_reviews = pd.read_parquet("D:\\Users\\Cesar\\Desktop\\Proyecto_individial_1\\Data_ingeneria\\ETL\\users_reviews_ETL")
users_reviews.replace({None: pd.NA}, inplace=True)
users_reviews.to_parquet("users_reviews.parquet", index=False)

# Lectura y preprocesamiento de users_items
users_items = pd.read_parquet("D:\\Users\\Cesar\\Desktop\\Proyecto_individial_1\\Data_ingeneria\\ETL\\users_items_ETL")
users_items.replace({None: pd.NA}, inplace=True)
users_items.to_parquet("users_items.parquet", index=False)

def PlayTimeGenre(genero: str):
    df = steam_games[steam_games["genres"].apply(lambda x: genero in x if isinstance(x, list) else False)]
    df = pd.merge(df, users_items, on='item_id', how='inner')
    df2 = df.groupby('release_year')['playtime_forever'].sum()
    df2 = df2.sort_values(ascending=False)
    df3 = df2.reset_index()
    df4= df3.drop('playtime_forever', axis=1)
    año = df4.iloc[0, 0]
    return {"genero": genero, "año": año}

def UsersRecommend( año : int ):
    juegos_del_año = steam_games[steam_games["release_year"] == año]
    df = pd.merge(juegos_del_año, users_reviews, on='item_id', how='inner')
    df2 = df[df['recommend'] == False]
    df3 = df2.groupby("app_name")['recommend'].count()
    df3 = df3.sort_values(ascending=False)
    df4=df3.tail(3)
    df5 = df4.reset_index()
    df5.drop('recommend', axis=1)
    df5
    puesto1 = df5.iloc[0, 0]
    puesto2 = df5.iloc[1,0 ]
    puesto3= df5.iloc[2,0 ]
    lista_resultados = [
    {"puesto1": puesto1},
    {"puesto2": puesto2},
    {"puesto3": puesto3}
    ]
    return lista_resultados


def UsersWorstDeveloper(año: int):
    
    juegos_del_año = steam_games[steam_games["release_year"] == año]
    df = pd.merge(juegos_del_año, users_reviews, on='item_id', how='inner')
    df2 = df[df['recommend'] == False]
    df3 = df2.groupby("publisher")['recommend'].count()
    df4 = df3.sort_values(ascending=False).head(3)
    df5 = df4.reset_index()
    df5.drop('recommend', axis=1)
    puesto1 = df5.iloc[0, 0]
    puesto2 = df5.iloc[1,0 ]
    puesto3= df5.iloc[2,0 ]
    lista_resultados = [
    {"puesto1": puesto1},
    {"puesto2": puesto2},
    {"puesto3": puesto3}
    ]
    return lista_resultados


print(PlayTimeGenre("Simulation"))




