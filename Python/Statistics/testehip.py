import random as rd
import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np
import statistics as st


############### distribuição gaussiana (normal) em torno da média ############################
aleat4 = []
for i in range(1000):
    aleat4.append( rd.gauss(0,1) ) #rd.gauss(media,desvio padrao)

plt.hist(aleat4,bins=10,density=True, color = 'gray')
plt.xlabel('classes')
plt.ylabel('frequencia')

# comparando com curva teórica
xmin,xmax=plt.xlim()
med=st.mean(aleat4)
desv=st.pstdev(aleat4)
eix=np.linspace(xmin,xmax,5)
eiy=norm.pdf(eix,med,desv)  # probability density function
plt.plot(eix,eiy,color='black')

################################ distribuição uniforme  ###############################################
# distribuição uniforme
aleat2 = []
for i in range(1000):
    aleat2.append( rd.uniform(-50,50) ) #todos numeros com msm prob de ocorrer

plt.hist(aleat2,bins=10,color='gray')
plt.xlabel('classes')
plt.ylabel('frequencia')

# comparando com curva teórica
xmin,xmax=plt.xlim()
med=st.mean(aleat2)
desv=st.pstdev(aleat2)
eix=np.linspace(xmin,xmax,10)
#eiy=eix-################### verificar
plt.plot(eix,eiy,color='black')






