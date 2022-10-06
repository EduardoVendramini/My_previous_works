#####################################################################################################
#
# SCRIPT COMPLETO DE FILTRAGEM DE DADOS E ANÁLISE ESTATÍSTICA
#
# Script completo, utilizado para filtragem dos dados e análise estatística (média, desvio padrão e quantidade das amostras por trajeto (origem -> destino))
#
# Data: Março de 2022                           Última atualização: 20 de março de 2022
#####################################################################################################
######################################## FILTRAGEM DOS DADOS ######################################## 
##########################################
#
# SCRIPT PARA FILTRAGEM DOS DADOS
#
# Script utilizado para filtragem dos dados
#
#
##########################################

## Importa os pacotes
import pandas as pd
from geopy.distance import distance
from geopy import Point
## ---

## ----------------- Parâmetros -------------------------- #

## Tempo de deslocamento mínimo de 1 minutos
_TEMPO_DESLOCAMENTO_MINIMO = 1
## Tempo parado máximo de 30 minutos
_TEMPO_PARADO_TRAJETO_MAXIMO = 30
## Velocidade mínima de 10 Km/h
_VELOCIDADE_MEDIA_MINIMA = 10
## Tolerância do desvio padrão de no máximo 30 minutos
_TOLERANCIA_DESVIO= 30.00
## Tolerância da quantidade de amostras para remoção de discprantes
_TOLERANCIA_QTDE_AMOSTRAS = 3
## ------------------------------------------------------ #

# Importa a base de dados
#baseDados_df = pd.read_excel("DadosBase.xlsx")
baseDados_df = pd.read_excel("C:/Users/eduardo/Documents/GitHub/Rotas_Via_Lacteos/src/Script_Analise_Prejuizo/DadosBase_Leite.xlsx")
## ---

## Recebe somente os dados mais importantes da base de dados
baseDados_df = baseDados_df [["ORIGEM_LAT","ORIGEM_LON", "DESTINO_LAT","DESTINO_LON","TEMPO_COLETA_ENTREGA_MIN", "TEMPO_PARADO_TRAJETO_MIN","TEMPO_DESLOCAMENTO_MIN","KM"]]
## ---

## Remove linhas nas quais o deslocamento foi nulo, ou seja, não houve um trajeto
baseDados_df = baseDados_df.loc[(baseDados_df.ORIGEM_LAT != baseDados_df.DESTINO_LAT) & (baseDados_df.ORIGEM_LON != baseDados_df.DESTINO_LON), :]
## ---

## Trunca para cinco casas após a vírgula, os valores das coordenadas
#baseDados_df.update(baseDados_df.iloc[:, 0:].round(4))
baseDados_df.update(baseDados_df.iloc[:, 0:].round(5))
## ---

#### -------------------- Calcula a distância entre os pontos, a distância mínima
baseDados_df["PONTO_ORIGEM"] = baseDados_df.apply(lambda row: Point(latitude=row["ORIGEM_LAT"], longitude=row["ORIGEM_LON"]), axis=1)
baseDados_df["PONTO_DESTINO"] = baseDados_df.apply(lambda row: Point(latitude=row["DESTINO_LAT"], longitude=row["DESTINO_LON"]), axis=1)
baseDados_df["DISTANCIA_KM_CALCULADA"] = baseDados_df.apply(lambda row: distance(row["PONTO_ORIGEM"], row["PONTO_DESTINO"]).km if row["PONTO_DESTINO"] is not None else float("nan"), axis=1)

baseDados_df = baseDados_df.drop("PONTO_ORIGEM", axis=1)
baseDados_df = baseDados_df.drop("PONTO_DESTINO", axis=1)
#### --------------------

## Adiciona coluna de velocidade média
baseDados_df["VELOCIDADE_MEDIA"] = baseDados_df["KM"]/(baseDados_df["TEMPO_DESLOCAMENTO_MIN"]/60)
## ---

## ---------------------- Filtros Parametrizados
baseDados_df = baseDados_df.loc[(baseDados_df.KM > baseDados_df.DISTANCIA_KM_CALCULADA), :]
baseDados_df = baseDados_df.loc[(baseDados_df.TEMPO_DESLOCAMENTO_MIN > _TEMPO_DESLOCAMENTO_MINIMO), :]
baseDados_df = baseDados_df.loc[(baseDados_df.TEMPO_PARADO_TRAJETO_MIN < _TEMPO_PARADO_TRAJETO_MAXIMO), :]
baseDados_df = baseDados_df.loc[(baseDados_df.VELOCIDADE_MEDIA > _VELOCIDADE_MEDIA_MINIMA), :]
#### --------------------




