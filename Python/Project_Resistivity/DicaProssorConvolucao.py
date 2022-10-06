###### PACOTES ########
import matplotlib.pyplot as plt
import numpy as np

t = np.array(range(80)) # t em dias
x = np.array(range(len(t)))*0 # x em mm
x[10]=10
x[30]=20


a = 0.05
b = 1.55
c = 310
h = ( np.exp(-a * t) ) * -b

#### impulsos ####
plt.figure(figsize=[15,5])
plt.plot(t,x)

#### resposta a 1 impulso ####
plt.figure(figsize=[15,5])
plt.plot(t,h) # 1 impulso

#### resposta a entrada ####
y = np.convolve(x,h,'full') + c
y = y[0:len(t)]
plt.figure(figsize=[15,5])
plt.plot(t,y) # resposta aos impulsos

# colocar segundo e ultima juntas
fig, ax1 = plt.subplots()
ax1.stem(t,x,'r')
ax2 = ax1.twinx()
ax2.plot(t,y)


# y - saída (resistividade)
# x - entrada (chuva)
# h - resposta a um impulso (a uma chuva)
# y - convolve(x,h)
# t - tempo
