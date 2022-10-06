import pandas as pd
import scipy.stats as stats
from statsmodels.stats.multicomp import MultiComparison
import numpy as np

# Carregar dados
data = pd.read_excel('C:/Users/eduardo/Desktop/IC/6AULAANOVA/LENHA.xlsx')
A = data['A']
B = data['B']
C = data['C']

############################### ANOVA ############################
# analisa se há diferença significativa entre as médias de 
# 3 ou mais grupos analisando apenas 1 fator (one way)
# Amostras devem ser independentes
# Devem ter distribuição normal
# Variâncias devem sei iguais

fstats, pvalue = stats.f_oneway(A, B, C)
# H0 => Médias iguais
# H1 => Médias diferentes
print('P-valor = ', pvalue)
if pvalue < 0.05:    # Significância de 5%
   print("Rejeita-se hipótese nula. Médias diferem")
else:
  print("Falhamos em rejeitar a hipótese nula. Médias iguais")

####################### TUKEY ###########################
# Retorna: 
# 'True' se a média se difere das demais
# 'False' se a média não se difere

dadosempilhados = data.stack().reset_index()
dadosempilhados = dadosempilhados.rename(
    columns = {'level_1': 'tratamento', 0:'resultado'} )

MultiComp = MultiComparison(dadosempilhados['resultado'],
                            dadosempilhados['tratamento'])

print(MultiComp.tukeyhsd(alpha=0.05).summary())
np.mean(A)
np.mean(B)
np.mean(C)


