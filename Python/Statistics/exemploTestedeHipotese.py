import statsmodels.api as sm

## colocar um problema com esse de proporção !!!

n = 1018 # sample
pnull = .52 # null hypothesis
phat = .56 # percentage of those who believe 
# the eletctronics do affect the teenagers sleep

# Ho => de que a proporção é igual a 0.52
# H1 => proporção maior que 0.52

# p valor < nivel de significancia => rejeita-se H0

z, p = sm.stats.proportions_ztest(phat * n, n, pnull, 
                           alternative='larger') 
# alternative='two-sided'
print(z,p)
# out -> (z-statistic , the corresponding p-value)


if p < 0.05:
	print('Null hypothesis rejected')
else:
	print('Alternative hypothesis rejected')

# null rejected implies that indeed more than 52% 
# of the parents believe the electronics interfere 

# Teste de hipóteses para VARIÂNCIA




