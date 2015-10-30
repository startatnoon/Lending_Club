import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv') 
loansData.dropna(inplace=True) #removes null values
loansData.boxplot(column='Amount.Funded.By.Investors')
plt.title("Lending Club Loan Data")
plt.show()

loansData.hist(column='Amount.Funded.By.Investors')
plt.show()


plt.figure()
graph = stats.probplot(loansData['Amount.Funded.By.Investors'], dist="norm", plot=plt)
plt.show()