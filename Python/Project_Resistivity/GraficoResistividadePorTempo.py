########### PROJETO RESISTIVIDADE X CHUVA X TEMPO ################
###### PACOTES ########
import pandas as pd
import matplotlib.pyplot as plt

###### EXTRAÇÃO DADOS ########
data = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/Resistividades.xlsx')
data = data.rename(columns = 
                   {'Dias Após Primeira Chuva': 
                    't', 'Resist R1 [ohm]': 'R1', 'Resist R2 [ohm]': 
                        'R2', 'Chuva [mm]':'c'})
chuvas = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/Chuvas.xlsx')
chuvas = chuvas.rename(columns = {'Dias após primeira chuva':'tchu','Chuva [mm]':'c'})
    
###### EXTRAÇÃO VARIÁVEIS ########
t=data['t']
R1=data['R1']
R2=data['R2']
tchu=chuvas['tchu']
c=chuvas['c']

###### GRÁFICO RESISTIVIDADE 1 X TEMPO ########
fig, ax1 = plt.subplots()
ax1.plot(t, R1, label='Resistividade 1',marker='.', markersize = '10', color = 'darkgreen')
ax1.set_ylabel('Resistividade 1 [Ohm*m]')
ax1.set_xlabel("Dias após primeira medição")
plt.legend()

ax2 = ax1.twinx()
ax2.stem(tchu,c, bottom=0,label='Chuvas')
ax2.set_ylabel('Chuva [mm]')

plt.legend()
plt.title("Resistividade 1 em função do tempo")

###### GRÁFICO RESISTIVIDADE 2 X TEMPO ########
fig, ax1 = plt.subplots()
ax1.plot(t, R2, label='Resistividade 2',marker='.', markersize = '10', color='darkred')
ax1.set_ylabel('Resistividade 2 [Ohm*m]')
ax1.set_xlabel("Dias após primeira medição")
plt.legend()

ax2 = ax1.twinx()
ax2.stem(tchu,c, bottom=0,label='Chuvas')
ax2.set_ylabel('Chuva [mm]')

plt.legend()
plt.title("Resistividade 2 em função do tempo")