## Filtra somente as colunas úteis para análise estatística
baseDados_resumida_df = baseDados_df[["ORIGEM_LAT","ORIGEM_LON", "DESTINO_LAT", "DESTINO_LON", "VELOCIDADE_MEDIA", "KM", "TEMPO_DESLOCAMENTO_MIN","TEMPO_COLETA_ENTREGA_MIN"]]
## ---

## ------------------ Ordena as linhas, colocando a maior coordenada sempre na origem
baseDados_resumida_df["flag"] = False
baseDados_resumida_df.loc[baseDados_resumida_df.ORIGEM_LAT > baseDados_resumida_df.DESTINO_LAT, "flag"] = True

baseDados_resumida_df["Origem_Lat"] = baseDados_resumida_df.loc[:, "ORIGEM_LAT"]
baseDados_resumida_df["Origem_Lon"] = baseDados_resumida_df.loc[:, "ORIGEM_LON"]

baseDados_resumida_df["Destino_Lat"] = baseDados_resumida_df.loc[:, "DESTINO_LAT"]
baseDados_resumida_df["Destino_Lon"] = baseDados_resumida_df.loc[:, "DESTINO_LON"]

baseDados_resumida_df.loc[baseDados_resumida_df.flag == True, "Origem_Lat"] = baseDados_resumida_df["DESTINO_LAT"]
baseDados_resumida_df.loc[baseDados_resumida_df.flag == True, "Origem_Lon"] = baseDados_resumida_df["DESTINO_LON"]

baseDados_resumida_df.loc[baseDados_resumida_df.flag == True, "Destino_Lat"] = baseDados_resumida_df["ORIGEM_LAT"]
baseDados_resumida_df.loc[baseDados_resumida_df.flag == True, "Destino_Lon"] = baseDados_resumida_df["ORIGEM_LON"]

baseDados_filtrada_df = baseDados_resumida_df
baseDados_filtrada_df["Velocidade_Media"] = baseDados_resumida_df["VELOCIDADE_MEDIA"]
baseDados_filtrada_df["Km"] = baseDados_resumida_df["KM"]
baseDados_filtrada_df["Tempo_Deslocamento_Minutos"] = baseDados_resumida_df["TEMPO_DESLOCAMENTO_MIN"]

## Ordena as colunas de acordo com a coordenada, ordem crescente
baseDados_filtrada_df = baseDados_filtrada_df.sort_values(by=["Origem_Lat", "Origem_Lon", "Destino_Lat", "Destino_Lon"], ascending=True)
# ----

## Filtra somente as colunas de interesse
baseDados_filtrada_df = baseDados_filtrada_df
## ---

## Reseta o index da base de dados
baseDados_filtrada_df = baseDados_filtrada_df.reset_index(drop = True)
## ---

## Exporta dados filtrados
baseDados_filtrada_df.to_excel("dadosFiltrados.xlsx", index = False)
## ---
######################################## ANÁLISE ESTATÍSTICA DOS DADOS ######################################## 

##########################################
#
# SCRIPT PARA OBTENÇÃO DE DADOS ESTATISTICOS
#
# Script utilizado para obtenção da média, desvio padrão e número de elementos
#
#
##########################################

## Calcula a média, agrupando as colunas de coordenadas de origem e destino, em seguida cria um novo Data Frame temp
temp_Media= baseDados_filtrada_df.groupby(["Origem_Lat", "Origem_Lon", "Destino_Lat", "Destino_Lon"], as_index = False, sort = False).mean()
## Calcula o desvio padrão, agrupando as colunas de coordenadas de origem e destino, em seguida cria um novo Data Frame temp_Desvio
temp_Desvio = baseDados_filtrada_df.groupby(["Origem_Lat", "Origem_Lon", "Destino_Lat", "Destino_Lon"], as_index = False, sort = False).std()
## Conta a qtde de elementos, agrupando as colunas de coordenadas de origem e destino, em seguida cria um novo Data Frame temp_NElementos
temp_NElementos = baseDados_filtrada_df.groupby(["Origem_Lat", "Origem_Lon", "Destino_Lat", "Destino_Lon"], as_index = False, sort = False).count()
## ---

