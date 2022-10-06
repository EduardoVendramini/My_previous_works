########### PROJETO RESISTIVIDADE X CHUVA X TEMPO ################
###### PARTE - CONVOLUÇÃO ########
###### PACOTES ########
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

###### EXTRAÇÃO DADOS ########
data = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/ModeloDeAjuste.xlsx')
data = data.rename(columns = {'Tempo (t)': 't', 'Entrada (u)': 'c'})

###### EXTRAÇÃO VARIÁVEIS ########
t=data['t']
R1=data['R1']
c=data['c']

###### PLOT SIMPLES ########
plt.figure(figsize=[15,5])
plt.plot(t,R1,'.')

plt.figure(figsize=[15,5])
plt.plot(t,c,'.')




x=np.array([-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10])
#y=[250,260,265,267,190,205,215,190,200,207]
y=x*x

plt.figure(figsize=[15,5])
plt.plot(x,y)

# y - saída (resistividade)
# x - entrada (chuva)
# h - resposta a um impulso (a uma chuva)
# y = convolve(x,h)



conv=np.convolve(x,y,'same')
# full não corta, same corta o fim e valid corta o começo e fim
plt.plot(x,conv)


#y=np.convolve(R1, c, mode='same')
y=np.convolve([5,0,0,0,30,0,0,8,0,0],[250,260,265,267,190,205,215,190,200,207], 'same')
plt.figure(figsize=[15,5])
plt.plot(x,y)

