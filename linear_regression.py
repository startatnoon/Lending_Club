import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statsmodels.api as sm

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData['Interest.Rate'][0:5] # first 5 rows of Interest.Rate
# 81174     8.90%
# 99592    12.12%
# 80059    21.98%
# 15825     9.99%
# 33182    11.71%
# Name: Interest.Rate, dtype: object

loansData['Loan.Length'][0:5] # first 5 rows of Loan.Length
# 81174    36 months
# 99592    36 months
# 80059    60 months
# 15825    36 months
# 33182    36 months
# Name: Loan.Length, dtype: object

loansData['FICO.Range'][0:5] # first 5 rows of FICO.Range
# 81174    735-739
# 99592    715-719
# 80059    690-694
# 15825    695-699
# 33182    695-699
# Name: FICO.Range, dtype: object

loansData['Interest.Rate'] = loansData['Interest.Rate'].map(lambda x: round(float(x.rstrip('%')) / 100, 4))
cleanLoanLength = loansData['Loan.Length'].map(lambda x: int(x.rstrip(' months')))
cleanFICO = loansData['FICO.Range'].map(lambda x: int(x[0:3]))
loansData['FICO.Score'] = cleanFICO
loansData['Loan.Length'] = cleanLoanLength

#plt.figure()
#p = loansData['FICO.Score'].hist()
#plt.show()
#a = pd.scatter_matrix(loansData, alpha=0.05, figsize=(10,10), diagonal='hist')
intrate = loansData['Interest.Rate']
loanamt = loansData['Amount.Requested']
fico = loansData['FICO.Score']

loansData.to_csv('loansData_clean.csv', header=True, index=False)

# The dependent variable
y = np.matrix(intrate).transpose()
# The independent variables shaped as columns
x1 = np.matrix(fico).transpose()
x2 = np.matrix(loanamt).transpose()
x = np.column_stack([x1,x2])
X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit()
print f.summary()