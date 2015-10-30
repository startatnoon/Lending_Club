#I will use 2013-2014 data because it is fairly recent and lots of data
#although I could probably load more data to the bottom
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

theLoans = pd.read_csv('LoanStats3c.csv',skiprows=1)
theLoans=theLoans.dropna()
theLoans['int_rate'] = theLoans['int_rate'].map(lambda x: float(x.rstrip('%')) / 100)
theLoans['intercept'] = 1.0
theLoans['home_ownership'] = pd.Categorical(theLoans['home_ownership']).labels
#interest rates based on income
#x = np.column_stack([theLoans['annual_inc'],theLoans['intercept']])
#X = sm.add_constant(x)
m1 = sm.OLS(theLoans['int_rate'], theLoans['annual_inc'])
result1= m1.fit()
print result1.summary()

m2 = sm.OLS(theLoans['int_rate'], theLoans[['annual_inc','home_ownership']])
result2= m2.fit()
print result2.summary()

m3 = sm.OLS(theLoans['int_rate'], theLoans[['annual_inc','home_ownership','intercept']])
result3= m3.fit()
print result3.summary()


#questions for mentor
#what is the matrix form of x?
#What is interaction of home_ownership and incomes?