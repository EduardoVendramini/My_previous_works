###### PACOTES ########
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


###### EXTRAÇÃO DADOS ########
data = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/NOVOSDADOSCONDUTIVIDADE.xlsx')
data = data.rename( columns = {'Tempo (t)':'t','Entrada (u)': 'chu'} )


###### EXTRAÇÃO VARIÁVEIS ########
t = data['t']
R1 = data['CON1']
R2 = data['CON2']
chu = data['chu']


###### EXTRAÇÃO VARIÁVEIS PRO GRAFICO DE IMPULSOS ########
chuvas = pd.read_excel ('C:/Users/eduardo/Desktop/IC/ProjetoResistividade/Chuvas.xlsx')
chuvas = chuvas.rename(columns = {'Dias após primeira chuva':'tchu','Chuva [mm]':'c'})
tchu16=chuvas['tchu']
chu16=chuvas['c']







#################### CONSTANTES ###########################
a = 0.016 # intervalo de 0 a 1 incrementando 0,001
b = 4.4E-05 # intervalo de 0,000 100 a 0,000 300 incrementando 0,000 001
c = 0 # intervalo de 0 a 1 incrementando 0,001




# # #### FUNÇÃO EXPONENCIAL AO LONGO TO TEMPO #####
# h = ( np.exp( (-a) * t) ) * (b)

# # #### impulsos ####
# plt.figure(figsize=[15,5])
# plt.stem(t,chu)

# # #### resposta da exponencial a 1 impulso na origem ####
# plt.figure(figsize=[15,5])
# plt.plot(t,h,'.') # 1 impulso

# # #### resposta a entrada ####
# y = np.convolve(chu,h,'full') + c 
# y = y[0:len(t)]             
            
               
# ######### PLOTS ###########
# fig, ax1 = plt.subplots(figsize=(15,5))

# # # resposta aos impulsos
# ax1.plot(t, y, label = 'Resposta aos impulsos') 
# plt.legend()

# # medições de resistividade
# ax1.plot(t, R1,'.', label = 'Medição de Condutividade')
# plt.legend()
# ax1.set_ylabel('Condutividade [Siemens/m]')
# ax1.set_xlabel("Dias após primeira chuva")

# # impulsos de chuva
# ax2 = ax1.twinx()
# ax2.set_ylabel('Chuva [mm]')
# ax2.stem(tchu16,chu16, label = 'Chuvas')
# plt.legend(loc='upper right')
# plt.title("Condutividade em função do tempo")








x=10E5
for A in np.arange(0.016,0.017,1e-04):#(start,stop,step)
    for B in np.arange(4.4e-05,4.5e-05,1e-06):
        for C in np.arange(0,0.050,0.001):
            
            ############### REFAZ MODELO ################################################
            h = ( np.exp( (-A) * t) ) * (B)
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

# out 0.00014725902449511775 0.016 4.4e-05 0.0





############### MODELO NOVO ###############
h = ( np.exp( (-a) * t) ) * (b)
y = np.convolve(chu,h,'full') + c 
y = y[0:len(t)]               
            
               
            
            
            
            
            
######### PLOTS ###########
fig, ax1 = plt.subplots(figsize=(15,5))

# # resposta aos impulsos
ax1.plot(t, y, label = 'Resposta aos impulsos') 
plt.legend()

# medições de resistividade
ax1.plot(t, R1,'.', label = 'Medição de Condutividade')
plt.legend()
ax1.set_ylabel('Condutividade [Siemens/m]')
ax1.set_xlabel("Dias após primeira chuva")

# impulsos de chuva
ax2 = ax1.twinx()
ax2.set_ylabel('Chuva [mm]')
ax2.stem(tchu16,chu16, label = 'Chuvas')
plt.legend(loc='upper right')
plt.title("Condutividade em função do tempo")


