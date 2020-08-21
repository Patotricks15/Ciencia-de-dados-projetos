import pandas as pd

df_anime = pd.read_csv('anime.csv')
df_notas = pd.read_csv('rating.csv')

df = pd.merge(df_notas, df_anime.drop('rating', axis=1), on='anime_id')

df.groupby('name')['rating'].count().sort_values(ascending=False).head(10)

notas = pd.DataFrame(df.groupby('name')['rating'].mean())
notas['numero de avaliações'] = pd.DataFrame(df.groupby('name')['rating'].count())
notas['avaliação média'] = pd.DataFrame(df.groupby('name')['rating'].mean().round(2))

genero = pd.DataFrame(data=df_anime[['name', 'genre']])
genero.set_index('name', inplace=True)


def verificar_genero(lista_genero, string):
    if any(x in string for x in lista_genero):
        return True
    else:
        return False

def recomendar_anime(nome_do_anime, n):
    genero_anime = genero.loc[nome_do_anime].values[0].split(', ')
    cols = df_anime[df_anime['genre'].apply(lambda x: verificar_genero(genero_anime, str(x)))]['name'].tolist()
    matriz_de_animes = df[df['name'].isin(cols)].pivot_table(index='user_id', columns='name', values='rating')
    anime_nota = matriz_de_animes[nome_do_anime]
    anime_parecido = matriz_de_animes.corrwith(anime_nota)
    anime_correlacionado = pd.DataFrame(anime_parecido, columns=['correlação'])
    anime_correlacionado = anime_correlacionado.join(notas[['numero de avaliações', 'avaliação média']])
    anime_correlacionado.dropna(inplace=True)
    animes_recomendados = anime_correlacionado[anime_correlacionado['numero de avaliações'] > 3000].sort_values(
        'correlação', ascending=False)
    animes_recomendados = animes_recomendados.rename_axis('Animes recomendados')
    print(f'Anime escolhido: {nome_do_anime}')
    return animes_recomendados.head(n + 1)


recomendar_anime(nome_do_anime, 5)
