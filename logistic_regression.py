#logistic_regression.py
import pandas as pd
import statsmodels.api as sm
import math

loansData = pd.read_csv('./loansData_clean.csv')
loansData['IR_TF'] = loansData['Interest.Rate'].map(lambda x: int(x >= .12))
loansData[loansData['Interest.Rate']==.1].head()
#rename a column
#loansData = loansData.rename(columns={'Intercept': 'int'})
#ind_vars = list(loansData.columns.values)
loansData['Intercept'] = 1.0
ind_vars = ['FICO.Score','Amount.Requested', 'Intercept']
#interest_rate = b + a1(FICOScore) + a2(LoanAmount)
logit = sm.Logit(loansData['IR_TF'], loansData[ind_vars])
result = logit.fit()
coeff = result.params
print coeff

def logistic_function(a,b):
	return 1/(1+math.exp(coeff[2]+coeff[1]*a+coeff[0]*b))

print logistic_function(10000,720)
#p is above .7, accept as true

def pred(a,b):
	if logistic_function(a,b) >= .7:
		print "Loan at or under 12%% approved"
	else:
		print "Loan at or under 12%% not approved"

