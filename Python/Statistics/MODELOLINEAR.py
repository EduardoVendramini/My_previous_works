import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import seaborn as sns

############## EXTRAÇÃO DE VARIÁVEIS A SEREM TRABALHADAS ####################
dados = pd.read_excel('C:/Users/eduardo/Desktop/IC/3AULASESTATISTICA/DADO1.xlsx')


#Correlação entre os dados
dados.corr()

dados.head()
X = dados['POPULACAO'].values
Y = dados['CRESCDEMO'].values



############## REGRESSÃO LINEAR ####################
X = sm.add_constant(X) 
modelo = sm.OLS(Y, X) # Método Mínimos Quadrados Ordinários
resultado = modelo.fit() # ajuste do modelo
print(resultado.summary())
coef_linear, coef_angular = resultado.params
reta = coef_angular*X+coef_linear

X = X[:,1] #exclui primeira coluna da matriz
reta = reta[:,1] #exclui primeira coluna da matriz


############## GRÁFICO COM MODELO LINEAR ####################
sns.relplot(data=dados,x=X,y=Y,hue='MUNICIPIO',s=50,height=5, aspect=1.5) 
plt.plot(X,reta,color='red');
plt.xlabel('População urbana')
plt.ylabel('Crescimento demográfico')
plt.title('Relação entre crescmiento demográfico e população de municípios')






# ############## Erro médio absoluto ####################
# MAE = mean_absolute_error(Y,reta)
# print("MAE = {:0.2f}".format(MAE))
# ############## Erro quadrático médio ####################
# RMSE = np.sqrt(mean_squared_error(Y,reta))
# print("RMSE = {:0.2f}".format(RMSE))