## Renomeia as colunas
temp_Media= temp_Media.rename(columns = {"Tempo_Deslocamento_Minutos": "Media_Tempo"}) 
temp_Desvio = temp_Desvio.rename(columns = {"Tempo_Deslocamento_Minutos": "DESVIO_PADRAO"})
temp_NElementos = temp_NElementos.rename(columns = {"Tempo_Deslocamento_Minutos": "N_ELEMENTOS"})
# ---

## Atribui as colunas de média, desvio padrão e qtde de elementos
estatistica_df = temp_Media
estatistica_df = estatistica_df.rename(columns = {"Velocidade_Media": "Media_VelocidadeMedia"})
estatistica_df = estatistica_df.rename(columns = {"Km": "Media_Km"})
estatistica_df["Desvio_Padrao_Tempo"] = temp_Desvio["DESVIO_PADRAO"]
estatistica_df["N_Elementos"] = temp_NElementos["N_ELEMENTOS"]
## ---

## Exporta os dados para excel
#estatistica_df.to_excel("dadosEstatisticos.xlsx", index = False)

### Base de dados utilizada para recalcular os dados estatísticos retirando os dados discrepantes
baseDadosReplicada_df = estatistica_df.reindex(estatistica_df.index.repeat(estatistica_df.N_Elementos)).reset_index(drop=True)

######################################## REMOÇÃO DOS DADOS (DE TEMPO) DISCREPANTES ######################################## 
##########################################
#
# SCRIPT PARA REMOÇÃO DE TEMPOS DISCREPANTES
#
# Script utilizado para remoção de tempos de deslocamentos discrepantes das demais amostras de determinado trajeto
#
#
##########################################

## Inicialmente a base de dados é igual a base de dados filtradas
dados_ReFiltrados_df = baseDados_filtrada_df
## ---

## Filtra e atribui as colunas de interesse da base de dados replicada a nova base de dados 
#dados_ReFiltrados_df[["Media_Tempo", "Desvio_Padrao_Tempo", "N_Elementos"]] = baseDadosReplicada_df.loc[:, "Media_Tempo":"N_Elementos"]
## ---

## Atribui _TOLERANCIA_DESVIO para a coluna de Desvio_Padrao_Tempo onde  o Desvio_Padrao_Tempo é maior que a TOLERANCIA_DESVIO
dados_ReFiltrados_df.loc[(dados_ReFiltrados_df.N_Elementos > _TOLERANCIA_QTDE_AMOSTRAS) & (dados_ReFiltrados_df.Desvio_Padrao_Tempo > _TOLERANCIA_DESVIO), "Desvio_Padrao_Tempo"] = _TOLERANCIA_DESVIO
## ---

## Atribui 0.00 na coluna de Media_Tempo, para os elementos no qual o tempo de deslocamento é maior que o tempo média + o desvio padrão, ou o tempo de deslocamento é menor que a média - desvio pradão do respectivo trajeto
dados_ReFiltrados_df.loc[(dados_ReFiltrados_df.N_Elementos > _TOLERANCIA_QTDE_AMOSTRAS) & ((dados_ReFiltrados_df.Tempo_Deslocamento_Minutos > (dados_ReFiltrados_df.Media_Tempo + dados_ReFiltrados_df.Desvio_Padrao_Tempo)) | (dados_ReFiltrados_df.Tempo_Deslocamento_Minutos < (dados_ReFiltrados_df.Media_Tempo - dados_ReFiltrados_df.Desvio_Padrao_Tempo)))
, "Media_Tempo"] = 0.00

## Filtra e atribui somente os dados no qual a Media_Tempo é diferente de 0.00, e filtra somente as colunas de Origem_Lat:Tempo_Deslocamento_Minutos
dados_ReFiltrados_df = dados_ReFiltrados_df.loc[dados_ReFiltrados_df.Media_Tempo != 0.00,:]
## ---


estatistica_df = dados_ReFiltrados_df[["Tempo_Deslocamento_Minutos", "TEMPO_COLETA_ENTREGA_MIN"]]

## Exporta os dados para excel
estatistica_df.to_excel("dadosEstatisticos.xlsx", index = False)





