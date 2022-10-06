###### PACOTES ########
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np



################## LINEAR    #############################################################################

###### EXTRAÇÃO DADOS ########
data = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/ModeloLinear.xlsx')
data = data.rename( columns = {'Tempo (t)':'t','Entrada':'chu','R1 Modelo Linear': 'Modelo'} )


###### EXTRAÇÃO VARIÁVEIS ########
t = data['t']
chu = data['chu']
modelo=data['Modelo']


###### EXTRAÇÃO VARIÁVEIS PRO GRAFICO DE IMPULSOS ########
chuvas = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/Chuvas.xlsx')
chuvas = chuvas.rename(columns = {'Dias após primeira chuva':'tchu','Chuva [mm]':'c'})
tchu16=chuvas['tchu']
chu16=chuvas['c']
################################################





######################################################################################################################

               



############## EXPONENCIAL ########################################################################################

###### EXTRAÇÃO DADOS ########
data2 = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/DadosResistividadeChuvaPython.xlsx')
data2 = data2.rename( columns = {'Tempo (t)':'t','Entrada (u)': 'chu'} )

###### EXTRAÇÃO VARIÁVEIS ########
t2 = data2['t']
R1 = data2['R1']
chu2 = data2['chu']


################################################

#### CONSTANTES ####
A = 0.057
B = 1.34
C = 278.5399



############### REFAZ MODELO ################################################
h = ( np.exp( (-A) * t2) ) * (-B)
y = np.convolve(chu2,h,'full') + C 
y = y[0:len(t2)]    
            







######################################################################################################################











######### PLOTS ###########
fig, ax1 = plt.subplots(figsize=(15,5))

# # resposta aos impulsos LINEAR
ax1.plot(t, modelo, label = 'Modelo linear') 
plt.legend()

# # resposta aos impulsos EXPONENCIAL
plt.plot(t2, y, label = 'Modelo Exponencial') 
plt.legend()

# medições de resistividade
ax1.plot(t2, R1,'.', label = 'Medição de Resistividade')
plt.legend()
ax1.set_ylabel('Resistividade [Ohm*m]')
ax1.set_xlabel("Dias após primeira chuva")

# impulsos de chuva
ax2 = ax1.twinx()
ax2.set_ylabel('Chuva [mm]')
ax2.stem(tchu16,chu16, label = 'Chuvas')
plt.legend(loc='upper left')
plt.title("Resistividade em função do tempo")











