#Imports e leitura do arquivo csv
import sys
import matplotlib

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('netflix_titles.csv')

#Funcao do grafico histograma
def graf_hist(x,titulo, nome):
    # Fill NaN values with 0 and then extract numeric values and convert to integers
    df[nome] = df[nome].fillna('0').str.extract('(\d+)').astype(int)
    
    fig, ax = plt.subplots()
    df[nome].plot(kind='hist', bins=10)  # You can adustj the number of bins as needed
    ax.set_title(titulo)
    plt.xlabel(x)
    plt.ylabel('Frequência')
    plt.show()
  
#Funcao do grafico horizontal
def graf_h(yLabel,titulo,x, y, fig_height, fontsz):
    plt.figure(figsize=(15, fig_height))
    plt.barh(x, y)
    plt.xlabel('Contagem')
    plt.ylabel(yLabel)
    plt.title(titulo)
    plt.gca().invert_yaxis()
    plt.yticks(fontsize=fontsz)
    plt.show()



#Analises


#Primeira analise

# Obtém uma série (coluna) com os países
countries_column = df['country']

# Cria um dicionário para armazenar a contagem de cada país
country_count = {}

# Itera sobre os valores da coluna "country"
for country in countries_column:
    if not pd.isna(country):
        # Remove os colchetes e as aspas simples dos valores da coluna "country"
        country = country.strip("[]' ")  # Remove [ ], ' ' from country names
        # Divide os valores da coluna "country" quando houver vírgulas
        country_list = country.lower().split(',')
        for c in country_list:
            if c.strip():  # This checks if the country name is not empty after stripping
                if c in country_count:
                    country_count[c] += 1
                else:
                    country_count[c] = 1

# Ordena os países pelo número de ocorrências em ordem decrescente
sorted_countries = sorted(country_count.items(), key=lambda x: x[1], reverse=True)
# Extrai os nomes dos países e suas contagens
country_names = [country[0].strip() for country in sorted_countries]
country_counts = [country[1] for country in sorted_countries]
num_countries = len(country_names)
fig_height = max(5, num_countries * 0.3)

#Segunda analise

rating_column = df['rating']

unique_rating = set()

for rating in rating_column:
    if not pd.isna(rating):
        rating_list = country.split(', ')
        unique_rating.update(rating_list)
        

rating_counts = {}

for rating in rating_column:
    if not pd.isna(rating):
        rating_list = rating.split(', ')
        for r in rating_list:
            if r in rating_counts:
                rating_counts[r] += 1
            else:
                rating_counts[r] = 1
ratings = list(rating_counts.keys())
counts = [rating_counts[r] for r in ratings]

#Terceira analise

# Get the 'listed_in' column
listed_in_column = df['listed_in']

# Initialize lists to store genres and their counts
genres = []
genre_counts = []

# Iterating over the values in the 'listed_in' column and count genres
for listed_in in listed_in_column:
    if not pd.isna(listed_in):
        listed_genres = [genre.strip() for genre in listed_in.split(',')]
        for genre in listed_genres:
            if genre in genres:
                index = genres.index(genre)
                genre_counts[index] += 1
            else:
                genres.append(genre)
                genre_counts.append(1)

# Sort the genre counts and genres in descending order
sorted_indices = sorted(range(len(genre_counts)), key=lambda i: genre_counts[i], reverse=True)
top_10_genres = [(str(genres[i]), genre_counts[i]) for i in sorted_indices[:10]]

#Quarta analise

# Sort the genre counts and genres in descending order
sorted_indices = sorted(range(len(genre_counts)), key=lambda i: genre_counts[i], reverse=True)
top_10_genres = [(str(genres[i]), genre_counts[i]) for i in sorted_indices[:10]]

# Filtra apenas as linhas que têm informações de ano de lançamento
df = df.dropna(subset=['release_year'])

# Converte a coluna 'release_year' para números inteiros
df['release_year'] = df['release_year'].astype(int)

# Conta a quantidade de filmes lançados por ano
movies_per_year = df['release_year'].value_counts().sort_index()

# Get the top 10 years with the most movies released
top_10_years = movies_per_year.nlargest(10)


#Mostra os graficos


graf_hist("Duração","Gráfico de Duração", "duration")

graf_h("Países","Contagem de Países",country_names, country_counts, fig_height,5)

graf_h("Ratings","Gráfico de Ratings",ratings,counts, 20, 10)

graf_h("Gênero","Top 10 Gêneros foda", [genre for genre, _ in top_10_genres], [count for _, count in top_10_genres], 20, 10)

graf_h("Ano de Lançamento","Top 10 Anos com Maior Número de Filmes Lançados", top_10_years.index.astype(str), top_10_years.values, 20, 10)
