###### PACOTES ########
import matplotlib.pyplot as plt
import pandas as pd

###### EXTRAÇÃO DADOS ########
data = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/ModeloLinear.xlsx')
data = data.rename( columns = {'Tempo (t)':'t','Entrada':'chu','R1Modelo': 'Modelo'} )

###### EXTRAÇÃO VARIÁVEIS ########
t = data['t']
R1 = data['R1']
R2 = data['R2']
chu = data['chu']
modelo=data['Modelo']


###### EXTRAÇÃO VARIÁVEIS PRO GRAFICO DE IMPULSOS ########
chuvas = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/Chuvas.xlsx')
chuvas = chuvas.rename(columns = {'Dias após primeira chuva':'tchu','Chuva [mm]':'c'})
tchu16=chuvas['tchu']
chu16=chuvas['c']
################################################




               
######### PLOTS ###########
fig, ax1 = plt.subplots(figsize=(15,5))

# # resposta aos impulsos
ax1.plot(t, modelo, label = 'Modelo linear') 
plt.legend()

# medições de resistividade
ax1.plot(t, R1,'.', label = 'Medição de Resistividade')
plt.legend()
ax1.set_ylabel('Resistividade [Ohm*m]')
ax1.set_xlabel("Dias após primeira chuva")

# impulsos de chuva
ax2 = ax1.twinx()
ax2.set_ylabel('Chuva [mm]')
ax2.stem(tchu16,chu16, label = 'Chuvas')
plt.legend(loc='upper left')
plt.title("Resistividade em função do tempo")
