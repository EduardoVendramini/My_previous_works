from scipy.stats import shapiro, ttest_1samp, levene, ttest_ind
import statistics as st
import numpy as np

#---------------------------------------------------------------------------

#################################### T- Test ############################# 
# O teste T tem dois tipos: o de uma amostra e o de duas amostras
# independentes.
# O com UMA amostra verifica se a média dessa é diferente de uma
# média conhecida ou hipotética.
# O teste T para 2 amostras verifica se há estatística que evidencie
# que as amostras têm valores de médias significativamente iguais.

#---------------------------------------------------------------------------

################# EXEMPLO MÉDIA DE ALUNOS DE UMA TURMA A #################
A = [6.5, 7, 5, 4.5, 8.5, 7, 6.5]

############################### NORMALIDADE ##############################
# Como o teste T é paramétrico, precisamos verificar se 
# a amostra tem distribuição normal
stat, p = shapiro(A)
print('stat=%.3f, p=%.3f' % (stat, p))
if p > 0.05:
	print('Gaussiana')
else:
	print('NÃO Gaussiana')
    
# Média aritmética da amostra
print(st.mean(A))

############################ T Test (1 amostra) ############################
# Se supormos que a média do grupo tende a 8,
# Ho => media igual a 8
# H1 => média menor de 8

tset, pval = ttest_1samp(A, 8, alternative = 'less') # equal_var=True, 
# alternative={'two-sided', ‘less’, ‘greater’}
print('P-valor = ', pval)
if pval < 0.05:    # Significância de 5%
   print("Rejeita-se hipótese nula")
else:
  print("Aceita-se hipótese nula")
# ou seja, com significancia de 5%, 
# não há estatística que evidencie que 
# a amostra tenha média igual a 8

#---------------------------------------------------------------------------

############################### T Test (2 amostras) ######################## 
############################### TURMAS A  E B ##############################
# A = [6.5, 7, 5, 4.5, 8.5, 7, 6.5]
B = [6, 7, 7.5, 3, 5, 4, 4]

# NORMALIDADE DE B
stat, p = shapiro(B)
print('stat=%.3f, p=%.3f' % (stat, p))

if p > 0.05:
	print('Gaussiana')
else:
	print('NÃO Gaussiana')

# Médias amostrais de âmbas as amostras
print("média da turma A = ", st.mean(A))
print("média da turma B = ", st.mean(B))
print("variância da turma A = ", st.variance(A))
print("variância da turma B = ", st.variance(B))

################################ Teste de variâncias ########################

stat, p = levene(A, B)
p
# H0 => Variâncias iguais - homocedasticidade
# h1 => Variâncias diferentes - heterocedasticidade

if p < 0.05:
  print("Rejeita-se hipótese nula. As variâncias são diferentes")
else:
  print("Aceita-se hipótese nula. As variâncias são iguais")


####################### T Test (2 amostras) ################################
# Ho => media de A é igual a B
# H1 => média de A é maior que B

ttest, pval = ttest_ind(A, B, alternative = 'greater')
# alternative={'two-sided', ‘less’, ‘greater’}
print("p-value", pval)
if pval < 0.05:
  print("Rejeita-se hipótese nula. A média de A é MAIOR que de B")
else:
  print("Aceita-se hipótese nula. A média de A é igual a de B")
  
# Portanto, aceita-se a hipótese nula de que as médias são iguais

#---------------------------------------------------------------------------

################ Teste de hipóteses para VARIÂNCIA ########################
# Brown-Forsythe.
# homogeneidade de variâncias (homoscedasticidade)

a = [8.88, 9.12, 9.04, 8.98, 9.00, 9.08, 9.01, 8.85, 9.06, 8.99]
b = [8.88, 8.95, 9.29, 9.44, 9.15, 9.58, 8.36, 9.18, 8.67, 9.05]
c = [8.95, 9.12, 8.95, 8.85, 9.03, 8.84, 9.07, 8.98, 8.86, 8.98]

stat, p = levene(a, c)
p
# H0 => Variâncias iguais (homogêneas) - homocedasticidade
# h1 => Variâncias diferentes (heterogêneas) - heterocedasticidade
if p < 0.05:
  print("Rejeita-se hipótese nula. As variâncias são diferentes")
else:
  print("Aceita-se hipótese nula. As variâncias são iguais")
# The small p-value suggests that the populations do not have equal 
# variances.
# This is not surprising, given that the sample variance of b is 
# much larger than that of a and c:

# Cálculo das variâncias efetivamente
np.var(a)
np.var(b)
np.var(c)







