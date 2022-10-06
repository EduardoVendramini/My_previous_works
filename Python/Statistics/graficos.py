import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

############### BOXPLOT ################
data = pd.read_excel ('C:/Users/eduardo/Desktop/UTFPR/IC/PAITON/Graficos/dados.xlsx')
vet=data['nome']
sns.boxplot(vet,color='gray')
plt.title('BOXPLOT')



############### HISTOGRAMA ################
data2 = pd.read_table ('C:/Users/eduardo/Desktop/UTFPR/IC/PAITON/Graficos/dados.txt')
plt.style.use('fivethirtyeight')
#bins = [100,130,160,190,210]
vet2=data2['nome']
plt.hist(vet2,bins=5,edgecolor='black', color = 'brown')
plt.title('HISTOGRAMA')
plt.xlabel('idade')
plt.ylabel('n de ocorrencias')


############### DIAGRAMA DE DISPERSÃO ################
data3=pd.read_excel('C:/Users/eduardo/Desktop/UTFPR/IC/PAITON/Graficos/dispersao.xlsx')
temp=data3['tempo']
resist=data3['resistividade']
sns.scatterplot(temp, resist) 
plt.title('TITULO')

sns.lineplot(x="tempo", y="resistividade",data=data3)#COM LINHA
plt.title('Diagrama de Dispersão')

sns.regplot(temp, resist) #MODELO LINEAR

ax = sns.regplot(resist,temp, logx=True, fit_reg=True) #MODELO LOGARITMICO


############### GRÁFICO EM BARRAS ################
height = [3, 12, 5, 18, 45]
bars = ('A', 'B', 'C', 'D', 'E')
#HORIZONTAL
plt.title('TITULO')
plt.barh(bars, height)

#VERTICAL
plt.title('Gráfico de Barras')
plt.bar(bars, height)


############### GRÁFICO DE SETORES ################
labels = 'A', 'B', 'C', 'D'
sizes = [12, 11, 3, 30]
explode = (0, 0.2, 0, 0) 
plt.pie(sizes, explode=explode, labels=labels, autopct='%.1f%%',
        shadow=True, startangle=90)
plt.title('Gráfico de setores')
plt.axis('equal')









