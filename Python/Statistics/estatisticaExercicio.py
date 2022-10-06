import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statistics as st
import numpy as np

# CARREGANDO DADOS PARA O EXERCÍCIO
data=pd.read_excel('C:/Users/eduardo/Desktop/IC/3AULASESTATISTICA/DADO1.xlsx')

###################### DIAGRAMA DE DISPERSÃO ###########################
sns.relplot(data=data,x='TAXAMORT',y='TAXAALFAB',hue='MUNICIPIO',
            s=50,height=5, aspect=1.5) 
plt.xlabel('Taxa de alfabetização')
plt.ylabel('Taxa de mortalidade infantil')
plt.title('Mortalidade x Alfabetização')
#numeros?????equação e R² E OUTRO MODELO EM CIMA DESSE GRÁGFICO

###################### MODELO LINEAR ###########################
sns.regplot(x="TAXAMORT", y="TAXAALFAB",data=data) 
plt.title('Diagrama de Dispersão')
plt.xlabel('Taxa de alfabetização')
plt.ylabel('Taxa de mortalidade infantil')
plt.figure(figsize=(1,1))
#numeros?????


from sklearn.linear_model import LinearRegression

x = data['TAXAMORT']
y = data['TAXAALFAB']
reg = LinearRegression().fit(x, y)
reg.score(x, y)
reg.coef()
reg.intercept()
reg.predict(np.array([[3, 5]]))

###################### MODELO LOGARÍTMICO ###########################
sns.regplot(x="TAXAMORT", y="TAXAALFAB",data=data, logx=True) 
plt.title('Diagrama de Dispersão')
plt.xlabel('Taxa de alfabetização')
plt.ylabel('Taxa de mortalidade infantil')


###################### BOXPLOTS ###########################
sns.boxplot(data=data['TAXAMORT'])
plt.title('Boxplot taxa de mortalidade infantil')

sns.boxplot(data=data['TAXAALFAB'])
plt.title('Boxplot taxa de alfabetização')

data.boxplot(column=['TAXAALFAB','TAXAMORT']) #PLT
plt.title('BOXPLOTS')


###################### CORRELAÇÃO ###########################
data.corr(method='pearson',min_periods=1)
# pearson : standard correlation coefficient
# kendall : Kendall Tau correlation coefficient
# spearman : Spearman rank correlation


###################### ESTATÍSTICA DESCRITIVA ###########################

# Função que ordena os dados !
vetor=data['POPULACAO']
vetor=np.sort(data['POPULACAO'])
st.multimode(vetor) #se não for unimodal

# QUARTIS
np.quantile(vetor, q=.5) #q=0 LI, q=.25 Q1, q=.5 Mediana, q=.75 Q2, q=1 LS
np.quantile(vetor, q=1) # percentil 100

data.mean() #retorna a média de cada coluna
data.median() #retorna a mediana de cada coluna
data.mode() #retorna a moda de cada coluna
data.var() #retorna a variância de cada coluna
data.max() #retorna valor máximo de cada coluna
data.min() #retorna valor ínimo de cada coluna
data.cov() #retorna uma matriz indicando a covariância de cada coluna com outra
data.corr()#retorna uma matriz com a correlação de cada coluna com as outras colunas do Dataframe

# ASSIMETRIA
data.skew()
#Assimetria (skewness): mede o grau de simetria da curva, em relação a 
#distribuição normal.

# Uma assimetria positiva, com valor > 0, significa que 
# a cauda da distribuição está mais para a direita. 
# Ou seja, que os valores de moda < mediana < média.

# Uma assimetria negativa, com valor < 0, significa que a 
# cauda da distribuição está mais para a esquerda. 
# Ou seja, que os valores de média < mediana < moda.

# CURTOSE
data.kurtosis()
# leptocúrtica
# mesocúrtica
# platicúrtica
# Se o valor encontrado é igual 0, você tem uma distribuição 
# mesocúrtica; se maior que 0, leptocúrtica, correspondendo a 
# uma curva mais pontuda; se menor que 0, platicúrtica, ou seja, 
# uma curva mais achatada, com maior variabilidade dos dados.


# ESTATISTICA COMPLETA
data.describe()



