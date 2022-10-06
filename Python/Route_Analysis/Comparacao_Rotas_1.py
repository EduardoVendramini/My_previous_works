import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

############### DADOS ################
data = pd.read_excel ('C:/Users/eduardo/Documents/GitHub/Rotas_Via_Lacteos/src/Script_Estatistica_Total/Comparacao30RotasAbril.xlsx')
# Se não tiver medição de tempo real exclui linha
data.drop(data[(data['Tempo real']=='?')].index, inplace=True)
data = data.astype({'Tempo real':'float'})
# Estatística dos dados
describe=data.describe()


############### BOXPLOT DOS ERROS ################
# NOSSO SOFTWARE
erro1=data['Erro Software']
sns.boxplot(erro1,color='gray')
plt.title('Erro absoluto software')
# PLANO DELES
erro2=data['Erro deles']
sns.boxplot(erro2,color='brown')
plt.title('Erro absoluto planejamento antigo')


############### DIAGRAMA DE DISPERSÃO ################
Rota=data['Rota']
Dia=data['Dia']
Real=data['Tempo real']
Software=data['Tempo Software']
PlanoAntigo=data['Tempo Previsto deles']
x = np.arange(0, 25, 1)

plt.xticks(x,Dia, rotation=70)
plt.plot(x, Real, color='red',label='Tempo de rota real') 
plt.plot(x, Software, color='purple',label='Tempo Software')
plt.plot(x,PlanoAntigo,color='blue',label='Plano antigo')
plt.title('Tempo de rotas por dia de execução')
plt.legend()
plt.ylabel('Tempo de rotas em horas')



############### GRÁFICO DE BARRAS ################
# média dos tempos de rotas
media_tempo = [describe._get_value('mean', 'Tempo Software'),
describe._get_value('mean', 'Tempo real'),
describe._get_value('mean', 'Tempo Previsto deles')]
descricao = ['Software','Real','Previsão antiga']
plt.bar(descricao, media_tempo)
plt.title('Tempo médio de rota em horas')

# Erro em porcentagem
media_erro = [describe._get_value('mean', 'Erro Software')*100,
describe._get_value('mean', 'Erro deles')*100]
descricao = ['Software','Previsão antiga']
plt.bar(descricao, media_erro)
plt.title('Erro médio de tempo de rota')
plt.ylabel('Porcento')

# Erro considerando uma rota de 11h
media_erro = [describe._get_value('mean', 'Erro Software')*11,
describe._get_value('mean', 'Erro deles')*11]
descricao = ['Software','Previsão antiga']
plt.bar(descricao, media_erro)
plt.title('Erro médio de tempo de uma rota de 11h')
plt.ylabel('Horas')

############### GRÁFICO DE SETOR ################
# Quantas vezes o nosso se mostrou melhor
data['Nosso_Melhor'] = data.apply(lambda x: True
            if x['Erro Software'] < x['Erro deles'] else False, axis = 1)
true_count = data.Nosso_Melhor.sum()
false_count = len(data) - true_count
y = [true_count, false_count]
mylabels = ["Software", "Previsão antiga"]
plt.pie(y, labels = mylabels, startangle = 90, autopct='%1.1f%%')
plt.title('Número de vezes que o resultado é mais próximo ao real')
