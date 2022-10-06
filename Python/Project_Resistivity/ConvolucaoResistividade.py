###### PACOTES ########
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

###### EXTRAÇÃO DADOS ########
data = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/DadosResistividadeChuvaPython.xlsx')
data = data.rename( columns = {'Tempo (t)':'t','Entrada (u)': 'chu'} )

###### EXTRAÇÃO VARIÁVEIS ########
t = data['t']
R1 = data['R1']
R2 = data['R2']
chu = data['chu']

###### EXTRAÇÃO VARIÁVEIS PRO GRAFICO DE IMPULSOS ########
chuvas = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/Chuvas.xlsx')
chuvas = chuvas.rename(columns = {'Dias após primeira chuva':'tchu','Chuva [mm]':'c'})
tchu16=chuvas['tchu']
chu16=chuvas['c']
################################################

#### CONSTANTES ####
a = 0.05
b = 1.55
c = 310

# #### FUNÇÃO EXPONENCIAL AO LONGO TO TEMPO #####
# h = ( np.exp( (-a) * t) ) * (-b)

# #### impulsos ####
# plt.figure(figsize=[15,5])
# plt.stem(t,chu)

# #### resposta da exponencial a 1 impulso na origem ####
# plt.figure(figsize=[15,5])
# plt.plot(t,h,'.') # 1 impulso

# #### resposta a entrada ####
# y = np.convolve(chu,h,'full') + c 
# y = y[0:len(t)]







################ OTIMIZAÇÃO DE PARÂMETROS ################
x=10E5
for A in np.arange(0.05,0.06,.001):#(start,stop,step)
    for B in np.arange(1.3,1.4,.01):
        for C in np.arange(278,280,0.01):
            
            ############### REFAZ MODELO ################################################
            h = ( np.exp( (-A) * t) ) * (-B)
            y = np.convolve(chu,h,'full') + C 
            y = y[0:len(t)]    
            
            ############### CALCULA SOMA DOS RESIDUOS ###################################
            soma=0
            for i in range(len(y)):
                if R1[i] > 0: # verifica se o valor medido existe
                    soma = soma + (R1[i]-y[i])**2
            
            ########### VERIFICA VALOR MAIS BAIXO DE SOMA DOS RESIDUOS #################
            if soma < x:
                x=soma
                a=A
                b=B
                c=C
print(x,a,b,c)   

# out 71160.74575205758 0.05700000000000001 1.34 278.5399999999995












######### PLOTS ###########

fig, ax1 = plt.subplots(figsize=(15,5))

# resposta aos impulsos
ax1.plot(t, y, label = 'Resposta aos impulsos') 
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



# y - saída (resistividade)
# chu - entrada (chuva)
# h - resposta a um impulso (a uma chuva)
# y - convolve(x,h)
# t - tempo
