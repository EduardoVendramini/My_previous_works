import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Carregando dados do tipo txt
dados = pd.read_table('C:/Users/eduardo/Desktop/IC/4AULAREGRASSAO/DADOS.txt')


# Verificar se há correlação entre os dados
dados.corr()


# Diagrama de dispersão sem modelo
X = dados['ANOS'].values
Y = dados['CLIENTES'].values
plt.scatter(X,Y);
plt.title('Número de clientes com respeito aos anos do empregado na empresa')
plt.xlabel('Anos na empresa');
plt.ylabel('Número de clientes');


# Variáveis para o cálculo do modelo
media_X = np.mean(X)
media_Y = np.mean(Y)
erro_x = X-media_X
erro_y = Y-media_Y

# Cálculo efetivamente
soma_erro_xy = np.sum(erro_x*erro_y)
erro_x_quadratico = (X-media_X)**2.0
soma_erro_x_quadratico = np.sum(erro_x_quadratico)
m = soma_erro_xy / soma_erro_x_quadratico

print("Coeficiente angular = {:0.2f}".format(m))

c = media_Y - m*media_X

print("Coeficiente linear = {:0.2f}".format(c))

reta = m*X+c

# Diagrama de dispersão com modelo linear
plt.scatter(X,Y);
plt.plot(X,reta,label='Ajuste linear',color='red');
plt.title('Número de clientes com respeito aos anos do empregado na empresa')
plt.xlabel('Anos na empresa');
plt.ylabel('Clientes obtidos');




























