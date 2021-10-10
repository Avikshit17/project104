import pandas as pd
df=pd.read_csv("height-weight.csv")
weight=df["Weight(Pounds)"].tolist()
weight.sort()
n=len(weight)
if(n%2==0):
    a1=weight[n//2]
    a2=weight[n//2-1]
    median=(a1+a2)/2
else:
    median=weight[n//2]
print(median)
