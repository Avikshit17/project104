import pandas as pd
df=pd.read_csv("Internet Users.csv")
height=df["Population"].tolist()

sum=0
for eachdata in height: 
    sum=float(eachdata)+sum
mean=sum/len(height)
print(mean)