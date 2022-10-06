import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats

# Generate random data
np.random.seed(12)
races =   ["asian","black","hispanic","other","white"]
voter_race = np.random.choice(a = races,
                              p = [0.05, 0.15 ,0.25, 0.05, 0.5],
                              size=1000)

voter_age = stats.poisson.rvs(loc=18, mu=30, size=1000)

# Group age data by race
voter_frame = pd.DataFrame({"race":voter_race,"age":voter_age})
groups = voter_frame.groupby("race").groups

# Etract individual groups
asian = voter_age[groups["asian"]]
black = voter_age[groups["black"]]
hispanic = voter_age[groups["hispanic"]]
other = voter_age[groups["other"]]
white = voter_age[groups["white"]]

# Perform the ANOVA
# The samples are independent.
# Each sample is from a normally distributed population.
# The population standard deviations of the groups are all equal. 
# This property is known as homoscedasticity.

fstats, pvalue = stats.f_oneway(asian, black, hispanic, other, white)
# comentar sobre ANOVA com 2 ou mais fatores ex: (idade, classe e genero)
# H0 => Médias iguais
# H1 => Médias diferentes
print('P-valor = ', pvalue)
if pvalue < 0.05:    # Significância de 5%
   print("Rejeita-se hipótese nula. Médias diferem")
else:
  print("Falhamos em rejeitar a hipótese nula. Médias iguais")


# OUTRO MODO SIMILIAR TO R
import statsmodels.api as sm
from statsmodels.formula.api import ols

model = ols('age ~ race', data = voter_frame).fit() # Mínimos quadrádos ordinários
anova_result = sm.stats.anova_lm(model, typ=2)
print (anova_result)


# Generate random data com uma mostra diferente
np.random.seed(12)
voter_race = np.random.choice(a= races,
                              p = [0.05, 0.15 ,0.25, 0.05, 0.5],
                              size=1000)

# Use a different distribution for white ages
white_ages = stats.poisson.rvs(loc=18, mu=32, size=1000)
voter_age = stats.poisson.rvs(loc=18, mu=30, size=1000)
voter_age = np.where(voter_race=="white", white_ages, voter_age)

# Group age data by race
voter_frame = pd.DataFrame({"race":voter_race,"age":voter_age})
groups = voter_frame.groupby("race").groups   

# Extract individual groups
asian = voter_age[groups["asian"]]
black = voter_age[groups["black"]]
hispanic = voter_age[groups["hispanic"]]
other = voter_age[groups["other"]]
white = voter_age[groups["white"]]

# Perform the ANOVA again
fstats, pvalue = stats.f_oneway(asian, black, hispanic, other, white)
# H0 => Médias iguais
# H1 => Médias diferentes
print('P-valor = ', pvalue)
if pvalue < 0.05:    # Significância de 5%
   print("Rejeita-se hipótese nula. Médias diferem")
else:
  print("Falhamos em rejeitar a hipótese nula. Médias iguais")

# Alternate method
model = ols('age ~ race', data = voter_frame).fit()
anova_result = sm.stats.anova_lm(model, typ=2)
print (anova_result)


# TUKEY AGORA
# H0 => 
from statsmodels.stats.multicomp import pairwise_tukeyhsd

tukey = pairwise_tukeyhsd(endog=voter_age,     # Data
                          groups=voter_race,   # Groups
                          alpha=0.05)          # Significance level

tukey.plot_simultaneous()    # Plot group confidence intervals
plt.vlines(x=49.57,ymin=-0.5,ymax=4.5, color="red")

print(tukey.summary())              # See test summary
