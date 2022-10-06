from scipy.stats import ttest_ind
import statistics as st


A=[6.5, 7, 5, 4.5, 8.5, 7, 6.5]
B=[6, 7, 7.5, 3, 5, 4, 4]

print(st.mean(A))
print(st.mean(B))

print(ttest_ind(A, B)) 
# Calculate the T-test for the means
# of two independent samples of scores.






