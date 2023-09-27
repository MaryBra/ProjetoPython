#Importando a biblioteca pandas para o sistema
import pandas as pd

#Lê o arquivo CSV
df = pd.read_csv("netflix_titles.csv", encoding="UTF-8")
#Loop Principal
while True:
    #Valor de entrada do menu
    entrada = int(input("\nMENU \n1-Análise do numero de filmes e series feitos por cada pais \n2-Análise das classificações indicativas dos filmes e séries \n3-Análise do tempo de cada filme listados em ordem crescente \n4-Análise dos 10 gêneros mais populares da netflix \n5-Análise da quantidade de filmes feitos por ano"))

    if entrada == 1:
        #Obtém umacoluna com os países da tabela
        countries_coluna = df['country']

        #Cria um conjunto para armazenar países únicos
        unique_countries = set()

        #Itera sobre os valores da coluna country
        for country in countries_coluna:
            #Verifica se country não é um valor nulo 
            if not pd.isna(country):
            # Divide os valores da coluna "country" quando houver vírgulas
                country_list = country.split(', ')
                #Adiciona os elementos da lista country_list garantindo que apenas valores unicos sejam adicionados
                unique_countries.update(country_list)

        # Exibe a lista de países únicos
        """print("Países que aparecem na tabela:")
        for country in unique_countries:
            print(country)"""

        #Criação do dicionário 
        country_counts={}

        #Loop para contagem de quantas vezes cada pais aparece na tabela
        for country in countries_coluna:
            if not pd.isna(country):
                # Divide os valores da coluna "country" quando houver vírgulas
                country_list = country.split(', ')
                for c in country_list:
                    #Verifica se o pais ja existe no dicionário
                    if c in country_counts:
                        #Se existir, incrementa a contagem em 1
                        country_counts[c] += 1
                    else:
                        #Se não existir cria uma entrada no dicionario com contagem igual a 1
                        country_counts[c] = 1
        # Exibe a contagem de quantas vezes cada país aparece na lista
        for country, count in country_counts.items():
            print(f"{country}: {count} vezes")

    elif entrada == 2:

    #Segunda analise

        #Obtém uma coluna com as classificações da tabela
        rating_coluna = df['rating']

        #Cria um conjunto para armazenar classificações unicas
        unique_class = set()

        #Itera sobre os valores da coluna rating 
        for rating in rating_coluna:
            #Verifica se nao tem valores nulos na coluna rating
            if not pd.isna(rating):
                # Divide os valores da coluna "rating" quando houver vírgulas
                rating_list = rating.split(', ')
                #Adiciona os elementos da lista rating_list garantindo que apenas valores unicos sejam adicionados
                unique_class.update(rating_list)
        
        #Criação do dicionário
        rating_counts = {}

        #Loop para contagem de quantas vezes cada classificação aparece na tabela
        for rating in rating_coluna:
            if not pd.isna(rating):
                rating_list = rating.split(', ')
                for r in rating_list:
                    #Verifica se a classificação ja existe no dicionário                    
                    if r in rating_counts:
                        #Se existir, incrementa a contagem em 1
                        rating_counts[r] += 1
                    else:
                        #Se não existir cria uma entrada no dicionario com contagem igual a 1
                        rating_counts[r] = 1
        # Exibe a contagem de quantas vezes cada país aparece na lista
        for rating, count in rating_counts.items():
            print(f"{rating}: {count} vezes")


    elif entrada == 3:

    #Terceira analise

        # Filtra apenas as linhas que têm informações de duração e o tipo é "Movie"
        movies_df = df[(df['type'] == 'Movie') & (~df['duration'].isna())]
        #Extrai numeros da coluna 'duration' no DataFrame 'movies_df' e converte em valores float
        movies_df['duration'] = movies_df['duration'].str.extract('(\d+)').astype(float)

        # Classifica o DataFrame por duração do menor para o maior
        movies_df = movies_df.sort_values(by='duration', ascending=True)

        # Exibe o tipo, título e duração dos filmes
        for index, row in movies_df.iterrows():
            #print(f"Tipo: {row['type']}")
            print(f"Título: {row['title']}")
            print(f"Duração: {row['duration']} minutos")
            print("-" * 40)


    elif entrada == 4:

    #Quarta analise
        #Importa a classe counter que é usada para contar a ocorrencia de elementos em uma sequencia, como uma lista ou string
        from collections import Counter

        #Obter a coluna 'listed_in'
        listed_in_coluna = df['listed_in']

        #Inicializar um contador para acompanhar a contagem de cada gênero
        genero_counter = Counter()

        #Iterar sobre os valores da coluna 'listed_in' e contar os gêneros
        for listed_in in listed_in_coluna:
            if not pd.isna(listed_in):
                #Divide a string em elementos separados por virgula e aramazena na lista "generos" removendo espaços em branco ao redor de cada elemento
                generos = [genre.strip() for genre in listed_in.split(',')]
                genero_counter.update(generos)

        #Obter os 10 gêneros mais populares em ordem decrescente
        top_10_generos = genero_counter.most_common(10)

        #Exibir os 10 gêneros mais populares
        print("Os 10 gêneros mais populares:")
        for genero, count in top_10_generos:
            print(f"{genero}: {count} vezes")

    elif entrada == 5:
    #Quinta a analise

        #Filtra apenas as linhas que têm informações de ano de lançamento(dropna() elimina as entradas que nao possuem um ano de lancamento definido)
        df = df.dropna(subset=['release_year'])

        #Converte a coluna 'release_year' para números inteiros
        df['release_year'] = df['release_year'].astype(int)

        #Conta a quantidade de filmes lançados por ano
        movies_per_year = df['release_year'].value_counts().sort_index()

        #Exibe a quantidade de filmes lançados por ano
        print("Quantidade de filmes lançados por ano:")
        print(movies_per_year.to_string())
